from django.shortcuts import render
#import forms
# Create your views here.


def ajout(request):
    #gform = forms.RecetteForm()
    return render(request, 'cookingapp/ajout.html') #{"form": gform})


def index(request):
    return render(request, 'cookingapp/index.html')


def main(request):
    return render(request, 'cookingapp/main.html')

