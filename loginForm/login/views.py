# Create your views here.
from django.shortcuts import render

from login.login_form import LoginForm


def login_request(request):
    form = LoginForm()
    context = dict()
    context['form'] = form
    return render(request, 'login.html', context)


def login_validate(request):
    username = 'not_authenticated'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        try:
            if form.is_valid():
                return render(request, 'user.html', {'username': form.cleaned_data['username']})
        except:
            return render(request, 'user.html', {'username': 'not_registered'})

    else:
        return render(request, 'user.html', {'username': username})
