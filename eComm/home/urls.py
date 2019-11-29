from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns=[
    path('',views.show),
    path('login-register/',views.check),
    path('login/',views.login),
    path('register/',views.register),
    path('validate/',views.validate),
    path('logout/',views.logout),
    url(r'^viewProduct(?P<product_id>[0-9]{1,2})/',views.viewProduct)
]