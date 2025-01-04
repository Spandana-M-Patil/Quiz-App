from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username):
            messages.error(request, "User not found!")
            return redirect('login/')
        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request, "Invalid password")
            return redirect('login/')
        else:
            login(request, user)
            return redirect('/home/')

    return render(request, 'authenticate/login.html')

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "User name already taken!")
            return redirect('/')
        
        user = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = username
            )
        
        user.set_password(password)
        user.save()

        messages.info(request, 'Account has been created!')
        return redirect('login/')
    else:
        return render(request, 'authenticate/register.html')



