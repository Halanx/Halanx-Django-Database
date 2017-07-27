from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import BatchSerializer
from rest_framework.response import Response

from .models import Batch
from OrderBase.models import Order
from ShopperBase.models import Shopper
from Carts.models import CartItem
from OrderBase.serializers import OrderSerializer
from BatchBase.serializers import BatchSerializer
from Halanx import settings

from pyfcm import FCMNotification
push_service = FCMNotification(api_key=settings.GCM_API_KEY)

from batch_maker import distance


# function to find nearest shoppers to a centroid
def find_shopper(centroid):
    shoppers = Shopper.objects.filter(IsOnline=True,Verified=True)
    sloc = [(s.id,distance(centroid, (s.Latitude, s.Longitude))) for s in shoppers]
    sloc = sorted(sloc, key = lambda x:x[1])
    return sloc


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
                items = CartItem.objects.get(BatchId = batch)
                shopper = batch.ShopperId

                # set of all users to notify
                users = []
                for item in items:
                    users.append(item.CartUser)
                users = set(users)

                # notify all users
                for user in users:
                    user_gcm_id = user.GcmId
                    result = push_service.notify_single_device(registration_id=user_gcm_id,
                                data_message = ShopperSerializer(shopper).data)
                
            elif batch.PermanentAvailable == False and batch.TemporaryAvailable == False:
                # batch rejected by shopper. Find new shopper

                shoppers = find_shopper((batch.CentroidLatitude, batch.CentroidLongitude))
                # removing current shopper who rejected batch
                shoppers = filter(lambda x:x[0]!=batch.ShopperId.id, shoppers)

                if shoppers:
                    batch.TemporaryAvailable = True
                    shopper = Shopper.objects.get(id = shoppers[0][0])
                    batch.TemporaryShopper = shopper.PhoneNo
                    batch.ShopperId = shopper

                elif len(shoppers) == 0:
                    batch.TemporaryAvailable = False
                    batch.save()
                    return Response({'status': "No shopper found"}, status=200)

                batch.save()

                # gcm notification
                registration_id = batch.ShopperId.GcmId
                result = push_service.notify_single_device(registration_id=registration_id,
                                                           data_message=BatchSerializer(batch))

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






