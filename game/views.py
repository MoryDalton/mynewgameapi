# from django.http import Http404, HttpResponseNotFound
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
        data = request.data
        serializer = MySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        

class MyViewUser(APIView):
    authentication_classes = []
    

    
    

    def get(self, request, id):
        try:
            data = GameClass.objects.get(id=id)
        except GameClass.DoesNotExist:
            return Response({"User":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
            

        serializer = MySerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        try:
            instance = GameClass.objects.get(id=id)
        except GameClass.DoesNotExist:
            return Response({"User":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
            
        serializer = MySerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        
    
    
    def delete(self, request, id):
        try:
            data = GameClass.objects.get(id=id)
        except GameClass.DoesNotExist:
            return Response({"User":"Not Found"}, status=status.HTTP_404_NOT_FOUND)

        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    