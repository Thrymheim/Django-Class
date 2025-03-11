from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Laptop


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('signup')


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



def home(request):
    if request.user.is_authenticated:
        laptops = Laptop.objects.all()
        return render(request, 'home.html', {'laptops': laptops})
    else:
        return redirect('login')


@login_required
def add_laptop(request):
    if not request.user.is_staff:
        return redirect('home')

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        Laptop.objects.create(name=name, description=description)
        return redirect('home')
    return render(request, 'add_laptop.html')


@login_required
def edit_laptop(request, pk):
    if not request.user.is_staff:
        return redirect('home')

    laptop = Laptop.objects.get(pk=pk)
    if request.method == 'POST':
        laptop.name = request.POST.get('name')
        laptop.description = request.POST.get('description')
        laptop.save()
        return redirect('home')
    return render(request, 'edit_laptop.html', {'laptop': laptop})


@login_required
def delete_laptop(request, pk):
    if not request.user.is_staff:
        return redirect('home')

    laptop = Laptop.objects.get(pk=pk)
    laptop.delete()
    return redirect('home')
