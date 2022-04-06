import sys

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, HttpResponse
from django.db import connection
from .models import Volunteer
import os

val = None


# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')


def loginOptions(request):
    return render(request, 'loginOptions.html')


def signup_page(request):
    return render(request, 'signup.html')


def vol_signed_up(request):
    username = request.POST['user-name']
    phonenumber = request.POST['user-phone-number']
    email = request.POST['user-email']

    cursor = connection.cursor()
    query1 = "select * from donationmanagementsiteapp_volunteer where email= '" + email + "'"
    cursor.execute(query1)
    data = cursor.fetchall()

    if len(data) > 0:
        return render(request, 'Unsuccessfulpopup.html')
        sys.exit()

    else:
        password = request.POST['user-password']

        aadhar_image = request.FILES['user-aadhar-image']
        fss = FileSystemStorage()
        file = fss.save(aadhar_image.name, aadhar_image)  # this is for saving image in media folder
        aadhar_image_path = fss.url(file)  # this is for getting image path

        address = request.POST['user-address']
        city = request.POST['city-name']
        state = request.POST['state-name']

        new_volunteer = Volunteer(username=username, phonenumber=phonenumber, email=email, password=password,
                                  aadhar_image_path=aadhar_image_path, address=address, city=city, state=state)
        new_volunteer.save()

        return render(request, 'Successfulpopup.html')


def vol_loged_in(request):
    email = request.POST['email']
    password = request.POST['password']

    cursor = connection.cursor()
    query1 = "select * from donationmanagementsiteapp_volunteer where email= '" + email + "'"
    cursor.execute(query1)
    data = cursor.fetchone()

    if data is not None:
        if password == data[4]:
            global val

            def val():
                return email

            data = {"username": data[1]}
            return render(request, 'dashboard.html', data)
        else:
            return HttpResponse('Your password is wrong')


def vol_profile_info(request):
    gl_email = val()

    cursor = connection.cursor()
    query1 = "select * from donationmanagementsiteapp_volunteer where email= '" + gl_email + "'"
    cursor.execute(query1)
    data = cursor.fetchone()
    if data is not None:
        return HttpResponse('hello')
    else:
        return HttpResponse('no data')
