from django.contrib import admin
from django.urls import path, include

from movie.views import *
from rest_framework import routers




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/movie/', MovieAPIList.as_view()),
    path('api/v1/movie/<int:pk>/', MovieAPIUpdate.as_view()),
    path('api/v1/moviedelete/<int:pk>/', MovieAPIDestroy.as_view())
]

