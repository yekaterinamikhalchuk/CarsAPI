from rest_framework import serializers
from .models import Cars


class CarsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['id', 'vin', 'user']


class CarDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cars
        fields = '__all__'
