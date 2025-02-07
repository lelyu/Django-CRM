from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from . import forms
from .models import Record

# Home/Login view
def home(request):
    records = Record.objects.all()
    
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
    
    return render(request, 'home.html', {'records': records})

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


# pk: primary key
# get customer_record
def customer_record(request, customer_id):
    if request.user.is_authenticated:
        # look up records
        customer_record = Record.objects.get(id=customer_id)
        return render(request, 'record.html', {'customer_record': customer_record})
    messages.success(request, 'Please login first.')
    return redirect('home')

def delete_record(request, customer_id):
    if request.user.is_authenticated:
        # look up records
        customer_record = Record.objects.get(id=customer_id)
        customer_record.delete()
        return redirect('home')
    messages.success(request, 'Please login first.')
    return redirect('home')


def add_record(request):
    form = forms.AddRecordForm(request.POST)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Record added')
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    messages.success(request, 'Please login first.')
    return redirect('home')


def edit_record(request, customer_id):
    if request.user.is_authenticated:
        # look up records
        curr_record = Record.objects.get(id=customer_id)
        form = forms.AddRecordForm(request.POST or None, instance=curr_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record edited')
            return redirect('home')
        return render(request, 'edit_record.html', {'form': form})
    messages.success(request, 'Please login first.')
    return redirect('home')