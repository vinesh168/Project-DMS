"""Donation_management URL Configuration

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
import Donar.views
from django.urls import path
from Donar.views import Donarsignup,Donarsignin,Donarverify,donordashboard,donatenow,profile,updateProfile,logout,editprofile



urlpatterns = [
    path('Donarsignup', Donarsignup),
    path('Donarsignin', Donarsignin),
    path('Donarverify', Donarverify),
    path('donordashboard', donordashboard),
    path('donatenow', donatenow),
    path('profile', profile),
    path('editprofile', editprofile),
    path('updateProfile', updateProfile),
    path('logout', logout),
]
