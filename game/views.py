from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import GameClass
from .serializers import MySerializer

# Create your views here.



class Myview(APIView):
    def get(self, request):
        data = GameClass.objects.all()
        serializer = MySerializer(data, many=True)
        return Response(serializer.data)