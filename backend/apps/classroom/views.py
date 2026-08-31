from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User, Room, Connection
from .serializers import UserListSerializer, UserCreateSerializer, RoomListSerializer, RoomCreateSerializer, ConnectionRoomSerializer, UserLoginSerializer, MessageListSerializer


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request, user_name):
        user = get_object_or_404(User, name=user_name)
        serializer = UserLoginSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RoomView(APIView):
    def get(self, request):
        creator = get_object_or_404(User, name=request.query_params['creator'])
        room = Connection.objects.filter(user=creator)
        room = [connection.room for connection in room]
        serializer = RoomListSerializer(room, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoomCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            creator = get_object_or_404(User, name=request.data['creator'])
            Connection.objects.create(user=creator, room=serializer.instance)
            for user in request.data.get('users', []):
                user_exist = get_object_or_404(User, name=user)
                Connection.objects.create(user=user_exist, room=serializer.instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomUserView(APIView):
    def post(self, request, room_name):
        room = get_object_or_404(Room, name=room_name)
        add_user = get_object_or_404(User, name=request.data['name'])
        serializer = ConnectionRoomSerializer(data={'user': add_user.id, 'room': room.id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageView(APIView):
    def get(self, request, room_name):
        room = get_object_or_404(Room, name=room_name)
        list_room = Connection.objects.filter(room=room)
        message_room = [message for connection in list_room for message in connection.messages.all()]
        serializer = MessageListSerializer(message_room, many=True)
        return Response(serializer.data)
