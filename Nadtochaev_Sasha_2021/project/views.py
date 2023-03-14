from django.shortcuts import render

def project_page(request):
    return render(request, 'Project_app.html')
