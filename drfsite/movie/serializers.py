import io

from django.template.defaultfilters import title
from rest_framework import serializers
from rest_framework.parsers import JSONParser

from movie.models import Movie


# class WomenModel:
#     def __init__(self):
#         self.title = title
#         self.description = description

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        field = "__all__"

# def encode():
#     model = MovieModel("1+1", "Description: Оно")
#     model_sr = MovieSerializer(model)
#     print(model_sr, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{title: "It", "description": "Description:  asdas}')
#     data = JSONParser().parse(stream)
#     serializer = MovieSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
