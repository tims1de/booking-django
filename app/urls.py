from django.contrib import admin
from django.urls import include, path

import endpoints.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(endpoints.urls))
]
