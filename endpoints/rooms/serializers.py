from rest_framework import serializers

from rooms.models import Rooms


class RoomsSerializer(serializers.ModelSerializer):
    booked_rooms = serializers.IntegerField(read_only=True)
    left_rooms = serializers.IntegerField(read_only=True)

    class Meta:
        model = Rooms
        fields = [f.name for f in Rooms._meta.fields] + ['booked_rooms'] + ['left_rooms']