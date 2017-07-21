
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


class StoreSerializer1(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ['id', 'StoreName', 'Latitude', 'Longitude', 'StoreLogo']





