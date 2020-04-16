# Create your views here.
from django.shortcuts import render

from login.login_form import LoginForm


def login_request(request):
    form = LoginForm()
    context = dict()
    context['form'] = form
    return render(request, 'login.html', context)


def login_validate(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['username'])
            return render(request, 'user.html', {'username': form.cleaned_data['username']})
