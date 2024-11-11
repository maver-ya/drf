from django.contrib import admin
from django.urls import path, include, re_path

from movie.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/movie/', MovieAPIList.as_view()),
    path('api/v1/movie/<int:pk>/', MovieAPIUpdate.as_view()),
    path('api/v1/moviedelete/<int:pk>/', MovieAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),  # new
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # new
]
