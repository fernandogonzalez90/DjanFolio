from django.shortcuts import render
from portfolio.models import Project, Certificaciones


def home(request):
    projects = Project.objects.all()
    cert = Certificaciones.objects.all()
    return render(request, 'home.html', {'projects': projects, 'cert' : cert})
