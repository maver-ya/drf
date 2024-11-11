from django.forms import model_to_dict
from django.shortcuts import render
from django.template.defaultfilters import title
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie
from .serializers import MovieSerializer

# class MovieAPIView(generics.ListAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


class MovieAPIView(APIView):
    def get(self, request):
        lst = Movie.objects.all().values()
        return Response({'post': list(lst)})

    def post(self, request):
        post_new = Movie.objects.create(
            title=request.date['title'],
            description=request.date['description'],
            release_date=request.date['release_date'],
            duration=request.date['duration'],
            rating=request.date['rating'],
            cat_id=request.date['cat_id']

        )
        return Response({'post': model_to_dict(post_new)})
