from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),  # Default Django admin URL
    path('accounts/', include('allauth.urls')),  # Include allauth URLs for login, logout, etc.
    # Your other URLs...
]