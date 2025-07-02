from django.core.cache import cache
from django.db.models import Count, ExpressionWrapper, F, IntegerField, Q
from rest_framework.decorators import api_view
from rest_framework.response import Response

from endpoints.rooms.serializers import RoomsSerializer
from rooms.models import Rooms


@api_view(['GET'])
def get_all_rooms(request):
    cache_key = 'all_rooms'
    cached_data = cache.get(cache_key)

    if cached_data is not None:
        return Response(cached_data)

    rooms = Rooms.objects.all()
    serializer = RoomsSerializer(rooms, many=True)
    cache.set(cache_key, serializer.data, timeout=60 * 5)

    return Response(serializer.data)

@api_view(['GET'])
def get_left_rooms_by_date(request):
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')

    rooms = (Rooms.objects.annotate(booked_rooms=Count('bookings',
                     filter=(
                         (Q(bookings__date_from__gte=date_from) & Q(bookings__date_from__lte=date_to)) |
                         (Q(bookings__date_from__lte=date_from) & Q(bookings__date_to__gt=date_from))))
                        )
                    .annotate(
                    left_rooms=ExpressionWrapper(F('quantity') - F('booked_rooms'), output_field=IntegerField()))
                    .filter(Q(left_rooms__gte=1)))

    serializer = RoomsSerializer(rooms, many=True)
    return Response(serializer.data)