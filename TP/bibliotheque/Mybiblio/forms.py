from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from TD3_django.bibliotheque import models


class LivreForm(ModelForm):
    class Meta:
        model = models.Livre
        fields = ('titre', 'auteur', 'date_parution', 'nombres_pages', 'resume')
        labels = {
            'titre': _('Titre'),
            'auteur': _('Auteur'),
            'date_parution': _('date␣de␣parution'),
            'nombres_pages': _('nombres␣de␣pages'),
            'resume': _('Résumé')
        }
