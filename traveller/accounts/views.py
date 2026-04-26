from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self): # <--- Rename this from 'queryset' to 'get_queryset'
        queryset = User.objects.all()
        exp = self.request.query_params.get('experience')
        if exp is not None:
            queryset = queryset.filter(experience=exp)
        return queryset