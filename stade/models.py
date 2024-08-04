from django.db import models
from avis.models import Avis

# Create your models here.

class Stade(models.Model):

    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to='uploads/images', null=False, blank=False)
    location = models.CharField(max_length=150,null=False,blank=False)
    NbrOfparticipant = models.IntegerField(null=False,blank=False)
    decription = models.TextField()
    open = models.IntegerField(null=False,blank=False)
    note = models.IntegerField(null=False,default=False,blank=False)
    avis = models.ManyToManyField(Avis)



def __str__(self):
    return self.name



