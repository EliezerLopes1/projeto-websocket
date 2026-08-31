from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator


class User(models.Model):
    name = models.CharField(max_length=40, unique=True)


class Room(models.Model):
    name = models.CharField(max_length=40, unique=True)


class Connection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="connections")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="connections")


class Message(models.Model):
    text = models.TextField()
    date = models.TimeField(default=timezone.now)
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE, related_name="messages")
