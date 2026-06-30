from django.test import TestCase
from django.urls import reverse
from ..models import Menu
from ..serializers import MenuSerializer


class MenuViewTest(TestCase):

    def setUp(self):
        # create test data
        self.item1 = Menu.objects.create(title="Pizza", price=9.99, inventory=10)
        self.item2 = Menu.objects.create(title="Pasta", price=12.99, inventory=5)
        self.item3 = Menu.objects.create(title="Salad", price=6.99, inventory=8)

    def test_getall(self):
        # get API response
        response = self.client.get(reverse('menu'))

        # get data from DB
        menus = Menu.objects.all()

        # serialize DB data
        serializer = MenuSerializer(menus, many=True)

        # compare response vs serializer
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)