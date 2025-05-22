from django.urls import path
from rest_framework.routers import DefaultRouter
from users.views import register_view, whoami, UserListAPIView

# router = DefaultRouter()
# router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    path('register/', register_view),
    path('whoami/', whoami),
    path('users/', UserListAPIView.as_view())
] #+ router.urls