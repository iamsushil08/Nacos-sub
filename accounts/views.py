from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def register_view(request):
    return render(request, "accounts/register.html")

def login_view(request):
    return render(request, "accounts/login.html")
def logout_view(request):
    return render(request,"accounts/logot.html")