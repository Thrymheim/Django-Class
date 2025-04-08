from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Laptop, Feedback
from .forms import FeedbackForm


def login_view(request):
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
def laptop_detail(request, pk):  # Changed laptop_id to pk
    laptop = get_object_or_404(Laptop, pk=pk)  # Changed id to pk
    return render(request, 'laptop_detail.html', {'laptop': laptop})

@login_required
def add_feedback(request, pk):  # Changed laptop_id to pk
    laptop = get_object_or_404(Laptop, pk=pk)  # Changed id to pk

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.laptop = laptop
            feedback.save()
            return redirect('laptop_detail', pk=laptop.pk)  # Changed id to pk
    else:
        form = FeedbackForm()

    return render(request, 'feedback_form.html', {
        'form': form,
        'laptop': laptop
    })