from . import views
from django.urls import path


urlpatterns = [
    path("", views.UpcomingBookingsApproved.as_view(), name="upcoming-bookings"),
    path("new-booking", views.NewBooking.as_view(), name="new-booking"),
    path('edit-booking/<int:pk>', views.EditBooking.as_view(), name="edit-booking"),
]
