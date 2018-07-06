from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import RegistrationForm

from django.contrib.auth.models import User

def signup(request):

    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('hello/')

    else:
        form = RegistrationForm()

    return render(request, 'signuppage.html', {'form':form})


def hello(request):
    return render(request, 'hello.html')

def profile(request):
    return render(request, 'profile.html', {'user': request.user})

def user(request):
    return render(request, 'newuser.html')