from rest_framework import serializers
from .models import Cart, CartItem
from Products.serializers import ProductSerializer
from UserBase.serializers import UserSerializer
from OrderBase.models import Order


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'


# To receive CartItem from frontend
class CartItemSerializer(serializers.ModelSerializer):
    # for POST as it needs only Item Id
    class Meta:
        model = CartItem
        fields = '__all__'


# To display cartitem while serializing orders
class CartItemSerializer1(serializers.ModelSerializer):
    # for get query
    CartUser = UserSerializer(read_only=True)
    Item = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = '__all__'


# to display cartitems while serializing Batches
class CartItemSerializer2(serializers.ModelSerializer):

    # info of order while displaying cartitems in batches
    class OrderSerializer1(serializers.ModelSerializer):
        class Meta:
            model = Order
            fields = ['id', 'Latitude', 'Longitude', 'DeliveryAddress']

    CartUser = UserSerializer(read_only=True)
    Item = ProductSerializer(read_only=True)
    OrderId = OrderSerializer1(read_only=True)

    class Meta:
        model = CartItem
        fields = '__all__'




