from rest_framework import serializers

from vehicle.models import Car, Moto, Mileage


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'

class MotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Moto
        fields = ('title', 'description')

class MileageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mileage
        fields = ('car', 'moto', 'mileage', 'year')