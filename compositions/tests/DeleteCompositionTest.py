from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from compositions.models import Composition


class DeleteCompositionTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            username="admin",
            password="adminadmin",
            email="admin@example.com")
        self.client.force_login(self.user)
        self.composition = Composition(name='compo')
        self.composition.save(user=self.user)

    def test_delete_composition(self):
        self.assertEqual(len(Composition.objects.all()), 1)
        response = self.client.get(reverse('delete_composition', kwargs={'composition_id': self.composition.id}))
        index_path = reverse('index')
        self.assertRedirects(response, index_path)
        response = self.client.get(index_path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Composition.objects.all()), 0)
