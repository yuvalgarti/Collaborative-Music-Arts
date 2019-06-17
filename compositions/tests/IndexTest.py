from django.test import Client, TestCase
from django.urls import reverse


class IndexTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['compositions']), 0)
