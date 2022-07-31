from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.



class Myview(APIView):
    def get(self, request):
        data={"data": "hello mory"}
        return Response(data)