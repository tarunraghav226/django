from django import forms

from .models import UserDB


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        name = self.cleaned_data['username']
        user = UserDB.objects.filter(username=name)

        if not user:
            raise forms.ValidationError('User not registered')
        return user


class RegisterUser(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())
