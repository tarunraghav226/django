# Create your views here.
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
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
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Register Yourself')
                return redirect('/register_user/')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        return render(request, 'user.html', {'username': 'not_authenticated'})


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


def logout_request(request):
    logout(request)
    return redirect('/')
