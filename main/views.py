from django.shortcuts import render

def getIndex(request):
    return render(request, "main/index.html")

def getCourses(request):
    data = [
        {"Name": "C++" , "Price": "1000"},
        {"Name": "C" , "Price": "4000"},
        {"Name": "C#" , "Price": "3000"},
        {"Name": "JS" , "Price": "2000"},
    ]
    return render(request, "main/courses.html", {"courses": data})
