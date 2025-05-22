from rest_framework.viewsets import ModelViewSet
from blog.models import Blog
from blog.serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsAuthorOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    parser_classes = [MultiPartParser, FormParser]  

    def perform_create(self, serializer):
        serializer.save(author=self.request.user) 

    
    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        elif self.action == 'retrieve':
            return [IsAuthenticated()]
        elif self.action == 'create':
            return [IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAuthorOrReadOnly()]
        
        return [IsAuthenticated()]
        