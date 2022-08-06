from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework import status

from .serializers import MySerializer, ShowPlayerSerializer, CreatePlayerSerializer
from .models import Player

import mygame
# Create your views here.


class Game(APIView):
    
    authentication_classes = [SessionAuthentication]
    
    
    #all players
    def get(self, request):
        data = Player.objects.all()
        serializer = MySerializer(data, many=True)
        
        print(mygame.genereta_all())
        return Response(serializer.data)
    

    
    #create player
    def post(self, request):
        res = request.data     #data = {"user":123456}
        data = mygame.createBoard(res["user"])
        try:
            instance = Player.objects.get(user=res["user"])
            serializer = CreatePlayerSerializer(instance=instance, data=data)
            print('user exist')
        except Player.DoesNotExist:
            serializer = CreatePlayerSerializer(data=data)
            print('user created')
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        
        
        
class EditBoard(APIView):
    
    authentication_classes = [SessionAuthentication]
    
    
    #show player detail
    def get(self, request):
        new = request.META["HTTP_USER"]
        try:
            data = Player.objects.get(user=new)
        except Player.DoesNotExist:
            return Response({"User": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        
        serializer = ShowPlayerSerializer(data)
        return Response(serializer.data)
    

    
    #move player and win or loss
    def put(self, request):
        user = request.META["HTTP_USER"]    #INSTANCE={"loc_x": 5} ---> DATA={"loc_x": -1}
        try:
            instance = Player.objects.get(user=user)
        except Player.DoesNotExist:
            return Response({"User": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        data = mygame.moveX(instance, data)
        

        #end game /win or loss
        if True in data.values():
            serializer = MySerializer(instance=instance, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        
        #countinue
        serializer = ShowPlayerSerializer(instance=instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
            
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    
    #delete player
    def delete(self, request):
        user = request.META["HTTP_USER"]
        try:
            data = Player.objects.get(user=user)
        except Player.DoesNotExist:
            return Response({"User": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    