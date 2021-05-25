from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("bhanu", views.bhanu, name="bhanu"),
    path("ayush", views.ayush, name="ayush"),

]