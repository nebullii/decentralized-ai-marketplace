from django.contrib import admin
from django.urls import path, include
from users.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Include allauth URLs
    path('', home_view, name='home'), # Home Page
]
