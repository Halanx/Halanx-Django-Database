from rest_framework import serializers
from .models import Cart, CartItem
from Products.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    # for POST as it needs only Item Id
    class Meta:
        model = CartItem
        fields = '__all__'


class CartItemSerializer1(serializers.ModelSerializer):
    # for get query
    Item = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = '__all__'






