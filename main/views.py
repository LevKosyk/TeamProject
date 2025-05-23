from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.views.generic import DetailView, UpdateView, DeleteView


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


def getAdd(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        form.save()
        return redirect('/')

    form = StudentForm()
    return render(request, "main/form.html", {'form': form})
