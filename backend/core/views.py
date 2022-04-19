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
        serializer = HumanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        human = Human.objects.get(pk=serializer.data['id'])

        images = dict((request.data).lists())['images']

        for image in images:
            image = Image(image=image, human=human)
            image.save()

        return Response(serializer.data)
