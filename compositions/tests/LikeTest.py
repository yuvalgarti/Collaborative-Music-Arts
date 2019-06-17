from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from compositions.models import Composition, Track
from compositions.models.RatingModel import Rate


class LikeTest(TestCase):
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_superuser(
            username="admin",
            password="adminadmin",
            email="admin@example.com")
        cls.client.force_login(cls.user)
        cls.composition = Composition(name='compo')
        cls.composition.save(user=cls.user)
        cls.track = Track()
        cls.track.save(user=cls.user, composition_id=cls.composition.id)

    def test_like_button_get(self):
        self.assertEqual(Rate.objects.filter(track_id=self.track.id).count(), 0)
        response = self.client.get(reverse('like_button', kwargs={'track_id': self.track.id}))
        self.assertRedirects(response, reverse('show_composition', kwargs={'composition_id': self.track.composition.id}))
        self.assertEqual(Rate.objects.filter(track_id=self.track.id).count(), 1)

    def test_unlike(self):
        Rate(user=self.user, track=self.track).save()
        self.assertEqual(Rate.objects.filter(track_id=self.track.id).count(), 1)
        response = self.client.get(reverse('like_button', kwargs={'track_id': self.track.id}))
        self.assertRedirects(response, reverse('show_composition', kwargs={'composition_id': self.track.composition.id}))
        self.assertEqual(Rate.objects.filter(track_id=self.track.id).count(), 0)
