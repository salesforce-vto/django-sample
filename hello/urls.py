from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("bhanu", views.bhanu, name="bhanu"),
    path("ayush", views.ayush, name="ayush"),

]