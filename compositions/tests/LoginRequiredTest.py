from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from django.utils.http import urlencode

from compositions.models import Composition


def my_reverse(viewname, kwargs=None, query_kwargs=None):
    """
    Custom reverse to add a query string after the url
    Example usage:
    url = my_reverse('my_test_url', kwargs={'pk': object.id}, query_kwargs={'next': reverse('home')})
    """
    url = reverse(viewname, kwargs=kwargs)

    if query_kwargs:
        return (u'%s?%s' % (url, urlencode(query_kwargs))).replace('%2F', '/')

    return url


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


