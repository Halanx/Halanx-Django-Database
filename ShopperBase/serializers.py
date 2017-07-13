from rest_framework import serializers
from .models import Shopper, Documents, ShopperImage


class ShopperSerializer(serializers.ModelSerializer):
    AvailableDate = serializers.DateField(format="%d-%m-%Y")

    class Meta:
        model = Shopper
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Documents
        fields = '__all__'


class ShopperImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShopperImage
        fields = '__all__'

