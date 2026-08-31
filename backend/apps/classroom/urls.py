from django.urls import path
from .views import UserView, UserLoginView, RoomView, RoomUserView, MessageView


app_name = "classroom"

urlpatterns = [
    path("user/", UserView.as_view(), name="user-list"),
    path("login/<str:user_name>/", UserLoginView.as_view(), name="user-login"),
    path("room/", RoomView.as_view(), name="room-list"),
    path("room/<str:room_name>/users/", RoomUserView.as_view(), name="room-user"),
    path("room/<str:room_name>/messages/", MessageView.as_view(), name="room-messages"),
]
