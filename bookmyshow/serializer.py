from django.shortcuts import resolve_url
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import fields
from bookmyshow.models import Flight,Booking





class Validator(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['flight_number','departure_time','arrival_time']



class BookSerializer(serializers.ModelSerializer):
    flight = Validator()

    class Meta:
        model = Booking
        fields = ["flight" ,"booking_time"]
