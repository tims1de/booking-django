from django.urls import path

from . import views as user_views

urlpatterns = [
    path('all_users/', user_views.get_all_users),
    path('users_by_amount_of_bookings/<book_amount>', user_views.get_users_by_bookings),
]