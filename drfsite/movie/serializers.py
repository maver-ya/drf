import io

from django.template.defaultfilters import title
from rest_framework import serializers
from rest_framework.parsers import JSONParser

from movie.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Movie
        fields = "__all__"
