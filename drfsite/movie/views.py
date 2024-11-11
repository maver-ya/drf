from django.core.serializers import serialize
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
        m = Movie.objects.all()
        return Response({'post': MovieSerializer(m, many=True).data})

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Movie.objects.create(
            title=request.date['title'],
            description=request.date['description'],
            release_date=request.date['release_date'],
            duration=request.date['duration'],
            rating=request.date['rating'],
            cat_id=request.date['cat_id']

        )
        return Response({'post': MovieSerializer(post_new).data})
