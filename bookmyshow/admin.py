# admin.py
from django.contrib import admin
from .models import Flight, Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'flight', 'booking_time')
    list_filter = ('flight__flight_number', 'booking_time')

    def flight_number(self, obj):
        return obj.flight.flight_number
    flight_number.admin_order_field = 'flight__flight_number'  # Allows column order sorting
    flight_number.short_description = 'Flight Number'  # Renames column head

admin.site.register(Flight)
admin.site.register(Booking, BookingAdmin)
