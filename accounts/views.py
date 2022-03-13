from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalied details")
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method=="POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name already exisit")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"mailid already exisit")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password,email=email)
                user.save()
                messages.info(request,"user created")
        else:
            messages.info(request,"password not matched")
            return  redirect('register')
        return redirect('/')
    else:

        return render(request,'registration.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

