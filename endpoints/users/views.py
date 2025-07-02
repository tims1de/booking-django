from django.db.models import Count, Q
from rest_framework.decorators import api_view
from rest_framework.response import Response

from endpoints.users.serializers import UsersSerializer
from users.models import Users


@api_view(['GET'])
def get_all_users(request):
    users = Users.objects.all()
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_users_by_bookings(request, book_amount):
    users = (Users.objects.annotate(count_bookings=Count('bookings'))
             .filter(Q(count_bookings__gte=int(book_amount)))
             .prefetch_related('bookings'))
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data)