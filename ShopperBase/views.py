

from .models import Shopper, Documents, ShopperImage
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ShopperSerializer, DocumentSerializer, ShopperImageSerializer
from rest_framework.response import Response
from BatchBase.models import Batch
from BatchBase.serializers import BatchSerializer

import boto3
import base64
import json


@api_view(['GET'])
def get_shopper_batches(request, no):
    shopper = Shopper.objects.get(PhoneNo = no)
    batches = Batch.objects.filter(ShopperId = shopper)
    serializer = BatchSerializer(batches, many= True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def shopper_list(request):

    if request.method == 'GET':
        shoppers = Shopper.objects.all()
        serializer = ShopperSerializer(shoppers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ShopperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# To get product according to its pk
@api_view(['GET', 'PATCH', 'DELETE'])
def shopper_id(request, no):

    try:
        part = Shopper.objects.get(PhoneNo=no)
    except Shopper.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ShopperSerializer(part)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = ShopperSerializer(part, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(part, request.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'DELETE'])
def get_documents(request, who):

    try:
        document = Documents.objects.get(ShopperPhoneNo=who)
    except Documents.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DocumentSerializer(document)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def post_documents(request):

    if request.method == 'GET':
        docs = Documents.objects.all()
        serializer = DocumentSerializer(docs, many=True)
        return Response(serializer.data)

    if request.method == 'POST':

        data = request.data

        if data['AadharImage'] is not None:

            filename = '%s/Aadhar.jpeg' % data['ShopperPhoneNo']
            client = boto3.client('s3')
            img1 = base64.b64decode(data['AadharImage'])
            client.put_object(Bucket='halanx-shopper-documents',
                              ACL='public-read',
                              Key=filename, ContentType='jpeg',
                              Body=img1)

        if data['LicenseImage'] is not None:

            filename = '%s/License.jpeg' % data['ShopperPhoneNo']
            client = boto3.client('s3')
            img2 = base64.b64decode(data['LicenseImage'])
            client.put_object(Bucket='halanx-shopper-documents',
                              ACL='public-read',
                              Key=filename, ContentType='jpeg',
                              Body=img2)

        if data['VehicleRCImage'] is not None:

            filename = '%s/Vehicle-RC.jpeg' % data['ShopperPhoneNo']
            client = boto3.client('s3')
            img3 = base64.b64decode(data['VehicleRCImage'])
            client.put_object(Bucket='halanx-shopper-documents',
                              ACL='public-read',
                              Key=filename, ContentType='jpeg',
                              Body=img3)

        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            g = Documents.objects.get(ShopperPhoneNo=data['ShopperPhoneNo'])

            if g.AadharImage is not None:
                filename = '%s/Aadhar.jpeg' % g.ShopperPhoneNo
                g.AadharURL = 'https://s3-us-west-2.amazonaws.com/halanx-shopper-documents/' + filename
                g.AadharImage = None

            if g.LicenseImage is not None:

                filename = '%s/License.jpeg' % g.ShopperPhoneNo
                g.LicenseURL = 'https://s3-us-west-2.amazonaws.com/halanx-shopper-documents/' + filename
                g.LicenseImage = None

            if g.VehicleRCImage is not None:
                filename = '%s/Vehicle-RC.jpeg' % g.ShopperPhoneNo
                g.VehicleRCURL = 'https://s3-us-west-2.amazonaws.com/halanx-shopper-documents/' + filename
                g.VehicleRCImage = None

            g.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def upload_image(request, pk):

    part = Shopper.objects.get(PhoneNo=pk)

    if request.method == 'POST':

        data = request.data

        if data['DisplayPicture'] is not None:
            filename = '%s/DisplayPicture.jpeg' % data['ShopperPhoneNo']
            client = boto3.client('s3')
            img1 = base64.b64decode(data['DisplayPicture'])
            client.put_object(Bucket='halanx-shopper-documents',
                              ACL='public-read',
                              Key=filename, ContentType='jpeg',
                              Body=img1)

            part.DisplayPictureURL = 'https://s3-us-west-2.amazonaws.com/halanx-shopper-documents/' + filename
            part.save()

        serializer = ShopperImageSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()

            g = ShopperImage.objects.get(ShopperPhoneNo=data['ShopperPhoneNo'])

            if g.DisplayPicture is not None:
                g.DisplayPicture = None
                g.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






































