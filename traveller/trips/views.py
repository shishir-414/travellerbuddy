from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import Trek, JoinRequest
from .serializers import TrekSerializer, JoinRequestSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class TrekViewSet(viewsets.ModelViewSet):
    queryset = Trek.objects.all()
    serializer_class = TrekSerializer
    permission_classes = [IsAuthenticated]  # Allow any user to access trek endpoints
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields=['difficulty' , 'destination']
    search_fields = ['title', 'destination', 'description']
    ordering_fields = ['start_date', 'cost_per_person']
    

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
class JoinRequestViewSet(viewsets.ModelViewSet):
    queryset = JoinRequest.objects.all()
    serializer_class = JoinRequestSerializer
    permission_classes = [IsAuthenticated]  # Allow any user to access join request endpoints

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
