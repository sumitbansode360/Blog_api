from users.serializers import UserBlogSerializer, RegisterSerializer
from users.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListAPIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FormParser


@swagger_auto_schema(method="post", request_body=RegisterSerializer)
@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
@permission_classes([AllowAny])
def register_view(request):
    data = request.data 
    ser = RegisterSerializer(data=data)
    if ser.is_valid():
        ser.save()    
        return Response({"success":"registerd successfully!"})
    return Response({"message": ser.errors})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def whoami(request):
    return Response({"id":request.user.id, "user":request.user.username})

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserBlogSerializer