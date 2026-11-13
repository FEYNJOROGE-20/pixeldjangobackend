from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Contact


# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')

        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'register.html')

        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'register.html')

        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            messages.success(request, 'Account created successfully.')
            return redirect('register')

    return render(request, 'register.html')


def home(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'home.html')

        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'home.html')
        
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'home.html')

        else:
            user = User.objects.create_user(
                username=username,
                  email=email,
                    password=password 
                )
            messages.success(request, 'Account created successfully.')
            return redirect('home')
            

    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact_obj = Contact(
            full_name=full_name,
            email=email,
            subject=subject,
            message=message,
        )
        contact_obj.save()
        messages.success(request, 'Thank you for contacting us.')
        return redirect('contact')
    return render(request, 'contact.html')


