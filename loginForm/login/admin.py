# Register your models here.
from django.contrib import admin

from .models import UserDB, UserImage, LikedPhotos

admin.site.register(UserDB)

admin.site.register(UserImage)

admin.site.register(LikedPhotos)
