from django.db import models
from users.models import User


class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='blog_images')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title