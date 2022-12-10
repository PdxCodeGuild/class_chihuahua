from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def user_register(request):
    if request.method == "POST":
        new_user = User.objects.create(
            username = request.POST['username'],
            email = request.POST['email']

        )
        new_user.set_password(request.POST['password'])
        new_user.save()
        messages.success(request, 'User Registered!')
        return redirect('login')
    return render(request, 'register/register.html')



def user_login(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is not None:
            login(request,user)
            messages.success(request, 'User successfully logged in!')
            return redirect('about')
        elif user is None:
            messages.info(request, 'User does not exist!')
                
    return render(request, 'register/login.html')



def user_logout(request):
    logout(request)
    return redirect('home')