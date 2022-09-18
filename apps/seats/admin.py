from .models import Seat, Booking

from django.contrib import admin

# Register your models here.


@admin.register(Seat)
class SeatModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Booking)
class BookingModelAdmin(admin.ModelAdmin):
    pass
