from django.db import models
from sport.models import Sport
from stade.models import Stade

# Create your models here.

class Annonce(models.Model):

    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to='uploads/images', null=False, blank=False)
    location = models.CharField(max_length=150,null=False,blank=False)
    NbrOfparticipant = models.IntegerField(null=False,blank=False)
    duration = models.DateField()
    sport = models.ForeignKey(Sport,null=True,on_delete=models.SET_NULL)
    stade = models.ForeignKey(Stade,null=True,on_delete=models.SET_NULL)


    

def __str__(self):
    return self.name



