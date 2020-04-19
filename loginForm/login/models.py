# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class UserDB(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class UserImage(models.Model):
    username = models.CharField(max_length=100, unique=True)
    dp = models.ImageField(upload_to='dp', null=True)
    contest_photo = models.ImageField(upload_to='contest_photo', null=True)

    def __str__(self):
        return self.username


class LikedPhotos(models.Model):
    user_liked = models.CharField(max_length=100)
    image_link = models.CharField(max_length=200)

    def __str__(self):
        return self.user_liked
