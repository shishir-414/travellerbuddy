from rest_framework import serializers
from .models import User 

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['id', 'username', 'email', 'bio', 'fitness_level', 'profile_picture', 'experience']
        read_only_fields = ['id']

    def validate_fitness_level(self, value):
        if value < 1 or value > 10:
            raise serializers.ValidationError("Fitness level must be between 1 and 10.")
        return value