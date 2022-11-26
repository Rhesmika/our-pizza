from django.shortcuts import render, redirect
from .models import Booking
from django.views import generic
from datetime import datetime
from .forms import NewBookingForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User


class UpcomingBookingsApproved(generic.ListView):
    model = Booking
    today = datetime.today()
    queryset = Booking.objects.filter(booking_date__gte=today, status=1).order_by("booking_date")
    template_name = 'bookings.html'


class NewBooking(CreateView):
    form_class = NewBookingForm
    model = Booking
    success_url = 'my-bookings'
    template_name = 'bookings-new.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.status = 0
        self.object.save()
        return super().form_valid(form)
