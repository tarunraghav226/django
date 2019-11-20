from django.shortcuts import render
from home.models import Item,User
from math import ceil
from django.shortcuts import redirect
# Create your views here.
#function for creating items in slider
def slider(data,category=None):
    carousel=[]
    noData=0
    j=0

    #logic for creating slider if no category is given
    carousel.append([])
    for i in data:
        if noData%4==0:
            carousel[0].append([])
            j+=1
        carousel[0][j-1].append(i)
        noData+=1
    #logic for creating slider when category is given
    if category!=None:
        for cat in category:
            noData=0
            j=0
            carousel.append([])
            for i in data:
                if i.cate==cat or i.gender==cat:
                    if noData%4==0:
                        carousel[len(carousel)-1].append([])
                        j+=1
                    carousel[len(carousel)-1][j-1].append(i)
                    noData+=1                                                                                                                                  
    return carousel
        

def show(request):
    data=Item.objects.all()
    carousel=slider(data,category=('Electronics','Clothing'))
    info={'data':carousel,'slides':range(1,len(carousel[0]))}
    print(len(carousel),carousel)
    return render(request,'home.html',info)

def check(request):
    return render(request,'login-register.html')

def login(request):
    username='not a valid user'
    
    if request.method=='POST':
        pass

    return render(request,'base.html')

def register(request):
    return render(request,'register.html') 

def validate(request):
    if request.method=='POST':
        user=User()
        user.firstName=request.POST.get('first_name')
        user.lastName=request.POST.get('last_name')
        user.email=request.POST.get('email')
        user.password=request.POST.get('password')
        user.save()
        return redirect('/login/')
    return render(request,'/register.html/')