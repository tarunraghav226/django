from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from login.models import UserImage


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterUser(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):

        user = User()
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.password = self.cleaned_data['password1']

        if commit:
            user.save()
        return user


class UserImageForm(forms.ModelForm):
    class Meta:
        model = UserImage
        fields = ('dp', 'contest_photo')

    def save(self, username, commit=True):
        image_user = UserImage()
        image_user.username = username
        image_user.dp = self.cleaned_data['dp']
        image_user.contest_photo = self.cleaned_data['contest_photo']

        if commit:
            image_user.save()
        return image_user
