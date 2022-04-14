from django.shortcuts import render
from django.db import connection
# Create your views here.
from django.template import RequestContext



def Donarsignup(request):
    return render(request,"donor_signup.html")


def Donarsignin(request):
    email=request.GET["email"]
    Password=request.GET["psw"]
    cursor=connection.cursor()
    Query="select * from Donar where email='"+email+"'"
    cursor.execute(Query)
    data=cursor.fetchall()
    if len(data)>0:
        data={"email":"Already exist! use another email id."}
        return render(request,"donunsuccesfulpopup.html",data)
    else:
        FirstName=request.GET["fname"]
        LastName=request.GET["lname"]
        Mobile=request.GET["mob"]
        Address=request.GET["Add"]
        cursor=connection.cursor()
        Query1="insert into Donar(FirstName,LastName,email,mobile,Pass,address) values (%s,%s,%s,%s,%s,%s)"
        value=(FirstName,LastName,email,Mobile,Password,Address)
        cursor.execute(Query1,value)
        query3 = "insert into dashboard (email) values ('" + email + "')"
        cursor.execute(query3)
        return render(request,"donsuccessfulpopup.html")

def Donarverify(request):
    email=request.GET["email"]
    psw=request.GET["password"]
    cursor=connection.cursor()
    Query2="select email,pass,FirstName,LastName from Donar where email='"+email+"'"
    cursor.execute(Query2)
    data=cursor.fetchall()
    if len(data)==0:
        data={"email":"Donar doesn't exist"}
        return render(request,"donunsuccesfulpopup.html",data)

    else:
        if email==data[0][0] and psw==data[0][1]:
            global val
            def val():
                return data[0][0]
            fname=data[0][2]
            lname=data[0][3]
            query3 = "select * from dashboard where email='"+email+"'"
            cursor.execute(query3)
            das_data = cursor.fetchall()
            totaldon=das_data[0][1]
            acceptdon=das_data[0][2]
            rejectdon=das_data[0][3]
            pendingdon=das_data[0][4]
            successdon=das_data[0][5]
            d_data={"fname":fname,"lname":lname,"tdon":totaldon,"accdon":acceptdon,"rejdon":rejectdon,"pendon":pendingdon,"sucdon":successdon}
            return render(request,"donordashboard.html",d_data)
        else:
            data = {"email": "Donar doesn't exist"}
            return render(request, "donunsuccesfulpopup.html", data)

def donordashboard(request):
    glo_email=val()
    cursor = connection.cursor()
    Query4 = "select * from dashboard left join donar on dashboard.email=donar.email where dashboard.email='"+glo_email+"'"
    cursor.execute(Query4)
    data = cursor.fetchall()
    totaldon = data[0][1]
    acceptdon = data[0][2]
    rejectdon = data[0][3]
    pendingdon = data[0][4]
    successdon = data[0][5]
    fname=data[0][8]
    lname=data[0][9]
    d_data = {"fname": fname, "lname": lname, "tdon": totaldon, "accdon": acceptdon, "rejdon": rejectdon,
              "pendon": pendingdon, "sucdon": successdon}
    return render(request, "donordashboard.html", d_data)
def donatenow(request):
    return render(request, "donate_now.html")
def logout(request):
    return render(request, "Donor_login.html")
def profile(request):
    glo_email = val()
    cursor = connection.cursor()
    Query2 = "select FirstName,LastName,email,mobile,address from Donar where email='"+glo_email+"'"
    cursor.execute(Query2)
    data = cursor.fetchall()
    fname = data[0][0]
    lname = data[0][1]
    email = data[0][2]
    mobile = data[0][3]
    address=data[0][4]
    pro_data={"fname": fname, "lname": lname,"email":email,"mobile":mobile,"address":address}
    return render(request, "profile.html",pro_data)

def editprofile(request):
    glo_email = val()
    cursor = connection.cursor()
    Query2 = "select FirstName,LastName,email,mobile,address from Donar where email='"+glo_email+"'"
    cursor.execute(Query2)
    data = cursor.fetchall()
    fname = data[0][0]
    lname = data[0][1]
    email = data[0][2]
    mobile = data[0][3]
    address=data[0][4]
    pro_data={"fname": fname, "lname": lname,"email":email,"mobile":mobile,"address":address}
    return render(request, "editprofile.html",pro_data)


def updateProfile(request):
    glo_email = val()
    fname = request.GET["fname"]
    lname = request.GET["lname"]
    email = request.GET["email"]
    mob = request.GET["contact"]
    add = request.GET["Add"]
    cursor = connection.cursor()
    Query5 = "update donar set FirstName='"+fname+"',LastName='"+lname+"',email='"+email+"',mobile='"+mob+"',address='"+add+"' where email='"+glo_email+"'"
    Query6 = "update dashboard set email='"+email+"' where email='"+glo_email+"'"
    cursor.execute(Query5)
    cursor.execute(Query6)
    dic={"email":"Your profile is successfully updated."}
    return render(request, "donsuccessfulpopup.html",dic)

