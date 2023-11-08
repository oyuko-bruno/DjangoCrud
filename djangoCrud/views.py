from django.shortcuts import redirect,render
from  django.contrib.auth.models import  User
from django.contrib.auth import authenticate,login,logout
from .models import Student

def home(request):
    data=Student.objects.all()
    return  render(request, f'index.html', {'data' : data} )

def insertData(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        age=request.POST.get("age")
        #  gender=request.POST.get("gender")
        hifadhi=Student(name=name,email=email,age=age)

        hifadhi.save()
        return redirect('/')
    else:
        return render(request, 'index.html')

def updateData(request,id):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        age=request.POST.get("age")
        #  gender=request.POST.get("gender")

        rekebisha= Student.objects.get(id=id)
        rekebisha.name=name
        rekebisha.email=email
        rekebisha.age=age
        #  rekebisha.gender=gender
        rekebisha.save()
        return redirect('/')
    else:
        d=Student.objects.get(id=id)
        return render(request,'edit.html',{'d':d})

def delete(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    return redirect('/')

def handlesignup(request):
    if request.method== 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")

        myuser=User.objects.create_user(username,password)
        myuser.save()
    return  render(request,'signup.html')

def handlelogin(request):
    if request.method== 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")

        myuser=authenticate(username=username,password=password)

        if myuser is not None:
            login(request,myuser)
            return redirect('/')
        else:
            return redirect('/login')

    return  render(request,'login.html')

def handlelogout(request):
    logout(request)
    return  redirect('/signup') 