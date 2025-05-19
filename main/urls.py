from django.urls import path
from . import views

urlpatterns = [
    path("", views.getIndex, name="home"),
     path("/add", views.getAdd, name="add"),
]