from rest_framework import serializers

from vehicle.models import Car, Moto, Mileage


class CarSerializer(serializers.ModelSerializer):
    last_mileage = serializers.IntegerField(source='mileage_set.all().first().mileage')

    class Meta:
        model = Car
        fields = '__all__'


class MotoSerializer(serializers.ModelSerializer):
    last_mileage = serializers.SerializerMethodField()

    def get_last_mileage(self, instance):
        if instance.mileage_set.all().first():
            return instance.mileage_set.all().first().mileage
        return 0

    class Meta:
        model = Moto
        fields = ('title', 'description', 'last_mileage')


class MileageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mileage
        fields = ('car', 'moto', 'mileage', 'year')
