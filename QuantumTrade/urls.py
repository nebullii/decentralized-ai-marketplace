from django.contrib import admin
from django.urls import path, include
from .views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Includes Google authentication URLs
    path('users/', include('users.urls')), 
    path('marketplace/', include('marketplace.urls')),
]
