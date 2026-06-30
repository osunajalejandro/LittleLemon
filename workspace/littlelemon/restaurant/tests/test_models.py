from django.test import TestCase
from ..models import Menu


class MenuTest(TestCase):
    def test_menu_str(self):
        item = Menu.objects.create(
            title="Pizza",
            price=9.99,
            inventory=10,
        )

        expected_value = "Pizza : 9.99"
        self.assertEqual(str(item), expected_value)