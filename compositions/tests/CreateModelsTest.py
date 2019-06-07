from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.test import Client, TestCase
from django.urls import reverse

from compositions.models import Composition, Track
from .ReverseWithParams import my_reverse


class CreateModelsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            username="admin",
            password="adminadmin",
            email="admin@example.com")
        self.client.force_login(self.user)



"""
    # Migration error
    def test_create_variation(self):
        compo = Composition()
        compo.save(user=self.user)
        track = Track()
        track.save(user=self.user, composition_id=compo.id)
        show_variation_path = reverse('show_variation', kwargs={'variation_id': 1})
        response = self.client.post(reverse('create_variation', kwargs={'composition_id': compo.id}),
                                    {'name': 'vari1', 'tracks': [str(track.id)]})
        self.assertRedirects(response, show_variation_path)
        response = self.client.get(show_variation_path)
        self.assertEqual(response.status_code, 200)
"""
