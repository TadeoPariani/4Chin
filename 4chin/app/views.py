from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User(username=username, email=email, password=password)
        user.save()
        return redirect('home')  
    return render(request, 'app/register.html')


def login(request):
    if request.method == 'POST':
        try:
            usernameLogin = request.POST['username']
            passwordLogin = request.POST['password']
            user = User.objects.get(username=usernameLogin)
            if passwordLogin == user.password:
                return redirect('home')  
        except:
            Status = True
            context = {
                "Status": Status
            }
            return render(request, 'app/login.html', context)
    return render(request, 'app/login.html')


def user_list(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'app/index.html', context)