from .models import Trek,JoinRequest
from rest_framework import serializers

class TrekSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model = Trek
        fields = '__all__'

class JoinRequestSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    trek_title = serializers.ReadOnlyField(source='trek.title')
    class Meta:
        model = JoinRequest
        fields = '__all__'
        read_only_fields = ['status']