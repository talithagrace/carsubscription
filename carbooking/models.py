from django.db import models

# Create your models here.
class Car(models.Model):
    registration = models.CharField(max_length=10)
    VIN = models.CharField(max_length=17)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)

    def add(self):
        self.save()

    def __str__(self):
        return self.registration
