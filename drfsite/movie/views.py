from django.core.serializers import serialize
from django.forms import model_to_dict
from django.shortcuts import render
from django.template.defaultfilters import title
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie
from .serializers import MovieSerializer


# class MovieAPIView(generics.ListAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


class MovieAPIList(generics, ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieAPIView(APIView):
    def get(self, request):
        m = Movie.objects.all()
        return Response({'post': MovieSerializer(m, many=True).data})

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': "Methon PUT not allowed"})
        try:
            instance = Movie.objects.get(pk=pk)
        except:
            return Response({'error': "Methon PUT not allowed"})

        serializer = MovieSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': "Method DELETE not allowed"})

        Movie.objects.filter(pk=pk).delete()

        return Response({"post": "delete post" + str(pk)})