from django.shortcuts import render,redirect
from django.contrib.auth.models import  User
from income.models import IncomeModel
from expense.models import ExpenseModel


# Create your views here.
def home(request):
    return render(request,"home.html")

def addUser(request):
    if request.method == "POST":
        uname=request.POST.get("username")
        uemail=request.POST.get("email")
        upassword=request.POST.get("password")
        obj=User()
        obj.username=uname
        obj.email=uemail
        obj.set_password(upassword)
        obj.save()
        return redirect("/Account/addUser")

    return render(request,"form.html")

from django.contrib.auth import login,logout,authenticate
def userlogin(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        pswd=request.POST.get("password")
        user=authenticate(request,username=uname,password=pswd)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            d={"msg":"invalid username and password bro"}
            return render(request,"login.html",d)
    else:
        return render(request,"login.html")
def logot(request):
    logout(request)
    return redirect("/")

def srch(request):
    uid=request.session.get("_auth_user_id")
    obj=User.objects.get(id=uid)
    srchdata=request.GET.get("srch")
    datai=IncomeModel.objects.filter(income_description__contains=srchdata,User=obj)
    datae = ExpenseModel.objects.filter(expense_description__contains=srchdata,User=obj)

    d={
        "data1":datai,
        "data2": datae
    }
    return render(request,"srch.html",d)
