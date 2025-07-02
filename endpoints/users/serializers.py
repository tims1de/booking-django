from rest_framework import serializers

from endpoints.bookings.serializers import BookingsSerializer
from users.models import Users


class UsersSerializer(serializers.ModelSerializer):
    bookings = BookingsSerializer(many=True,read_only=True)

    class Meta:
        model = Users
        fields = '__all__'