from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from compositions.models import Composition


class CompositionTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            username="admin",
            password="adminadmin",
            email="admin@example.com")
        self.client.force_login(self.user)


