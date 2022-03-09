from django.shortcuts import render, redirect
from profile_app.forms import PersonForm
from django.contrib import messages
from profile_app.models import Person
# Create your views here.


def PP(request):
    if request.method == 'GET':
        form = PersonForm()
        return render(request, 'pp.html', {'form': form})
    else:
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('home')
        else:
            messages.error(request, 'Error Occur')
            messages.info(
                request, 'Please enter the correct value in required place.')
            return render(request, 'pp.html', {'form': form})


def home(request):
    person = Person.objects.all()[0]
    return render(request, 'home.html', {'person': person})


def signin(request):
    return render(request, 'signin.html')


def signout(request):
    return render(request, 'signout.html')


def register(request):
    return render(request, 'register.html')
