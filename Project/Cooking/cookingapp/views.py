from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RecetteForm
from . import models
from django import forms


def ajout(request):
    submitted = False
    if request.method == "POST":
        form = RecetteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            form = RecetteForm
            if 'submitted' in request.GET:
             submitted = True
    return render(request, 'cookingapp/ajout.html', {"form": form})


def index(request):
    return render(request, 'cookingapp/index.html')


def main(request):
    return render(request, 'cookingapp/main.html')


def liste(request):
    return render(request, 'cookingapp/liste.html')
