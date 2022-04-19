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

        for i in range(100):
            image = request.data.get(f'poster{i}')
            if image:
                obj = Image(image=image, human=human)
                obj.save()
            else:
                break

        return Response(serializer.data)


class MovieAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        name = request.data.get('name')
        poster = request.data.get('poster1')
        print('-----------', name, poster)

        movie = Movie(name=name, poster=poster)
        movie.save()

        serializer = MovieSerializer(movie)

        return Response(serializer.data)
