from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import HttpResponseNotFound

def hello(request):
    return HttpResponse("Hello, world! This is my first Django view.")

def greet(request):
    name = "Maziyar"  # Hardcoded name
    last_name = "kolagar"
    age = 20
    city = "Babol"
    return HttpResponse(f"Hello, I'm {name} {last_name} and im {age} yeas old and i live in {city}")

#Dynamic greet - tell class to dynamic it with name, lastname, age and city
def dynamicGreet(request, name, lastname, age, city):
    return HttpResponse(f"Hello, {name} {lastname} {age} {city}! Welcome to Django.")

#Class
def current_time(request):
    now = datetime.now()
    return HttpResponse(f"The current date and time is: {now}")
#Class
def list_items(request):
    items = ["Apple", "Banana", "Cherry"]
    items_text = "Here is a list of items:\n"
    for item in items:
        items_text += f"- {item}\n"
    return HttpResponse(items_text)


def custom_404(request, exception=None):
    return HttpResponseNotFound("Oops! The page you're looking for doesn't exist. Please check the URL and try again.")