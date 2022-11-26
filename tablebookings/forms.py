from .models import Booking
from django import forms


class NewBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('booking_date', 'booking_time', 'party_of', 'reference',)