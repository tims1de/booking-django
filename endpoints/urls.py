from django.urls import include, path

from .bookings import urls as booking_urls
from .rooms import urls as rooms_urls
from .users import urls as users_urls

urlpatterns = [
    path('users/', include(users_urls)),
    path('rooms/', include(rooms_urls)),
    path('bookings/', include(booking_urls)),
]

