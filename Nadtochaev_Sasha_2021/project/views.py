from django.shortcuts import render
from .models import Project

def project_page(request):
    return render(request, 'Project_app.html')

def project_index(request):
    projects = Project.objects.all()
    context = {'proecty':projects}
    return render(request, 'project_index.html', context)

def project_detai(request, pk):
    project = Project.objects.get(pk=pk)
    context = {'proect':project}
    return render(request, 'project_detail.html', context)