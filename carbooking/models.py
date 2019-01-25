from django.db import models
from django.conf import settings
import datetime
from django.core.exceptions import ValidationError

# Create your models here.
class Car(models.Model):
    registration = models.CharField(max_length=10, unique=True)
    VIN = models.CharField(max_length=17, unique=True)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)


    def add(self):
        self.save()

    def __str__(self):
        return '%s %s %s' % (self.make, self.model, self.registration)

class Booking(models.Model):
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    start_time = models.TimeField(blank=False, null=True, verbose_name='start time')
    end_time = models.TimeField(blank=False, null=True, verbose_name='end time')
    start_date = models.DateField(blank=False, null=True, verbose_name='start date')
    end_date = models.DateField(blank=False, null=True, verbose_name='end date')

    class Meta:
        unique_together = ("driver", "car", "start_time", "end_time", "start_date", "end_date")


    def clean_startdate(self):
        if self.start_date < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        return self.start_date

    def __str__(self):
        return '%s %s %s' % (self.driver, self.start_time, self.end_time)
