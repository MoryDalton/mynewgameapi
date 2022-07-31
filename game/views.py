from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework import status
from .models import GameClass
from .serializers import MySerializer

# Create your views here.



class Myview(APIView):
    authentication_classes = [SessionAuthentication]
    
    def get(self, request):
        data = GameClass.objects.all()
        serializer = MySerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        mydata=request.data
        serializer = MySerializer(data=mydata)
        if serializer.is_valid():
            serializer.save()
            return Response({"User": "added"}, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)