from django.urls import path
from . import views

urlpatterns = [
    path("", views.getIndex, name="home"),
]