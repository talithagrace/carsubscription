from django.urls import path
from . import carbooking_views

urlpatterns = [
    path('', carbooking_views.index, name='index'),
    path('add_car/', carbooking_views.add_car, name='add_car'),
    path('add_booking/', carbooking_views.add_booking, name='add_booking'),
    path('signup/', carbooking_views.SignUp.as_view(), name='signup'),
]
