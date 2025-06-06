<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path("", views.getIndex, name="home"),
    path("/add", views.getAdd, name="add"),
   path('<int:pk>', views.student_details, name="details"),
    path("<int:pk>/update", views.StudentUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", views.StudentDeleteView.as_view(), name="delete"),
    path('logIn/', views.logIn, name="logIn"),
    path('logUp/', views.logUp, name="logUp"),
    path('logOut/', views.logOut, name="logOut"),
    path('profile/', views.profile, name="profile"),
    path('edit/', views.editProfile, name="editProfile"),
=======
from django.urls import path
from . import views

urlpatterns = [
    path("", views.getIndex, name="home"),
    path("/add", views.getAdd, name="add"),
   path('<int:pk>', views.student_details, name="details"),
    path("<int:pk>/update", views.StudentUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", views.StudentDeleteView.as_view(), name="delete"),
    path('logIn/', views.logIn, name="logIn"),
    path('logUp/', views.logUp, name="logUp"),
    path('logOut/', views.logOut, name="logOut"),
    path('profile/', views.profile, name="profile"),
    path('edit/', views.editProfile, name="editProfile"),
>>>>>>> 5984854642474ac2632e85ce90862a14376f31fe
]