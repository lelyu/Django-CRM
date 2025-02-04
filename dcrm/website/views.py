from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    # check to see if user is logging in
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # authenticate
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, 'User is logged in.')
            return redirect('home')
        else:
            messages.success(request, 'There was an error. Try again.')
            return redirect('home')
    return render(request, 'home.html', {})
    
def login_user(request):
    pass


def logout_user(request):
    pass


