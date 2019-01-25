from django.contrib.auth.models import User
from django.test import TestCase
from carbooking.models import Car, Booking
from django.utils import timezone
from django.core.exceptions import ValidationError

class BookingModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        my_car = Car.objects.create(registration='BD45 H66', VIN='12345678999', make='ford', model='focus')
        my_user = User.objects.create_user(username='testgrace', email='testgrace@grace.com', password='secret')
        booking_1 = Booking.objects.create(driver=my_user, car=my_car, start_time='00:00:00', start_date='2018-10-10', end_time='00:00:00', end_date='2019-11-10')

    def test_future_date_validation(self):
        booking = Booking.objects.get(id=1)
        self.assertRaises(ValidationError, booking.clean_startdate)

    def test_overlaps_validation(self):
        user = User.objects.get(id=1)
        car = Car.objects.get(id=1)
        booking = Booking.objects.create(driver=user, car=car, start_time='00:00:00', start_date='2018-10-20', end_time='00:00:00', end_date='2019-11-10')
        self.assertRaises(ValidationError, booking.clean_overlaps)
