from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


REQUEST_STATUS = ((0, 'Pending'), (1, 'Approved'), (2, 'Denied'))


class Booking(models.Model):
    name = "User"
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    reference = models.CharField(max_length=50)
    booking_date = models.DateField()
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
