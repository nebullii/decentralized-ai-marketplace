from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')

@login_required
def profile_view(request):
    return render(request, 'profile.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
