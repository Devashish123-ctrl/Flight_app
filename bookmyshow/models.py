from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Flight(models.Model):
    flight_number = models.CharField(max_length=20, unique=True)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    total_seats = models.IntegerField(default=60)
    available_seats = models.IntegerField(default=60)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
 
