
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import messages
# Create your views here.


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username and password.')
            messages.info(request, 'Please enter valid information.')
            return redirect('signin')


def signout(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
            messages.info(request, 'Account already exist.')

        except User.DoesNotExist:
            User.objects.create(username=username,
                                email=email, password=password)

            # :::::::::::::::Sending mail:::::::::::::::::
            send_mail(
                'Account created',
                f'Your account has been created. Your username is {username}.',
                settings.EMAIL_HOST_USER,
                ['email', 'kabinbasnet77@gmail.com'],
                fail_silently=False,
            )

            messages.success(request, 'Account Created.')
            messages.success(request, 'Please Login.')

        return redirect('signin')
