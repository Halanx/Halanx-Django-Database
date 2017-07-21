from rest_framework import serializers
from .models import Batch
from Carts.serializers import CartItemSerializer2


class BatchSerializer(serializers.ModelSerializer):

    batch_items = CartItemSerializer2(many=True, read_only=True)

    class Meta:
        model = Batch
        fields = '__all__'








