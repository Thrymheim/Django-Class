from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def services(request):
    services = [
        {"name": "Web Design", "description": "We create beautiful websites."},
        {"name": "SEO", "description": "We help you rank higher on Google."},
        {"name": "Marketing", "description": "We promote your business online."},
    ]
    return render(request, 'services.html', {'services': services})

def contact(request):
    return render(request, 'contact.html')