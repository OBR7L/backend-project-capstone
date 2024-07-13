from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="Pho", price=10, inventory=50)
        MenuItem.objects.create(title="Bun bo Hue", price=10, inventory=50)

    def test_getall(self):
        url = reverse('MenuItemView')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        menuItems = MenuItem.objects.all()
        menuItemsSerializer = MenuItemSerializer(menuItems, many=True)
        self.assertEqual(menuItemsSerializer.data, response.data)