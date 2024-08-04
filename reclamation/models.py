from django.db import models

# Create your models here.


class Reclamation(models.Model):

    decription = models.TextField()
    
    

def __str__(self):
    return self.description
