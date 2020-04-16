# Create your views here.
from django.shortcuts import render

from login.login_form import LoginForm, RegisterUser
from .models import UserDB


def home_page(request):
    return render(request, 'home_page.html')


def login_request(request):
    form = LoginForm()
    context = dict()
    context['form'] = form
    return render(request, 'login.html', context)


def login_validate(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        # try:
        if form.is_valid():
            username = form.cleaned_data['username']
            return render(request, 'user.html', {'username': username})
        # except:
        #   pass
    else:
        return render(request, 'user.html', {'username': 'not_authenticated'})
    return render(request, 'user.html', {'username': 'not_registered'})


def register_request(request):
    form = RegisterUser()
    context = dict()
    context['form'] = form
    return render(request, 'register.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            new_user = UserDB(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            new_user.save()
            return render(request, 'user.html', {'username': form.cleaned_data['username']})
        else:
            return render(request, 'register.html', {'status': 'Fill form correctly'})
