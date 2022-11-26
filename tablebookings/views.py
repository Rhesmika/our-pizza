from django.shortcuts import render
from .models import Booking
from django.views import generic
from datetime import datetime


class UpcomingBookingsApproved(generic.ListView):
    model = Booking
    today = datetime.today()
    queryset = Booking.objects.filter(booking_date__gte=today).order_by("booking_date")
    template_name = 'bookings.html'