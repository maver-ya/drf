from django.core.serializers import serialize
from django.forms import model_to_dict
from django.shortcuts import render
from django.template.defaultfilters import title
from rest_framework import generics, viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from drfsite.settings import WSGI_APPLICATION
from .models import Movie
from .serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


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

# class MovieAPIView(generics.ListAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
