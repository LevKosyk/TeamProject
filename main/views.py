<<<<<<< HEAD
from django.shortcuts import render, redirect
from .models import Student, Comment
from .forms import StudentForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


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
    query = request.GET.get('q', '')
    grade_filter = request.GET.get('grade', '')

    student_list = Student.objects.all()
    if query:
        student_list = student_list.filter(name__icontains=query)
    if grade_filter:
        student_list = student_list.filter(grade__icontains=grade_filter)

    paginator = Paginator(student_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    grades = Student.objects.values_list('grade', flat=True).distinct()
    return render(request, "main/index.html", {
        "page_obj": page_obj,
        "query": query,
        "grade_filter": grade_filter,
        "grades": grades,
    })

def student_details(request, pk):
    student = Student.objects.get(pk=pk)
    error = None

    if request.method == "POST":
        text = request.POST.get('text', '').strip()
        if text:
            Comment.objects.create(name=request.user.username, text=text, user=student)
            return redirect('details', pk=student.pk)
        else:
            error = "Both name and comment are required."

    return render(request, 'main/details.html', {
        'student': student,
        'error': error,
    })

@login_required
def getAdd(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
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
            return redirect('login')
        
        return render(request, 'main/register.html', {'error': "Passwords are different"})


    return render(request, 'main/register.html')

@login_required
def logOut(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    user = request.user
    try:
        student = Student.objects.get(name=user.username)
        comments = Comment.objects.filter(user=student)
    except Student.DoesNotExist:
        student = None
        comments = Comment.objects.none()
    return render(request, 'main/profile.html', {'user': user, 'student': student, 'comments': comments})

@login_required
def editProfile(request):
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        return redirect('profile')
    return render(request, 'main/editProfile.html', {'user': request.user})
=======
from django.shortcuts import render, redirect
from .models import Student, Comment
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

def student_details(request, pk):
    student = Student.objects.get(pk=pk)
    error = None

    if request.method == "POST":
        text = request.POST.get('text', '').strip()
        if text:
            Comment.objects.create(name=request.user.username, text=text, user=student)
            return redirect('details', pk=student.pk)
        else:
            error = "Both name and comment are required."

    return render(request, 'main/details.html', {
        'student': student,
        'error': error,
    })

@login_required
def getAdd(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
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
            return redirect('login')
        
        return render(request, 'main/register.html', {'error': "Passwords are different"})


    return render(request, 'main/register.html')

@login_required
def logOut(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    user = request.user
    try:
        student = Student.objects.get(name=user.username)
        comments = Comment.objects.filter(user=student)
    except Student.DoesNotExist:
        student = None
        comments = Comment.objects.none()
    return render(request, 'main/profile.html', {'user': user, 'student': student, 'comments': comments})

@login_required
def editProfile(request):
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        return redirect('profile')
    return render(request, 'main/editProfile.html', {'user': request.user})
>>>>>>> 5984854642474ac2632e85ce90862a14376f31fe
