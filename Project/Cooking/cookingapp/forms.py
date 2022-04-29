from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class recetteForm(ModelForm):
    class Meta:
        model = models.recette
        fields = ("nom", "nombre_personne")
        labels = {
            'nom': _("Nom : "),
            'nombre_personne': _("Nombre de personnes : ")
        }