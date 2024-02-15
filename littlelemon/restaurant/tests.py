from django.test import TestCase
from restaurant.models import MenuModel
from restaurant.serializers import MenuSerializers
from rest_framework.test import APIClient
from rest_framework import status
import json
from django.test.client import RequestFactory
# Create your tests here.

class MenuItem(TestCase):
    menu_items = [
    {"title": "Pizza", "price": 9.99, "inventory": 20},
    {"title": "Burger", "price": 6.99, "inventory": 15},
    {"title": "Salad", "price": 5.99, "inventory": 10},
    {"title": "Pasta", "price": 12.99, "inventory": 25},
    {"title": "Sandwich", "price": 7.99, "inventory": 18}
]
    def setUp(self):
        [MenuModel.objects.create(title=data["title"],
                                  price=data["price"],
                                  inventory=data["inventory"]) for data in self.menu_items]
        client = APIClient()
        client.post('http://127.0.0.1:8000/auth/users/', data=json.dumps({"username":"hulio", "password":"qqqwwwGHD1233JMkb"}), content_type='application/json')

    # def test_get_item(self):
    #     item = MenuModel.objects.create(
    #         title="IceCream",
    #         price=5.00,
    #         inventory=100
    #     )
    #     item_str = str(item)
    #     self.assertEqual(item_str, "IceCream")
    #     self.assertEqual(MenuModel.objects.count(), 6)
        
    def test_get_all(self):
        client = APIClient()
        token = client.post("http://127.0.0.1:8000/api-token-auth/", data=json.dumps({"username":"hulio", "password":"qqqwwwGHD1233JMkb"}), content_type='application/json')
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.data["token"])
        response = client.get("http://127.0.0.1:8000/restaurant/menu", )
        request = RequestFactory().get('/')
        menu_items = MenuModel.objects.all()
        serializer = MenuSerializers(menu_items, many=True, context={'request': request})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        self.assertEqual(response.data, serializer.data)
        