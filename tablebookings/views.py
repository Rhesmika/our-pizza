from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from django.views import generic
from datetime import datetime
from .forms import NewBookingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, AccessMixin


# User Views
class UpcomingBookingsApproved(LoginRequiredMixin, generic.ListView):
    model = Booking
    today = datetime.today()
    queryset = Booking.objects.filter(booking_date__gte=today, status=1).order_by("booking_date")
    template_name = 'bookings.html'


class UpcomingBookingsPending(LoginRequiredMixin, generic.ListView):
    model = Booking
    today = datetime.today()
    queryset = Booking.objects.filter(booking_date__gte=today, status=0).order_by("booking_date")
    template_name = 'bookings_pending.html'


class NewBooking(LoginRequiredMixin, CreateView):
    form_class = NewBookingForm
    model = Booking
    success_url = '/bookings'
    template_name = 'booking_new.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class EditBooking(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = NewBookingForm
    success_url = '/bookings'
    template_name = 'booking_edit.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = 0
        self.object.save()
        return super().form_valid(form)


class DeleteBooking(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'booking_delete.html'
    success_url = '/bookings'


# Superuser Test
class SuperuserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin, AccessMixin):

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        redirect_url = '/bookings'
        if self.raise_exception:
            return redirect(redirect_url)
        return redirect(redirect_url)


# Admin views
class AllUpcomingBookings(SuperuserRequiredMixin, generic.ListView):
    model = Booking
    today = datetime.today()
    queryset = Booking.objects.filter(booking_date__gte=today).order_by("booking_date")
    template_name = 'bookings_admin.html'


class ApproveBooking(SuperuserRequiredMixin, UpdateView):
    model = Booking
    form_class = NewBookingForm
    success_url = '/bookings/admin-all'
    template_name = 'booking_admin_approve.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = 1
        self.object.save()
        return super().form_valid(form)


class CancelBooking(SuperuserRequiredMixin, DeleteView):
    model = Booking
    template_name = 'booking_admin_cancel.html'
    success_url = '/bookings/admin-all'


class UpdateBooking(SuperuserRequiredMixin, UpdateView):
    model = Booking
    form_class = NewBookingForm
    success_url = '/bookings/admin-all'
    template_name = 'booking_admin_update.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)
