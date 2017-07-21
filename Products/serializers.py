from rest_framework import serializers
from .models import Product, ProductPhoto
from StoreBase.serializers import StoreSerializer, StoreSerializer1


class ProductSerializer(serializers.ModelSerializer):

    RelatedStore = StoreSerializer1(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductPhoto
        fields = '__all__'











