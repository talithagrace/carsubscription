from django.shortcuts import render, redirect
from .models import Car, Booking
from .forms import AddCarForm, BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
def index(request):
    return render(request, 'carbooking/index.html', {})

@login_required
def add_car(request):
    if request.method == "POST":
        form = AddCarForm(request.POST)
        if form.is_valid():
            car_added = form.save(commit=False)
            car_added.user = request.user
            car_added.save()
            cars = Car.objects.all().order_by('registration')
            form = AddCarForm()
            context = {
                'cars': cars,
                'form': form
            }
            return render(request, 'carbooking/add_car.html', context)
    else:
        form = AddCarForm()
    return render(request, 'carbooking/add_car.html', {'form': form})

@login_required
def add_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            bookings = Booking.objects.all().order_by('start_time')
            form = BookingForm()
            context = {
                'bookings': bookings,
                'form': form
            }
            return render(request, 'carbooking/success.html', context)
    else:
        form = BookingForm()
    return render(request, 'carbooking/add_booking.html', {'form': form})


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
