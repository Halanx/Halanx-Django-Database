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
from Carts.serializers import CartItemSerializer
import requests


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

            order_items = CartItem.objects.filter(OrderId=curr)
            online_shoppers = Shopper.objects.filter(IsOnline=True, Verified=True)

            b = Batch()

            b.OrderId = curr

            if len(online_shoppers) == 0:
                b.TemporaryAvailable = False
                b.save()
                return Response({'status': "No shopper found"}, status=200)

            b.ShopperId = online_shoppers[0]
            b.TemporaryShopper = online_shoppers[0].PhoneNo
            b.TemporaryAvailable = True
            b.save()

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
























