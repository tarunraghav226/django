# Create your views here.
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from login.forms import LoginForm, RegisterUser, UserImageForm


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
    user_form = RegisterUser()
    image_form = UserImageForm()
    context = dict()
    context['user_form'] = user_form
    context['image_form'] = image_form
    return render(request, 'register.html', context)


@csrf_exempt
def register(request):
    if request.method == 'POST':
        user_form = RegisterUser(request.POST)
        image_form = UserImageForm(request.POST, request.FILES)

        if user_form.is_valid() and image_form.is_valid():
            user = user_form.save()
            image_form.save(username=user.username)

            messages.success(request, 'Account Created Successfully')
            return redirect('/register_user/')
        else:
            return render(request, 'register.html', {'user_form': user_form, 'image_form': image_form})
    else:
        return render(request, 'register.html', {'status': 'Fill form correctly'})


def logout_request(request):
    logout(request)
    return redirect('/')
