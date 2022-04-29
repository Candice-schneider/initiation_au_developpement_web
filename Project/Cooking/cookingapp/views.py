from django.shortcuts import render

# Create your views here.

def ajout(request):
    gform = forms.RecetteForm()
    return render(request, "cookingapp/ajout.html", {"form" : })