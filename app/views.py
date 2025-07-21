from django.shortcuts import render, redirect
from .models import Car, Category
from .forms import *

def index_view(request):
    cars = Car.objects.all()
    return render(request, 'app/index.html', {'cars': cars})

def detail_view(request, name):
    car = Car.objects.get(name=name)
    return render(request, 'app/detail_view.html', {'car': car})

def add_car(request):
    form = carForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index_view')
        else:
            form = carForm()
    return render(request, 'app/add_car.html', {'form': form})

def delete_car(request, car_id):
    car = Car.objects.get(id=car_id)
    if car:
        car.delete()
        return redirect('index_view')
    return render(request)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Car, Category

def edit_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    categories = Category.objects.all()

    if request.method == 'POST':
        car.name = request.POST.get('name')
        car.model = request.POST.get('model')
        car.year = request.POST.get('year')
        car.price = request.POST.get('price')
        car.description = request.POST.get('description')

        category_id = request.POST.get('category')
        car.category = Category.objects.get(id=category_id)

        # Handle image if user uploaded new one
        if 'image' in request.FILES:
            car.image = request.FILES['image']

        car.save()
        return redirect('detail_view', name=car.name)

    return render(request, 'app/edit_car.html', {
        'car': car,
        'categories': categories
    })


