from django.core.urlresolvers import reverse
from django.test import TestCase


class PricesSerializerTest(TestCase):

    def setUp(self):
        self.form = dict(one=12, second=3)

    def test_view(self):
        response = self.client.post(
            reverse('x'),
            data=self.form)
        print response.context['data']