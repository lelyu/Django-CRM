from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from . import forms

# Home/Login view
def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the email exists and get the associated user
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)  # Authenticate with username
        except User.DoesNotExist:
            user = None

        if user:
            login(request, user)
            messages.success(request, 'User is logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('home')

    return render(request, 'home.html', {})

# Logout view
def logout_user(request):
    logout(request)
    messages.success(request, 'You have logged out.')
    return redirect('home')

# Registration view
def register_user(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            # Authenticate user using the saved username
            user = authenticate(request, username=user.username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Registration successful. You are now logged in.')
                return redirect('home')
    
    else:
        form = forms.SignUpForm()
    
    return render(request, 'register.html', {'form': form})
