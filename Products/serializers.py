from rest_framework import serializers
from .models import Product, ProductPhoto
from StoreBase.serializers import StoreSerializer


class ProductSerializer(serializers.ModelSerializer):

    # RelatedStore = StoreSerializer()

    class Meta:
        model = Product
        fields = '__all__'


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = '__all__'




