from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Booking


@admin.register(Booking)
class bookingAdmin(ModelAdmin):
    list_display = ('author', 'reference', 'booking_date', 'party_of', 'status')
    search_fields = ('author', 'reference', 'booking_date', 'party_of', 'status')
    actions = ['pend_booking', 'approve_booking', 'deny_booking']

    def pend_booking(self, request, queryset):
        queryset.update(status=0)

    def approve_booking(self, request, queryset):
        queryset.update(status=1)

    def deny_booking(self, request, queryset):
        queryset.update(status=2)
