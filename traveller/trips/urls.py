from .views import TrekViewSet, JoinRequestViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include 

router = DefaultRouter()
router.register(r'treks', TrekViewSet, basename='trek')
router.register(r'join-requests', JoinRequestViewSet, basename='join-request')

urlpatterns = [
    path('', include(router.urls)),
]