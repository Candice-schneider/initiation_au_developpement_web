from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LivreForm
from .models import models


def ajout(request):
    if request.method == "POST":
        form = LivreForm(request)
        if form.is_valid():  # validation du formulaire.
            livre = form.save()  # sauvegarde dans la base
            return render(request, "Mybiblio/affiche.html", {"livre": livre})
            # envoie vers une page d'affichage du livre créé
        else:
            return render(request, "Mybiblio/ajout.html", {"form": form})
    else:
        form = LivreForm()  # création d'un formulaire vide
        return render(request, "Mybiblio/ajout.html", {"form": form})


def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save(commit=False)
        livre.id = id,
        livre.save()
        return HttpResponseRedirect("/Mybiblio")
    else:
        return render(request, "Mybiblio/ajout.html", {"form": lform, "id": id})


def index(request):
    liste = list(models.Livre.objects.all())


def affiche(request, id):
    livre = models.Livre.objects.get(pk=id)
    return render(request, "Mybiblio/affiche.html", {"livre": livre})
