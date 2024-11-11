from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Movie, Category
from .serializers import MovieSerializer

class MovieViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    # queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Movie.objects.all()[:3]

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})

# class MovieAPIList(generics, ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
#
# class MovieAPIUpdate(generics.UpdateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
#
# class MovieAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
