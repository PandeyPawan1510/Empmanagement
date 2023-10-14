from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import IncomeModel
# Create your views here.

def addincome(request):
    if request.method=="POST":
        amt=request.POST.get("amt")
        type=request.POST.get("type")
        desc=request.POST.get("description")
        date=request.POST.get("date")
        uid=request.session.get("_auth_user_id")
        obj=User.objects.get(id=uid)

        obji=IncomeModel()
        obji.income_amount=amt
        obji.income_type=type
        obji.income_date = date
        obji.income_description = desc
        obji.User=obj
        obji.save()
        return redirect("/")
    else:
        return render(request,"incomeform.html")

def list(request):
    uid=request.session.get("_auth_user_id")
    obj=User.objects.get(id=uid)
    data=IncomeModel.objects.filter(User=obj)
    d={
        "data":data
    }
    return render(request,"incdetails.html",d)


