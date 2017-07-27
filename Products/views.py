
from .models import Product
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ProductSerializer, ProductPhotoSerializer
from rest_framework.response import Response
from .models import ProductPhoto
from StoreBase.models import Store

import json
import base64
import boto3

@api_view(['GET', 'POST'])
def product_list(request):

    if request.method == 'GET':

        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# To get product according to its pk
@api_view(['GET', 'PATCH', 'DELETE'])
def product_id(request, pk):

    try:
        part = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(part)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = ProductSerializer(part, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(part, request.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def upload_photo(request, pk):

    part = Product.objects.get(id=pk)

    if request.method == 'POST':

        data = request.data

        if data['ProductString'] is not None:

            filename = '%s.jpeg' % data['ProductId']
            client = boto3.client('s3')
            img1 = data['ProductString']

            client.put_object(Bucket='halanx-products',
                              ACL='public-read',
                              Key=filename, ContentType='image/jpeg',
                              Body=img1)

            part.ProductImage = 'https://s3-us-west-2.amazonaws.com/halanx-products/' + filename
            part.save()

        serializer = ProductPhotoSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()

            g = ProductPhoto.objects.get(ProductId=data['ProductId'])

            if g.ProductString is not None:
                g.ProductString = None
                g.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


















