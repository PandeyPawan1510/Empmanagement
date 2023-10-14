

from django.contrib import admin
from django.urls import path,include
from account.views import home

urlpatterns = [
    path('admin/',admin.site.urls),
    path("",home),
    path("Account",include(("account.urls","account"),namespace="acc")),
    path("Income",include(("income.urls","income"),namespace="inc")),
    path("Expense", include(("expense.urls","expense"),namespace="exp"))
]
