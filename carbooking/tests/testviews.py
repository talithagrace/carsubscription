from django.test import TestCase
from carbooking.carbooking_views import index
from django.test.client import Client
from django.template.loader import render_to_string
from carbooking.forms import BookingForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from carbooking.models import Car, Booking

class ViewsTest(TestCase):
    c = Client()
    @classmethod
    def setUpTestData(cls):
        cls.my_car = Car.objects.create(registration='BD45 H66', VIN='12345678999', make='ford', model='focus')
        cls.my_user = User.objects.create_user(username='testgrace', email='testgrace@grace.com', password='secret')
        cls.booking_1 = Booking.objects.create(driver=cls.my_user, car=cls.my_car, start_time='00:00:00', start_date='2019-10-10', end_time='00:00:00', end_date='2019-11-10')
        cls.c.login

    def test_index_template(self):
        resp = self.c.get('')
        with self.assertTemplateUsed('carbooking/index.html'):
            render_to_string('carbooking/index.html')
        self.assertEqual(resp.status_code, 200)

    def test_add_booking(self):
        login = self.c.login(username='testuser', password='secret')
        form = BookingForm()
        resp = self.c.post('/add_booking/', {'form': form})
        self.assertEqual(resp.status_code, 302)
        with self.assertTemplateUsed('carbooking/add_booking.html'):
            render_to_string('carbooking/add_booking.html')

    def test_booking_form_valid(self):
        car = Car.objects.create(registration='BD45 H67', VIN='12345678599', make='ford', model='focus')
        user = User.objects.create_user(username='testgrace1', email='testgrace@grace.com', password='secret')
        form = BookingForm(data={'driver':user, 'car': car, 'start_time':'00:00', 'start_date':'2019-10-10', 'end_time':'00:00', 'end_date':'2019-11-10'})
        self.assertTrue(form.is_valid())

    def test_get_add_booking(self):
        resp = self.c.get('/add_booking/')
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, '/accounts/login/?next=/add_booking/')

    def test_booking_invalid_view(self):
        self.c.login()
        resp = self.c.post('/add_booking/', {'driver':"user", 'car': "car", 'start_time':'00:00:00', 'start_date':'2019-10-10', 'end_time':'00:00:00', 'end_date':'2019-11-10'})
        self.assertEqual(resp.status_code, 302)
        with self.assertTemplateUsed('carbooking/add_booking.html'):
            render_to_string('carbooking/add_booking.html')
