from factory.fuzzy import FuzzyInteger

from django.core.urlresolvers import reverse
from django.test import TestCase


class PricesSerializerTest(TestCase):

    def setUp(self):
        self.form = dict(one=12, second=3)
        self.form_2 = dict(one="asd", second=3)

    def test_view(self):
        one = FuzzyInteger(0,50).fuzz()
        second = FuzzyInteger(0,50).fuzz()
        form = dict(one=one, second=second)
        response = self.client.post(
            reverse('x'),
            data=form)
        self.assertEqual(one*second, response.context['data'])

    def test_view_incorrect(self):
        response = self.client.post(
            reverse('x'),
            data=self.form_2)
        self.assertEqual("error11   ", response.context['data'])

    def test_view_200(self):
        response = self.client.post(
            reverse('x'),
            data=self.form_2)
        self.assertEqual(200, response.status_code)