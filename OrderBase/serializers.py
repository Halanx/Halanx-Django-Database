
from rest_framework import serializers
from .models import Order
from Carts.serializers import CartItemSerializer1


class OrderSerializer(serializers.ModelSerializer):

    order_items = CartItemSerializer1(many=True, read_only=True)
    DeliveryDate = serializers.DateField(format="%d-%m-%Y")

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        obj = Order.objects.create(**validated_data)
        obj.save()
        return obj.id



