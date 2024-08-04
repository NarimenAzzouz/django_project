from django.db import models

# Create your models here.

class Avis(models.Model):

    note = models.IntegerField(null=False,blank=False)



    

def __str__(self):
    return self.note

