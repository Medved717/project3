from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView

from vehicle.models import Car, Moto, Mileage
from vehicle.serializers import CarSerializer, MotoSerializer, MileageSerializer


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

class MotoCreateAPIView(CreateAPIView):
    serializer_class = MotoSerializer

class MotoListAPIView(ListAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer

class MotoUpdateAPIView(UpdateAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer

class MotoDestroyAPIView(DestroyAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer

class MotoRetrieveAPIView(RetrieveAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer

class MileageCreateAPIView(CreateAPIView):
    serializer_class = MileageSerializer