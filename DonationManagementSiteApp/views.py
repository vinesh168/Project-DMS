from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.db import connection
import os


# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')


def loginOptions(request):
    return render(request, 'loginOptions.html')


def signup_page(request):
    return render(request, 'signup.html')


def signed_up(request):
    username = request.POST['user-name']
    phonenumber = request.POST['user-phone-number']
    email = request.POST['user-email']
    password = request.POST['user-password']

    aadhar_image = request.FILES['user-aadhar-image']
    fss = FileSystemStorage()
    file = fss.save(aadhar_image.name, aadhar_image)
    aadhar_image_path = fss.url(file)

    address = request.POST['user-address']

    cursor = connection.cursor()
    query1 = "select * from volunteer where email= '" + email + "'"
    cursor.execute(query1)
    data = cursor.fetchall()

    if len(data) > 0:

        return render(request, 'Unsuccessfulpopup.html')

    else:

        query2 = "insert into volunteer (username, phonenumber, email, password, aadhar_image_path, address) values (%s, %s, %s, %s, %s, %s)"
        values2 = (username, phonenumber, email, password, aadhar_image_path, address)
        cursor.execute(query2, values2)
        return render(request, 'Successfulpopup.html')


def loged_in(request):
    email = request.POST['email']
    password = request.POST['password']

    cursor = connection.cursor()
    query1 = "select * from volunteer where email= '" + email + "'"
    cursor.execute(query1)
    data = cursor.fetchone()

    if data is not None:
        if email == data[3] and password == data[4]:
            data = {"username": data[1], "image": data[5]}
            return render(request, 'dashboard.html', data)
        else:
            return render(request, 'Unsuccessfulpopup.html')
    else:
        return render(request, 'Unsuccessfulpopup.html')
