
from rest_framework import serializers
from .models import Store, Logo


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = '__all__'


class LogoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Logo
        fields = '__all__'









