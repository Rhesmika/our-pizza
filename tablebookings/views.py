from django.shortcuts import render
from .models import Booking
from django.views import generic


class BookingsApproved(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter(status=1).order_by("booking_date")
    template_name = 'bookings.html'
    paginate_by = 5
