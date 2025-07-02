from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from booking.models import Bookings
from endpoints.bookings.serializers import BookingsSerializer


@api_view(['GET'])
def get_all_bookings(request):
    bookings = Bookings.objects.all()
    serializer = BookingsSerializer(bookings, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def add_booking(request):
    if request.method == 'POST':
        serializer = BookingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        serializer = BookingsSerializer()
        return Response(serializer.data)