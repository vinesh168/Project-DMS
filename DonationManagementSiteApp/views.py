from django.shortcuts import render
from django.db import connection

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')


def loginOptions(request):
    return render(request, 'loginOptions.html')


def signup_page(request):
    return render(request, 'signup.html')


def signed_up(request):

    username = request.GET['user-name']
    phonenumber = request.GET['user-phone-number']
    email = request.GET['user-email']
    password = request.GET['user-password']
    aadhar_image = request.GET['user-aadhar-image']
    address = request.GET['user-address']

    cursor = connection.cursor()
    query1 = "select * from volunteer where email= '" + email + "'"
    cursor.execute(query1)
    data = cursor.fetchall()

    if len(data) > 0:

        return render(request, 'Unsuccessfulpopup.html')

    else:

        query2 = "insert into volunteer (username, phonenumber, email, password, aadharimage, address) values (%s, %s, %s, %s)"
        values2 = (username, phonenumber, email, password, LOAD_FILE('aadhar_image'), address)
        cursor.execute(query2, values2)
        return render(request, "Successfulpopup.html")

