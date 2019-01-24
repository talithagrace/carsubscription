from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_car/', views.add_car, name='add_car'),
    path('add_booking/', views.add_booking, name='add_booking'),
]
