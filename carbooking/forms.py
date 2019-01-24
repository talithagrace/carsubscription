from django import forms
from .models import Car, Booking
from django.forms import widgets
from datetime import datetime
from datetime import timedelta

class DateInput(forms.DateTimeInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('make', 'model', 'registration', 'VIN')

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('driver', 'car', 'start_date', 'start_time', 'end_date', 'end_time')
        widgets = {
            'start_time': TimeInput(),
            'end_time': TimeInput(),
            'start_date': DateInput(),
            'end_date': DateInput()
        }
