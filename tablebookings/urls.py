from . import views
from django.urls import path


urlpatterns = [
    path("", views.UpcomingBookingsApproved.as_view(), name="upcoming-bookings"),
    path("pending", views.UpcomingBookingsPending.as_view(), name="pending-bookings"),

    path("new-booking", views.NewBooking.as_view(), name="new-booking"),
    path('edit-booking/<int:pk>', views.EditBooking.as_view(), name="edit-booking"),
    path('delete-booking/<int:pk>', views.DeleteBooking.as_view(), name="delete-booking"),

    path('admin-all', views.AllUpcomingBookings.as_view(), name="admin-all-bookings"),
    path('admin-approve-booking/<int:pk>', views.ApproveBooking.as_view(), name="admin-approve-booking"),
    path('admin-cancel-booking/<int:pk>', views.CancelBooking.as_view(), name="admin-cancel-booking"),
    path('admin-update-booking/<int:pk>', views.UpdateBooking.as_view(), name="admin-update-booking"),

]
