from rest_framework.serializers import ModelSerializer, SerializerMethodField
from users.models import User
from blog.models import Blog
from rest_framework import serializers


class RegisterSerializer(ModelSerializer):

    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'profile', 'password1', 'password2']

    def validate(self, data):
        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 != password2:
            raise serializers.ValidationError({"warning":"password does not mathched"})
        
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data['password1']
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            bio = validated_data['bio'],
            profile = validated_data['profile']
        )
        user.set_password(password)
        user.save()
        return user
    

    
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