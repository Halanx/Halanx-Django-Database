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

from pyfcm import FCMNotification
push_service = FCMNotification(api_key=settings.GCM_API_KEY)

from batch_maker import distance, cluster_by_location
import numpy as np


# function to find nearest shoppers to a centroid
def find_shopper(centroid):
    shoppers = Shopper.objects.filter(IsOnline=True,Verified=True)
    sloc = [(s.id,distance(centroid, (s.Latitude, s.Longitude))) for s in shoppers]
    sloc = sorted(sloc, key = lambda x:x[1])
    return sloc



@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        data = request.data

        # get active items
        items_ordered = CartItem.objects.filter(RemovedFromCart=False, CartPhoneNo=data['CustomerPhoneNo'])

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

            # location of stores
            locations = np.array([(item.Item.RelatedStore.Latitude, item.Item.RelatedStore.Longitude) 
                for item in items_ordered])
            lookup = np.array([item.id for item in items_ordered])

            clusters = cluster_by_location(locations, lookup)

            for cluster in clusters:
                b = Batch()
                b.CentroidLatitude = cluster['c'][0]
                b.CentroidLongitude = cluster['c'][1]

                shoppers = find_shopper(cluster['c'])

                if shoppers:
                    shopper = Shopper.objects.get(id = shoppers[0][0])
                    b.TemporaryShopper = shopper.PhoneNo
                    b.TemporaryAvailable = True
                    b.ShopperId = shopper

                elif len(shoppers) == 0:
                    b.TemporaryAvailable = False
                    b.save()
                    return Response({'status': "No shopper found"}, status=200)
                
                b.save()
                
                # add items to batch
                for item_id in cluster['ids']:
                    item = CartItem.objects.get(id=item_id)
                    item.BatchId = b
                    item.save()


                # gcm notification
                registration_id = b.ShopperId.GcmId
                result = push_service.notify_single_device(registration_id=registration_id,
                                                           data_message=BatchSerializer(b).data)
                
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
























