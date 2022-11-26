from . import views
from django.urls import path


urlpatterns = [
    path("", views.UpcomingBookingsApproved.as_view(), name="upcoming-bookings"),
    path("new-booking", views.New.as_view(), name="new-booking"),
]