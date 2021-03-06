"""loginForm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page),
    path('login_request/', views.login_request),
    path('login_validate/', views.login_validate),
    path('register_user/', views.register_request),
    path('register/', views.register),
                  path('logout_request/', views.logout_request),
                  url(r'^like\/(?P<image_link>[-.\/\w]+)\/(?P<username>[-.\w]+)', views.like),
                  url(r'^confirm\/(?P<username>[\w]+)\/(?P<token>[\w]+)', views.confirm)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
