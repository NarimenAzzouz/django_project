from django.db import models
from annonce.models import Annonce
from reclamation.models import Reclamation
from paiement.models import Paiement

# Create your models here.

class Reservation(models.Model):

    resDate = models.DateField()
    endTime = models.DateField()
    startTime = models.DateField()
    annonce = models.ManyToManyField(Annonce)
    reclamation = models.ManyToManyField(Reclamation)
    paiement = models.ManyToManyField(Paiement)


def __str__(self):
    return self.resDate
