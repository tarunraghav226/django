from django import forms

from .models import UserDB


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        super(LoginForm, self).clean()

        dbuser = UserDB.objects.filter(username=self.cleaned_data.get('username'),
                                       password=self.cleaned_data.get('password'))

        if not dbuser:
            raise forms.ValidationError('User not registered')
        return self.cleaned_data


class RegisterUser(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())
