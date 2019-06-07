from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.test import Client, TestCase
from django.urls import reverse

from compositions.models import Composition, Track
from .ReverseWithParams import my_reverse


class CreateModelsTest(TestCase):
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_superuser(
            username="admin",
            password="adminadmin",
            email="admin@example.com")
        cls.client.force_login(cls.user)
        cls.composition = Composition(name='compo')
        cls.composition.save(user=cls.user)

    def test_create_composition_get(self):
        response = self.client.get(reverse('create_composition'))
        self.assertEqual(response.status_code, 200)

    def test_create_composition_post(self):
        response = self.client.post(reverse('create_composition'), {'name': 'compo1'})
        created_compo = Composition.objects.filter(name='compo1')[0]
        show_composition_path = reverse('show_composition', kwargs={'composition_id': created_compo.id})
        self.assertRedirects(response, show_composition_path)
        response = self.client.get(show_composition_path)
        self.assertEqual(response.status_code, 200)

    def test_create_track_get(self):
        response = self.client.get(reverse('create_track', kwargs={'composition_id': self.composition.id}))
        self.assertEqual(response.status_code, 200)

    def test_create_track_post(self):
        response = self.client.post(reverse('create_track', kwargs={'composition_id': self.composition.id}),
                                    {'instrument': 'guitar', 'track_file': './static/guitar.wav'})
        self.assertEqual(response.status_code, 200)

    def test_create_variation_post(self):
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
