"""DonationManagementSite URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from DonationManagementSiteApp.views import homepage, loginOptions, signup_page, vol_signed_up, vol_loged_in, vol_profile_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage', homepage),
    path('loginOptions', loginOptions),
    path('signup-page', signup_page),
    path('vol-signed-up', vol_signed_up),
    path('dashboard', vol_loged_in),
    path('Profile', vol_profile_info),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
