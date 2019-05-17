from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from .ReverseWithParams import my_reverse


class CreateModelsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            username="admin",
            password="adminadmin",
            email="admin@example.com")
        self.client.force_login(self.user)

    def test_create_composition(self):
        response = self.client.post(reverse('create_composition'), {'name': 'compo1'})
        show_composition_path = reverse('show_composition', kwargs={'composition_id': 1})
        self.assertRedirects(response, show_composition_path)
        response = self.client.get(show_composition_path)
        self.assertEqual(response.status_code, 200)
