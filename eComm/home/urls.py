from django.urls import path
from . import views


urlpatterns=[
    path('',views.show),
    path('login-register/',views.check),
    path('login/',views.login),
    path('register/',views.register),
    path('validate/',views.validate),
    path('logout/',views.logout),
]