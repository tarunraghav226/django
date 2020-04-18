# Register your models here.
from django.contrib import admin

from .models import UserDB, UserImage

admin.site.register(UserDB)

admin.site.register(UserImage)
