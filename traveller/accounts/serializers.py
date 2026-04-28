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

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User 
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # This will print in your terminal when you hit the register endpoint
        print(f"DEBUG: Creating user {validated_data['username']} with hashed password")
        
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
