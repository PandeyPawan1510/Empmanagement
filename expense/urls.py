from django.urls import path
from .import views as v
urlpatterns = [
    path("/Add",v.addexpense,name="add"),
    path("/List",v.list,name="list")

]