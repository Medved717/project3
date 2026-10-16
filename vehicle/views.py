from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView

from vehicle.models import Car, Moto, Mileage
from vehicle.serializers import CarSerializer, MotoSerializer, MileageSerializer, MotoMileageSerializer, \
    MotoCreateSerializer


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class MotoCreateAPIView(CreateAPIView):
    serializer_class = MotoCreateSerializer


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


class MotoMileageListAPIView(ListAPIView):
    queryset = Mileage.objects.filter(moto__isnull=False)
    serializer_class = MotoMileageSerializer

class MileageListAPIView(ListAPIView):
    queryset = Mileage.objects.all()
    serializer_class = MileageSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('car', 'moto')
    ordering_fields = ('year',)


