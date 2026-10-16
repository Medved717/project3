from django.urls import path

from vehicle.apps import VehicleConfig
from rest_framework.routers import DefaultRouter

from vehicle.serializers import MotoMileageSerializer
from vehicle.views import CarViewSet, MotoCreateAPIView, MotoListAPIView, MotoRetrieveAPIView, MotoUpdateAPIView, \
    MotoDestroyAPIView, MileageCreateAPIView, MotoMileageListAPIView, MileageListAPIView

app_name = VehicleConfig.name

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')

urlpatterns = [
                  # Moto
                  path('moto_create/', MotoCreateAPIView.as_view(), name='moto_create'),
                  path('moto_list/', MotoListAPIView.as_view(), name='moto_list'),
                  path('moto_retrieve/<int:pk>/', MotoRetrieveAPIView.as_view(), name='moto_retrieve'),
                  path('moto_update/<int:pk>/', MotoUpdateAPIView.as_view(), name='moto_update'),
                  path('moto_delete/<int:pk>/', MotoDestroyAPIView.as_view(), name='moto_delete'),

                  # Mileage
                  path('mileage_create/', MileageCreateAPIView.as_view(), name='mileage_create'),
                  path('moto_mileage_list/', MotoMileageListAPIView.as_view(), name='moto_mileage_list'),
                  path('mileage_list/', MileageListAPIView.as_view(), name='mileage_list'),
              ] + router.urls
