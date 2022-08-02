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
        # print(data)
        serializer = MySerializer(data, many=True)
        return Response(serializer.data)

    
    def post(self, request):
        # mydata=request.data
        # serializer = MySerializer(data=mydata)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response({"User": "added"}, status=status.HTTP_201_CREATED)
        # return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        data = request.data     # data = {"number": number, "r": 1 or -1}
        serializer = MySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"User": "added"}, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        

class MyViewUser(APIView):
    authentication_classes = [SessionAuthentication]
    
    def get(self, request, id):
        data = GameClass.objects.get(id=id)
        serializer = MySerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        instance = GameClass.objects.get(id=id)
        serializer = MySerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        
    
    
    def delete(self, request, id):
        data = GameClass.objects.get(id=id)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        