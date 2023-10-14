from django.urls import path
from . import views as v
urlpatterns=[
    path("/addUser",v.addUser,name="add"),
    path("/Login",v.userlogin,name="log"),
    path("/Logout",v.logot,name="logot"),
    path("/search",v.srch,name="srch")

]