from . import views
from django.urls import path


urlpatterns = [
    path("", views.BookingsApproved.as_view(), name="bookings"),
]
