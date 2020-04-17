# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from login.forms import LoginForm, RegisterUser


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


@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('/register_user/')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        return render(request, 'register.html', {'status': 'Fill form correctly'})
