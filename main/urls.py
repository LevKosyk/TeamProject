from django.urls import path
from . import views

urlpatterns = [
    path("", views.getIndex, name="home"),
     path("/add", views.getAdd, name="add"),
     path("<int:pk>", views.StudentDetailsView.as_view(), name="details"),
      path("<int:pk>/update", views.StudentUpdateView.as_view(), name="update"),
       path("<int:pk>/delete", views.StudentDeleteView.as_view(), name="delete"),
]