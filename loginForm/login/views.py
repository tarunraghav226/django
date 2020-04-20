# Create your views here.
import random

from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from login.forms import LoginForm, RegisterUser, UserImageForm
from login.models import UserImage, LikedPhotos
from loginForm import settings


def home_page(request):
    return render(request, 'home_page.html')


def login_request(request):
    form = LoginForm()
    context = dict()
    context['form'] = form
    return render(request, 'login.html', context)


@csrf_exempt
def login_validate(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user:
                all_user = UserImage.objects.filter(username=form.cleaned_data['username'])
                image_link = ''
                for i in all_user:
                    image_link += str(i.contest_photo)
                likes = LikedPhotos.objects.filter(image_link=image_link)
                login(request, user)
                return render(request, 'home_page.html', {'image_link': image_link, 'number_of_likes': likes.count()})
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

            # mail details
            CONFIRMATION_SUBJECT = 'Account Confirmation Link'
            CONFIRMATION_MESSAGE = 'Dear ' + user.username + ',\n We are happy that you registered to our contest.' + \
                                   'Please click on the below link to activate your account\n' + generate_confirmation_link(
                user.username)
            send_mail(CONFIRMATION_SUBJECT, CONFIRMATION_MESSAGE, settings.EMAIL_HOST,
                      [user_form.cleaned_data['email']], True)

            messages.success(request, 'Account Created Successfully')
            return redirect('/register_user/')
        else:
            return render(request, 'register.html', {'user_form': user_form, 'image_form': image_form})
    else:
        return render(request, 'register.html', {'status': 'Fill form correctly'})


def logout_request(request):
    logout(request)
    return redirect('/')


@login_required
def like(requset, image_link, username):
    has_user_already_liked = LikedPhotos.objects.filter(user_liked=username)
    likes = LikedPhotos.objects.filter(image_link=image_link)

    if not has_user_already_liked:
        like = LikedPhotos()
        like.image_link = image_link
        like.user_liked = username
        like.save()
    else:
        messages.info(requset, 'You already liked a photo you can\'t vote again')

    return render(requset, 'home_page.html', {'image_link': image_link, 'number_of_likes': likes.count()})


def generate_confirmation_link(username):
    s = 'aAbZcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890'
    link = '127.0.0.1:8000/confirm/' + username + '/'
    i = 20
    while i > 0:
        a = random.randint(0, len(s) - 1)
        link += s[a]
        i -= 1
    return link


def confirm(request, username, token):
    messages.info(request, 'Account confirmed ' + username)
    return redirect('/')
