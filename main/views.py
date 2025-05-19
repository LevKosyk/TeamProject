from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def getIndex(request):
    data = Student.objects.all()
    return render(request, "main/index.html", {"data": data})


def getAdd(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        form.save()
        return redirect('/')

    form = StudentForm()
    return render(request, "main/form.html", {'form': form})
