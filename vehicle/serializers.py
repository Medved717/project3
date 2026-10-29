from rest_framework import serializers

from vehicle.models import Car, Moto, Mileage
from vehicle.validators import TitleValidator, MinMileageValidator, MaxYearValidator, CarMotoTogetherValidator


class MileageSerializer(serializers.ModelSerializer):
    mileage = serializers.IntegerField(min_value=0, validators=[MinMileageValidator()])
    year = serializers.IntegerField(min_value=0, validators=[MaxYearValidator()])

    class Meta:
        model = Mileage
        fields = ('car', 'moto', 'mileage', 'year')
        validators = [CarMotoTogetherValidator(car_field='car', moto_field='moto')]


class CarSerializer(serializers.ModelSerializer):
    last_mileage = serializers.IntegerField(source='mileage_set.all.first.mileage', read_only=True)
    mileage = MileageSerializer(source='mileage_set', many=True, read_only=True)

    class Meta:
        model = Car
        fields = '__all__'


class MotoSerializer(serializers.ModelSerializer):
    last_mileage = serializers.SerializerMethodField()

    def get_last_mileage(self, instance):
        if instance.mileage.all().first():
            return instance.mileage.all().first().mileage
        return 0

    class Meta:
        model = Moto
        fields = ('title', 'description', 'last_mileage')


class MotoMileageSerializer(serializers.ModelSerializer):
    moto = MotoSerializer()

    class Meta:
        model = Mileage
        fields = ('moto', 'mileage', 'year')


class MotoCreateSerializer(serializers.ModelSerializer):
    mileage = MileageSerializer(many=True)

    class Meta:
        model = Moto
        fields = '__all__'
        validators = [TitleValidator(field='title')]

    def create(self, validated_data):
        mileages = validated_data.pop('mileage')
        moto = Moto.objects.create(**validated_data)
        for mileage in mileages:
            Mileage.objects.create(moto=moto, **mileage)
        return moto
