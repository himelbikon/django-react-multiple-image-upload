from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class HumanAPIView(APIView):

    def get(self, request):
        humans = Human.objects.all()
        serializer = HumanSerializer(humans, many=True)
        return Response(serializer.data)

    def post(self, request):
        print('---------', request.data)
        serializer = HumanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        human = Human.objects.get(pk=serializer.data['id'])

        images = dict((request.data).lists())['images']

        for image in images:
            image = Image(image=image, human=human)
            image.save()

        return Response(serializer.data)


class MovieAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        name = request.data.get('name')
        poster = request.data.get('poster')

        print('-----------', name, poster)

        movie = Movie(name=name, poster=poster)
        movie.save()

        serializer = MovieSerializer(movie)

        return Response(serializer.data)
