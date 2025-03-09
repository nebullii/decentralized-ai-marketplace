from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('google-auth/', views.google_auth, name='google-auth'),  # Backend for Google Sign-In
    path("wallet-login/", views.wallet_login, name="wallet-login")
]
