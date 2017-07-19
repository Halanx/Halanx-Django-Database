from rest_framework import serializers
from .models import Product, ProductPhoto
from StoreBase.serializers import StoreSerializer, StoreSerializer1


class ProductSerializer(serializers.ModelSerializer):

    RelatedStore = StoreSerializer1()

    class Meta:
        model = Product
        fields = '__all__'


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = '__all__'




