from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import ExpenseModel
# Create your views here.
def addexpense(request):
    if request.method=="POST":
        amt=request.POST.get("amt")
        type=request.POST.get("type")
        desc=request.POST.get("description")
        date=request.POST.get("date")
        uid=request.session.get("_auth_user_id")
        obj=User.objects.get(id=uid)

        obji=ExpenseModel()
        obji.expense_amount=amt
        obji.expense_type=type
        obji.expense_date = date
        obji.expense_description = desc
        obji.User=obj
        obji.save()
        return redirect("/")
    else:
        return render(request,"expenseform.html")

def list(request):
    uid=request.session.get("_auth_user_id")
    obj=User.objects.get(id=uid)
    data=ExpenseModel.objects.filter(User=obj)
    d={
        "data":data
    }
    return render(request,"expdetails.html",d)





