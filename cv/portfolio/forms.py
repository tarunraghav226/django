from django import forms

class PortfolioForm(forms.Form):
    name=forms.CharField(max_length=30)
    dob=forms.DateField()
    mot_name=forms.CharField(max_length=30)
    From=forms.CharField(max_length=30)
    current=forms.CharField(max_length=30)
    school=forms.CharField(max_length=30)
    university=forms.CharField(max_length=30)
    x=forms.CharField(max_length=5)
    xii=forms.CharField(max_length=5)
    hobbies=forms.CharField()
    skills=forms.CharField()
    desc=forms.CharField()
    dp=forms.ImageField()