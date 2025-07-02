from django.urls import path

from . import views as booking_views

urlpatterns = [
    path('all_bookings/', booking_views.get_all_bookings),
    path('add_booking/', booking_views.add_booking),
]