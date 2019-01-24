from django.shortcuts import render
from .models import Car

# Create your views here.
def index(request):
    return render(request, 'carbooking/index.html', {})
