from django.contrib import admin
from django.urls import path

from apps.classroom.views import HelloView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello', HelloView.as_view()),
]
