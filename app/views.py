from django.shortcuts import render
from .models import Car, Category

def index_view(request):
    cars = Car.objects.all()
    return render(request, 'app/index.html', {'cars': cars})

def detail_view(request, name):
    car = Car.objects.get(name=name)
    return render(request, 'app/detail.html', {'car': car})
