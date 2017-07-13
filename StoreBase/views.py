
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import StoreSerializer, LogoSerializer
from .models import Store, Logo
from Products.models import Product
from Products.serializers import ProductSerializer

import boto3
import base64


# list of all stores
@api_view(['GET', 'POST'])
def store_list(request):

    if request.method == 'GET':
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# To get product according to its pk
@api_view(['GET', 'PATCH', 'DELETE'])    # localhost:8000/stores/pk
def store_id(request, pk):

    try:
        part = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StoreSerializer(part)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = StoreSerializer(part, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(part, request.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def upload_logo(request, pk):
    part = Store.objects.get(id=pk)

    if request.method == 'POST':

        data = request.data

        if data['StoreLogoImage'] is not None:
            filename = '%s.jpeg' % data['StoreId']
            client = boto3.client('s3')
            img1 = base64.b64decode(data['StoreLogoImage'])
            client.put_object(Bucket='halanx-stores-logo',
                              ACL='public-read',
                              Key=filename, ContentType='jpeg',
                              Body=img1)

            part.StoreLogo = 'https://s3-us-west-2.amazonaws.com/halanx-stores-logo/' + filename
            part.save()

        serializer = LogoSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()

            g = Logo.objects.get(StoreId=data['StoreId'])

            if g.StoreLogoImage is not None:
                g.StoreLogoImage = None
                g.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def store_products(request, store):

    try:
        part = Product.objects.filter(StoreId=store)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(part, many=True)
        return Response(serializer.data)


"""
# to get products in a particular store
# this is wrong, lol
@api_view(['GET', 'PUT', 'DELETE'])     # localhost:8000/stores/pk/products
def store_products(request, pk):

    try:
        part = Product.objects.get(Store=pk)   # error
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(part, many=True)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    # not needed put query
    '''
    elif request.method == 'PUT':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    '''



"""









