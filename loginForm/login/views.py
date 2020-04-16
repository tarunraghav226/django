# Create your views here.
from django.shortcuts import render

from login.login_form import LoginForm


def login_request(request):
    form = LoginForm()
    context = dict()
    context['form'] = form
    return render(request, 'login.html', context)
