from django.shortcuts import render
from .models import Receipt

def getIndex(request):
    data = Receipt.objects.all()
    return render(request, "main/index.html", {"data": data})

