from . import views
from django.urls import path


urlpatterns = [
    path("my-bookings", views.UpcomingBookingsApproved.as_view(), name="upcoming-bookings"),
    path("new-booking", views.NewBooking.as_view(), name="new-booking"),
]