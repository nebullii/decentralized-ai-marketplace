import os
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

User = get_user_model()

@csrf_exempt
def google_auth(request):
    """ Handles Google OAuth authentication """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            token = data.get("token")

            # Verify the Google token
            google_url = f"https://oauth2.googleapis.com/tokeninfo?id_token={token}"
            response = requests.get(google_url)
            user_data = response.json()

            if "email" in user_data:
                user, created = User.objects.get_or_create(
                    username=user_data["email"],
                    defaults={"email": user_data["email"]}
                )
                login(request, user)
                return JsonResponse({"success": True})

            return JsonResponse({"success": False, "error": "Invalid token"}, status=400)
        
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)

    return JsonResponse({"success": False}, status=400)

def login_view(request):
    """ Handles user login with authentication and validation. """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('profile')  # Redirect to profile after login
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    """Handles user signup and validation."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")  
            password1 = form.cleaned_data.get("password1")  

            # Check if user already exists BEFORE creating a user
            if User.objects.filter(username=username).exists():
                messages.error(request, "A user with that username already exists.")
            else:
                user = form.save(commit=False)  # Create user but do NOT save to DB yet
                user.set_password(password1)  # Ensure password is hashed
                user.save()  # Now save to DB
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, "Your account has been created successfully!")
                return redirect('profile')  # Redirect to profile after signup
        else:
            messages.error(request, "Please correct the errors below.")

    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'profile.html')

@login_required
def logout_view(request):
    """ Handles user logout and redirects to the home page. """
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')
