from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import BatchSerializer
from rest_framework.response import Response

from .models import Batch
from OrderBase.models import Order
from ShopperBase.models import Shopper
from OrderBase.serializers import OrderSerializer

from batch_maker import cluster_by_location, find_shopper
from pyfcm import FCMNotification

push_service = FCMNotification(api_key=settings.GCM_API_KEY)


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
        batch = Batch.objects.get(pk=pk)
    except Batch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BatchSerializer(batch)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = BatchSerializer(batch, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(batch, request.data)

            if batch.PermanentAvailable == True:
                # batch accepted by shopper
                pass
            elif batch.PermanentAvailable == False and batch.TemporaryAvailable == False:
                # batch rejected by shopper. Find new shopper

                items_ordered = CartItem.objects.filter(BatchId=pk)

                for cluster in clusters:
                    b = batch
                    # creating tuple of centroid
                    shoppers = find_shopper((b.CentroidLatitude, b.CentroidLongitude))

                    # these items have already got a batch

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

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def batch_id_orders(request, pk):
    try:
        part = Order.objects.filter(BatchId=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(part, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def shopper_batches(request, no):  # to get batches of a shopper

    try:
        who = Shopper.objects.get(PhoneNo=no)
    except Shopper.DoesNotExist:
        return Response(startus=status.HTTP_404_NOT_FOUND)

    allbatch = Batches.objects.filter(ShopperId=who.id)

    if request.method == 'GET':
        serializer = BatchesSerializer(allbatch, many=True)
        return response(serializer.data)






