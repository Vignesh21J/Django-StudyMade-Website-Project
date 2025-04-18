# from django.http import JsonResponse

# def getRoutes(request):

#     routes = [
#         'GET /api',   #HomePage
#         'GET /api/rooms',
#         'GET /api/rooms/:id'
#     ]
#     return JsonResponse(routes, safe=False)


from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Room
from .serializers import RoomSerializer
# from base.api import serializers


@api_view(['GET'])
def getRoutes(request):

    routes = [
        'GET /api',   #HomePage
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)   #many=True it means there are many python objects that is converted to json by using serializers.py
    return Response(serializer.data)


@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)