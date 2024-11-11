from django.contrib import admin
from django.urls import path, include

from movie.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'movie', MovieViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
    # path('api/v1/movielist', MovieAPIViewSet.as_view({'get': 'list'})),
    # path('api/v1/movielist/<int:pk>', MovieAPIViewSet.as_view({'put': 'update'})),
]
