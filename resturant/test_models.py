from django.test import TestCase
from resturant.models import MenuItem 

class MenuItemModelTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(
            title="Test Item",
            price=9.99,
            inventory=5
        )
        fetched_item = MenuItem.objects.get(id=item.id)
        self.assertEqual(fetched_item.title, "Test Item")
        self.assertEqual(fetched_item.price, 9.99)
        self.assertEqual(fetched_item.inventory, 5)