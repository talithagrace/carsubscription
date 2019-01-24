from django.test import TestCase
from carbooking.views import index
from django.test.client import Client
from django.template.loader import render_to_string
from carbooking.forms import BookingForm
from django.contrib.auth import login, authenticate

class ViewsTest(TestCase):
    c = Client()

    def test_index_template(self):
        resp = self.c.get('')
        with self.assertTemplateUsed('carbooking/index.html'):
            render_to_string('carbooking/index.html')

    def test_add_booking(self):
        login = self.c.login(username='testuser', password='secret')
        form = BookingForm()
        resp = self.c.post('/add_booking/', {'form': form})
        self.assertEqual(resp.status_code, 302)
        with self.assertTemplateUsed('carbooking/add_booking.html'):
            render_to_string('carbooking/add_booking.html')
