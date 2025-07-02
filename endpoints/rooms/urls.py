from django.urls import path

from . import views as room_views

urlpatterns = [
    path('all_rooms/', room_views.get_all_rooms),
    path('left_rooms/', room_views.get_left_rooms_by_date),
]