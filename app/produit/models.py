from django.db import models

# Create your models here.
class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix_vente = models.DecimalField(max_digits=6, decimal_places=2)
    quantite_seuil = models.IntegerField()

    def __str__(self):
        return self.nom
    