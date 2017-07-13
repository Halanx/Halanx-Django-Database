

from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import BatchSerializer
from rest_framework.response import Response

from .models import Batch
from OrderBase.models import Order
from ShopperBase.models import Shopper
from OrderBase.serializers import OrderSerializer


@api_view(['GET', 'POST'])
def batch_list(request):

    if request.method == 'GET':
        batches = Batch.objects.all()
        serializer = BatchSerializer(batches, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# To get product according to its pk
@api_view(['GET', 'PATCH', 'DELETE'])
def batch_id(request, pk):

    try:
        part = Batch.objects.get(pk=pk)
    except Batch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BatchSerializer(part)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = BatchSerializer(part, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(part, request.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def batch_id_orders(request, pk):

    # returns json of all orders which have his particular batch number
    # now to retrieve items, you can go to Order.Items and call itemslist_id for all orders

    try:
        part = Order.objects.filter(BatchId=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(part, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def shopper_batches(request, no):    # to get batches of a shopper

    try:
        who = Shopper.objects.get(PhoneNo=no)
    except Shopper.DoesNotExist:
        return Response(startus=status.HTTP_404_NOT_FOUND)

    allbatch = Batches.objects.filter(ShopperId=who.id)

    if request.method == 'GET':
        serializer = BatchesSerializer(allbatch, many=True)
        return response(serializer.data)






