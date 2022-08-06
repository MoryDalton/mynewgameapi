from rest_framework.serializers import ModelSerializer
from .models import Player




class MySerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
        
        
        
class ShowPlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = ['user', 'loc_x', 'win', 'loss']
        
        
        
class CreatePlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
        
        extra_kwargs = {
            'loc_w': {'write_only': True},
            'loc_d': {'write_only': True},
        }
        