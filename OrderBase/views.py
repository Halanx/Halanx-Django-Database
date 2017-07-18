from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import OrderSerializer
from OrderBase.models import Order
from Carts.models import Cart, CartItem
from UserBase.models import User
from Products.models import Product
from ShopperBase.models import Shopper
from BatchBase.models import Batch
from BatchBase.serializers import BatchSerializer
from Carts.serializers import CartItemSerializer
import requests
from Halanx import settings

from batch_maker import find_shopper, cluster_by_location

import numpy as np
from pyfcm import FCMNotification
push_service = FCMNotification(api_key=settings.GCM_API_KEY)

# create a view for displaying all orders of a particular batch


@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        data = request.data

        items_ordered = CartItem.objects.filter(RemovedFromCart=False, CartPhoneNo=data['CustomerPhoneNo'])
        # get active items

        tot = 0
        for an_item in items_ordered:  # change active items to inactive
            an_item.RemovedFromCart = True
            an_item.IsOrdered = True
            tot += an_item.SubTotal
            an_item.save()

        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            cid = serializer.save()
            curr = Order.objects.get(id=cid)

            for an_item in items_ordered:  # change order id of active items
                an_item.OrderId = curr
                an_item.save()

            concerned_cart = Cart.objects.get(UserPhone=data['CustomerPhoneNo'])
            concerned_cart.Total = 0.0
            concerned_cart.save()  # total of carts is 0 now

            # store total of active items in order object
            curr.Total = tot
            curr.save()
            """
            items_ordered = CartItem.objects.filter(OrderId = cid)

            locations = np.array(
                [(items_ordered.Item.RelatedStore.Latitude, item.Item.RelatedStore.Longitude) for item in items_ordered])
            lookup = np.array([item.id for item in items_ordered])
            """

            clusters = cluster_by_location(locations, lookup)

            for cluster in clusters:
                b = Batch()
                shoppers = find_shopper(cluster['c'])
                b.CentroidLatitude = cluster['c'][0]
                b.CentroidLongitude = cluster['c'][1]

                # these items have already got a batch
                for item_id in cluster['ids']:
                    item = CartItem.objects.filter(id=item_id)
                    item.BatchId = b.id
                    item.save()

                if shoppers:
                    b.TemporaryAvailable = True
                    b.TemporaryShopper = shoppers[0].PhoneNo
                    b.ShopperId = shoppers[0]

                elif len(shoppers) == 0:

                    other_shoppers = Shopper.objects.filter(IsOnline=True, Verified=True)

                    # To check if any other shopper available
                    if len(other_shoppers) == 0:
                        b.TemporaryAvailable = False
                        b.save()
                        return Response({'status': "No shopper found"}, status=200)

                    else:
                        b.TemporaryShopper = other_shoppers[0].PhoneNo
                        b.ShopperId = other_shoppers[0]
                        b.TemporaryAvailable = True

                b.save()

                # gcm notification
                registration_id = b.ShopperId.GcmId
                batch_data = BatchSerializer(b).data
                result = push_service.notify_single_device(registration_id=registration_id,
                                                            data_message=batch_data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def order_items(request, pk):
    try:
        part = Order.objects.get(id=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        allitems = CartItem.objects.filter(OrderId=pk)
        serializer = CartItemSerializer(allitems, many=True)
        return Response(serializer.data)


# To get product according to its pk
@api_view(['GET', 'PATCH', 'DELETE'])
def order_id(request, pk):
    try:
        part = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(part)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = OrderSerializer(part, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(part, request.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def user_orders(request, pk):
    if request.method == 'GET':
        g = Order.objects.filter(CustomerPhoneNo=pk)
        serializer = OrderSerializer(g, many=True)
        return Response(serializer.data)
























