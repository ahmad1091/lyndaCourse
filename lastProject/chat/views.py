from django.shortcuts import render
from rest_framework import status,generics
from rest_framework.permissions import IsAuthenticated
from chat.models import Message, Room
from chat.serializers import RoomSerializer,MessageSerializer

# Create your views here.


class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class MessageList(generics.ListCreateAPIView):
    serializer_class = MessageSerializer    
    def get_queryset(self):
        room_id=Room.objects.get(id=self.kwargs['id'])
        return Message.objects.filter(room=room_id)

