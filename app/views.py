from django.shortcuts import render, redirect, get_object_or_404
from .models import Car, Category
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import  UserCreationForm

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
            car = form.save(commit=False)
            car.user = request.user
            car.save()
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

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully')
            login(request, user)  # Auto login after registration
            return redirect('index_view')

        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f"{error}")


    form = UserCreationForm()
    return render(request, 'app/user_register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index_view')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'app/user_login.html')

def user_logout(request):
    logout(request)
    messages.success(request,"You logged out successfully")
    return redirect("index_view")





