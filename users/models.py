from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    bio = models.CharField(max_length=400)
    profile = models.ImageField(upload_to='user_images')

    def __str__(self):
        return self.username