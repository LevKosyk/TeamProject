from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


class StudentDetailsView(DetailView):
    model = Student
    template_name = "main/details.html"
    context_object_name = "student"


class StudentUpdateView(UpdateView):
    model = Student
    template_name = "main/form.html"
    form_class = StudentForm

class StudentDeleteView(DeleteView):
    model = Student
    success_url = "/"
    template_name = "main/delete.html"


def getIndex(request):
    data = Student.objects.all()
    return render(request, "main/index.html", {"data": data})

@login_required
def getAdd(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        form.save()
        return redirect('/')

    form = StudentForm()
    return render(request, "main/form.html", {'form': form})


def logIn(request):

    if request.method == "POST":

        userName=request.POST['userName']
        userPassword=request.POST['userPass']

        user = authenticate(request, username=userName, password=userPassword)

        if user is not None:
            login(request, user)
            return redirect('home')
    
        return render(request, 'main/login.html', {'error': "Data is not correct"})

    return render(request, 'main/login.html')


def logUp(request):

    if request.method == "POST":

        userName=request.POST['userName']
        userPassword=request.POST['userPass']
        userPassword2=request.POST['userPass2']

        if userPassword == userPassword2:

            user = User.objects.create_user(userName, '', userPassword)
            user.save()

            user = authenticate(request, username=userName, password=userPassword)

            if user is not None:
                login(request, user)
            return redirect('main/index.html')
        
        return render(request, 'main/register.html', {'error': "Passwords are different"})


    return render(request, 'main/register.html')

@login_required
def logOut(request):
    logout(request)
    return redirect('home')
