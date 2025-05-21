from rest_framework.serializers import ModelSerializer, SerializerMethodField
from users.models import User
from blog.models import Blog

class BlogUserSerializer(ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'image', 'date']


class UserBlogSerializer(ModelSerializer):

    blogs = SerializerMethodField() 

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile', 'blogs']

    def get_blogs(self, obj):
        blogs = Blog.objects.filter(author=obj)
        return BlogUserSerializer(blogs, many=True).data