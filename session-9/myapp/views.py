from django.shortcuts import render
from .models import Skills, About,  Project

def home(request):
    projects = Project.objects.all()
    skills = Skills.objects.all()
    about = About.objects.first()

    context = {'projects': projects, 'skills': skills, 'about': about}
    return render(request, 'home.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'project_detail.html', {'project': project})
