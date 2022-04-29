from django.db import models

# Create your models here.


class Recette(models.Model):
    nom = models.CharField(max_length=45)
    nombre_personne = models.IntegerField()



