from django.shortcuts import render
from rest_framework import viewsets
from .models import Trek, JoinRequest
from .serializers import TrekSerializer, JoinRequestSerializer
from rest_framework.permissions import IsAuthenticated


class TrekViewSet(viewsets.ModelViewSet):
    queryset = Trek.objects.all()
    serializer_class = TrekSerializer
    permission_classes = [IsAuthenticated]  # Allow any user to access trek endpoints

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
class JoinRequestViewSet(viewsets.ModelViewSet):
    queryset = JoinRequest.objects.all()
    serializer_class = JoinRequestSerializer
    permission_classes = [IsAuthenticated]  # Allow any user to access join request endpoints

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
