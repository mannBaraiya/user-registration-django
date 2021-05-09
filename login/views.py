from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django import forms

from django.contrib import messages

# It is always better to put your forms in a seperate file
class CreateUserForm (UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


#views
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(user)
        else:
            redirect('login') # Put your home page screen

    return render(request, 'login/login.html', {})

def registration(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('login')

    context = {'form':form}
    return render(request, 'login/register.html', context)

# Create your views here.
