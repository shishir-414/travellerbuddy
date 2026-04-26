from .views import UserViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
# Explicitly provide 'basename' so the router doesn't crash 
# searching for a .model attribute in your viewset.
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]