from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Project
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})


@login_required
def salir(request):
    logout(request)
    return redirect('/')

def profile(request):

    projects = Project.objects.all()
    return render(request, 'profile.html', {'projects': projects})
