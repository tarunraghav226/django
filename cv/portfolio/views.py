from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from .forms import PortfolioForm

# Create your views here.
def show(request):
    return render(request,'index.html')

def form(request):
    return render(request,'form.html')

def saveProfile(request):
    person=Person()
    person.name=request.POST.get('name')
    person.dob=request.POST.get('dob')
    person.mot_name=request.POST.get('mot_name')
    person.From=request.POST.get('from')
    person.current=request.POST.get('current')
    person.school=request.POST.get('school')
    person.university=request.POST.get('university')
    person.x=request.POST.get('x')
    person.xii=request.POST.get('xii')
    person.hobbies=request.POST.get('hobbies')
    person.skills=request.POST.get('skills')
    person.desc=request.POST.get('desc')
    person.dp=request.FILES['dp']
    person.save()
    person.desc=list(person.desc.split('\n'))
    person.hobbies=person.hobbies.split('\n')
    person.skills=person.skills.split('\n')
    return render(request,'profile.html',{'person':person})

def handle_uploaded_file(f):  
    with open('cv/media/pics/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  