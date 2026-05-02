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
        # Added 'user' to read_only so it's handled by the backend, not the user input
        read_only_fields = ['status', 'user']

    def validate(self, data):
        user = self.context['request'].user
        trek = data['trek']

        # 1. Guard: Don't let organizers join their own trek
        if trek.created_by == user:
            raise serializers.ValidationError("You are the organizer of this trek!")

        # 2. Guard: Prevent duplicate requests
        if JoinRequest.objects.filter(user=user, trek=trek).exists():
            raise serializers.ValidationError("You have already requested to join this trek.")

        # 3. Guard: Check capacity
        if trek.participants.filter(status='accepted').count() >= trek.max_participants:
            raise serializers.ValidationError("This trek has reached its maximum number of participants.")

        return data