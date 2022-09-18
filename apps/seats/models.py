import datetime

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.utils.timezone import now

# Create your models here.


SEAT_NUMBER_CHOICES = (
    (2, 'two seats'),
    (4, 'four seats'),
    (6, 'six seats'),
    (6, 'eight seats')
)


PAYMENT_METHOD_CHOICES = (
    (1, 'cash'),
    (2, 'credit card'),
    (3, 'check')
)


class Seat(models.Model):
    number = models.IntegerField(choices=SEAT_NUMBER_CHOICES)

    def is_available(self, time):
        time_range = (time - datetime.timedelta(hours=1), time + datetime.timedelta(hours=1))
        return self.booking_set.all().filter(datetime__range=time_range)


class Booking(models.Model):
    datetime = models.DateTimeField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    preferred_payment_method = models.IntegerField(choices=PAYMENT_METHOD_CHOICES, null=True, blank=True)
    people_number = models.IntegerField(validators=(MaxValueValidator(14),))
    seats = models.ManyToManyField(Seat)  # 可以查这张桌子被哪些用户使用过


"""
time
9 10 11

id
1 2 5 6
numbers
2 4 6 8

7

Booking
    ...
    seats
        5,1
"""
