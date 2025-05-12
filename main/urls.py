from django.urls import path
from . import views

urlpatterns = [
    path("", views.getIndex, name="home"),
    path("courses/", views.getCourses, name="courses"),
]