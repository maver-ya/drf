import io

from django.template.defaultfilters import title
from rest_framework import serializers
from rest_framework.parsers import JSONParser

from movie.models import Movie

# class WomenModel:
#     def __init__(self):
#         self.title = title
#         self.description = description

class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    photo = serializers.ImageField()
    release_date = serializers.DateField()
    duration = serializers.IntegerField()
    rating = serializers.DecimalField(max_digits=3, decimal_places=1)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.cat_id = validated_data.get('cat', instance.cat_id)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()

        return instance

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


