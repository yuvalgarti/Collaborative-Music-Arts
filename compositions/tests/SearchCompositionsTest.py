from django.test import Client, TestCase
from django.contrib.auth.models import User
from compositions.models import Composition, Variation
from django.urls import reverse


class ShowVariationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            username="admin",
            password="adminadmin",
            email="admin@example.com")
        self.client.force_login(self.user)
        self.composition = Composition(name='compo')
        self.composition.save(user=self.user)
        self.composition2 = Composition(name='name')
        self.composition2.save(user=self.user)

    def test_search_compositions(self):
        self.assertEqual(Composition.objects.count(), 2)
        response = self.client.get(reverse('search_compositions'), data={'phrase': 'compo'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['compositions']), 1)
        self.assertEqual(response.context['compositions'][0].id, self.composition.id)
