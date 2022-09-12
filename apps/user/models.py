from django.db import models
from django.contrib.auth.models import User

# Create your models here.

PAYMENT_METHOD_CHOICES = (
    (1, 'cash'),
    (2, 'credit card'),
    (3, 'check')
)


class Account(models.Model):
    name = models.CharField(max_length=30)
    mailing_address = models.CharField(max_length=200)
    billing_address = models.CharField(max_length=200)
    star_points = models.FloatField(max_length=200, default=0)
    preferred_payment_method = models.IntegerField(choices=PAYMENT_METHOD_CHOICES, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
