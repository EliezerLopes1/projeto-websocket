from rest_framework import serializers
from rest_framework.serializers import ValidationError

from .models import User, Room, Connection, Message


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name']

    def validate_name(self, value):
        if User.objects.filter(name=value).exists():
            raise ValidationError('Usuário já existe')
        return value


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']


class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name']


class RoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['name']

    def validate_name(self, value):
        if Room.objects.filter(name=value).exists():
            raise ValidationError('Já existe uma sala com esse nome')
        return value


class ConnectionRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ['user', 'room']

    def validate(self, value):
        if Connection.objects.filter(user=value['user'], room=value['room']).exists():
            raise ValidationError("Usuário já adicionado na sala")
        return value


class MessageListSerializer(serializers.ModelSerializer):
    usuario = serializers.CharField(source='connection.user.name')

    class Meta:
        model = Message
        fields = ['id', 'text', 'date', 'connection', 'usuario']
