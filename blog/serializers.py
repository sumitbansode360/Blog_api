from rest_framework.serializers import ModelSerializer
from users.models import User
from blog.models import Blog

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'profile']

class BlogSerializer(ModelSerializer):

    author_detail = UserSerializer(source="author",read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'image', 'date', 'author', 'author_detail']