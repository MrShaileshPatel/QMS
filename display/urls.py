"""QMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls.conf import include
from . import views

app_name = 'display'
urlpatterns = [
    #path('admin/', admin.site.urls, 'admin'),
    path('', views.home, name = 'Home'),
    path('display', views.display1, name = 'Display1'),
    path('token_admin', views.token_admin, name = 'Token_Admin'),
    path('create_token', views.home, name = 'home'),
    path('delete_token', views.token_admin, name = 'Token_Admin'),

   
]
