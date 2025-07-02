from rest_framework import serializers

from booking.models import Bookings


class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = '__all__'