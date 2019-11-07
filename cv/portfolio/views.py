from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
# Create your views here.
def show(request):
    return render(request,'index.html')

def form(request):
    return render(request,'form.html')

def profile(request):
    info={
        'name':request.POST['name'],
        'dob':request.POST['dob'],
        'mother_name':request.POST['Mother_Name'],
        'from':request.POST['from'],
        'current':request.POST['current'],
        'school':request.POST['school'],
        'university':request.POST['university'],
        'x':request.POST['x'],
        'xii':request.POST['xii'],
        'hobbies':request.POST['hobbies'].split('\n'),
        'skills':request.POST['skills'].split('\n'),
        'desc':request.POST['desc'].split('\n'),
        'dp':'pics/'+request.POST['dp'],
    }
    obj=Person(name=info['name'],dob=info['dob'],mot_name=info['mother_name'],From=info['from'],current=info['current'],school=info['school'],university=info['university'],x=info['x'],xii=info['xii'],hobbies=info['hobbies'],skills=info['skills'],desc=info['desc'],dp=info['dp'])
    obj.save()
    info['dp']=obj.dp
    print(info['dp'])
    return render(request,'profile.html',info)