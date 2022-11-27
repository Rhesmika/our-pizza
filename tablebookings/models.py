from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from django.urls import reverse


REQUEST_STATUS = ((0, 'Pending'), (1, 'Approved'), (2, 'Edited'), (3, 'Denied'))


class Booking(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    reference = models.CharField(max_length=50)
    booking_date = models.DateField()
    booking_time = models.TimeField(default=datetime.time(19, 00))
    party_of = models.IntegerField(
        default=2,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
     )
    status = models.IntegerField(choices=REQUEST_STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
