from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def Home(request):
    return render(request,'facebook.html')

# Create your views here.
def Signup(request):
    if request.method=='POST':
        uname=request.POST.get('fname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        if pass1!=pass2:
            return HttpResponse('Password did not match')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

        


    return render(request,'signup.html')

       
def Login(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        pass1=request.POST.get('password')

        user=authenticate(request,username=uname,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')

        else:
            return HttpResponse('Username or password is not correct')
                



        
         
    return render(request,'login.html')