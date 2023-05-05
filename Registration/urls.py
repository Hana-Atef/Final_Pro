"""Registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from project.views import home, RegisterView ,CustomLoginView, RegisterAPI, LoginAPI
from knox import views as knox_views 
from project.forms import LoginForm
from django.urls import path, include
from django.urls import re_path
from project import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name="home"),
    # path('register/', RegisterView.as_view(), name='register'), 
    path('api/register/', RegisterAPI.as_view(), name='register'),
    # path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login.html',authentication_form=LoginForm), name='login'),
    # path('patient/',views.PatientData,name='patient'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    
    ]
# re_path(r'^oauth/', include('social_django.urls', namespace='social')),
