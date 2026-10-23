from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from vehicle.models import Car


class VehicleTestCreate(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="Test@test.ru")
        self.client.force_authenticate(user=self.user)
        self.car = Car.objects.create(title="Лада Седан 1", description="Баклажан 1", owner=self.user)

    def test_create_car(self):
        data = {
            "title": "Лада Седан",
            "description": "Баклажан"
        }

        response = self.client.post("/cars/", data=data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 4)
        self.assertEqual(Car.objects.count(), 2)
        self.assertEqual(response.data.get("title"), "Лада Седан")
        self.assertEqual(response.data.get("title"),"Лада Седан")

    def test_list_cars(self):

        response = self.client.get("/cars/")

        self.assertEqual(len(response.data), 1)
