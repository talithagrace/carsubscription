from django.test import TestCase
from carbooking.views import index
from django.test.client import Client
from django.template.loader import render_to_string

class IndexTest(TestCase):
    c = Client()

    def test_template(self):
        resp = self.c.get('')
        with self.assertTemplateUsed('carbooking/index.html'):
            render_to_string('carbooking/index.html')
