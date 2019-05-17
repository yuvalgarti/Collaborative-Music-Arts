from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from .ReverseWithParams import my_reverse

from compositions.models import Composition


class LoginRequiredTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_required(self, view_name=None, kwargs=None):
        if view_name:
            reversed_url = reverse(view_name, kwargs=kwargs)
            response = self.client.get(reversed_url)
            self.assertRedirects(response, my_reverse('login', query_kwargs={'next': reversed_url}))

    def test_login_required_create_composition(self):
        self.test_login_required(view_name='create_composition')

    def test_login_required_create_variation(self):
        compo = Composition()
        user = User()
        user.save()
        compo.save(user=user)

        self.test_login_required(view_name='create_variation', kwargs={'composition_id': compo.id})

    def test_login_required_create_track(self):
        compo = Composition()
        user = User()
        user.save()
        compo.save(user=user)
        self.test_login_required(view_name='create_track', kwargs={'composition_id': compo.id})

