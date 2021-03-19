from django.shortcuts import render,redirect
from .models import User,Admin
import mysql.connector
from operator import itemgetter
from django.contrib import messages

# Create your views here.
def welcome(req):
    return render(req,'welcome.html')
def login(req):
    con = mysql.connector.connect(host='localhost', user='root', password='', database='login')
    cursor = con.cursor()
    con2 = mysql.connector.connect(host='localhost', user='root', password='', database='login')
    cursor2 = con2.cursor()

    sqlcommand = "select uname from loginapp_user"
    sqlcommand = "select psd from loginapp_user"

    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand)


    e = []
    p = []

    for i in cursor:
        e.append(i)
    for j in cursor2:
        p.append(j)

    res=list(map(itemgetter(0),e))
    res2 = list(map(itemgetter(0), p))


    if req.method == "POST":
        uname = req.POST['uname']
        psd = req.POST['psd']
        i=1
        k=len(res)
        while i<k:
            if res[i]==uname and res2[i]==psd:
                return render(req,'welcome.html',{'uname':uname})
                break
            i+=1
        else:
            messages.info(req,'check username or password')
            return redirect('login')

    return render(req,'login.html')
def register(req):
    if req.method=="POST":
        user=User()

        user.fname=req.POST['fname']
        user.lname =req.POST['lname']
        user.uname = req.POST['uname']
        user.psd = req.POST['psd']
        if user.fname=='' or user.lname=='':
            messages.info(req,'some fields are empty')
            return redirect('register')
        else:
            user.save()

    return render(req,'register.html')