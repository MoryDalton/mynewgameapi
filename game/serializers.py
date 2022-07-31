from dataclasses import field
from rest_framework import serializers
from .models import GameClass


class MySerializer(serializers.ModelSerializer):
    class Meta:
        model = GameClass
        fields = ['name', 'message']