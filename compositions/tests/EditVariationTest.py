from django.test import Client, TestCase
from django.contrib.auth.models import User
from compositions.models import Composition, Variation
from django.urls import reverse


class EditVariationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            username="admin",
            password="adminadmin",
            email="admin@example.com")
        self.client.force_login(self.user)
        self.composition = Composition(name='compo')
        self.composition.save(user=self.user)
        self.variation = Variation(name='my_variation')
        self.variation.save(user=self.user, composition_id=self.composition.id)

    def test_edit_variation_get(self):
        response = self.client.get(reverse('edit_variation', kwargs={'variation_id': self.variation.id}))
        self.assertEqual(response.status_code, 200)
