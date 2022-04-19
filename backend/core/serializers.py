from rest_framework import serializers
from .models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = ['id', 'name', 'get_images']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
