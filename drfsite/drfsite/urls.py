from django.contrib import admin
from django.urls import path, include

from movie.views import *
from rest_framework import routers


class MyCustomRouter(routers.SimpleRouter):
    routes = [
        routers.Route(url=r'^{prefix}$',
                      mapping={'get': 'list'},
                      name='{basename}-list',
                      detail=False,
                      initkwargs={'suffix': 'List'}),
        routers.Route(url=r'^{prefix}/{lookup}$',
                      mapping={'get': 'retrieve'},
                      name='{basename}-detail',
                      detail=True,
                      initkwargs={'suffix': 'Detail'})
    ]


router = routers.DefaultRouter()
router.register(r'movie', MovieViewSet, basename='movie')
print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
    # path('api/v1/movielist', MovieAPIViewSet.as_view({'get': 'list'})),
    # path('api/v1/movielist/<int:pk>', MovieAPIViewSet.as_view({'put': 'update'})),
]
