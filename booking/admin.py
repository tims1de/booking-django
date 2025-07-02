from django.contrib import admin
from .models import Bookings

@admin.register(Bookings)
class AdminBookings(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

        obj = form.instance
        obj.price_per_day = sum(room.price for room in obj.rooms.all())
        obj.total_price = obj.total_days * obj.price_per_day
        obj.save()
