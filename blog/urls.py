from django.urls import path
from rest_framework.routers import DefaultRouter
from blog.views import BlogViewSet


router = DefaultRouter()
router.register(r'', BlogViewSet, basename='blog')

urlpatterns = [
    
] + router.urls