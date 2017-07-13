

from .models import Cart
from .models import CartItem
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from .serializers import CartSerializer
from .serializers import CartItemSerializer, CartItemSerializer1
from django.core import serializers
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def cart_list(request):

    if request.method == 'GET':

        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# To get product according to its pk
@api_view(['GET', 'PATCH', 'DELETE'])
def cart_id(request, no):

    try:
        part = Cart.objects.get(UserPhone=no)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = CartSerializer(part)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = BatchesSerializer(part, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(part, request.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def item_list(request):

    if request.method == 'GET':
        items = CartItem.objects.all()
        serializer = CartItemSerializer1(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def item_id(request, pk):

    try:
        part = CartItem.objects.get(pk=pk)
    except CartItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CartItemSerializer1(part)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = CartItemSerializer1(part, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(part, request.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def cart_itemlist(request, pk):

    try:

        g = Cart.objects.get(UserPhone=pk)
        allitems = g.carts.all()

    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CartItemSerializer1(allitems, many=True)
        return Response(serializer.data)

    # no need of POST here
    if request.method == 'POST':
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # error : 'Cart' object has no attribute 'user_set'
        # allitems = g.cartitem_set.all()     # error : no attribute named 'Cart'
        # filter is used in case of many possible results

    """
    if request.method == 'GET':

        abc = serializers.serialize('json', allitems)
        # serializer = CartItemSerializer(allitems)
        # return JsonResponse(allitems, safe=False)
        return HttpResponse(abc, content_type="application/json")

    """


@api_view(['GET'])
def cart_itemlist_active(request, pk):

    try:
        g = Cart.objects.get(UserPhone=pk)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        allitems = CartItem.objects.filter(CartPhoneNo=pk, RemovedFromCart=False)
        serializer = CartItemSerializer1(allitems, many=True)
        return Response(serializer.data)





