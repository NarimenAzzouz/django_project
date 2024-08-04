from django.db import models

# Create your models here.

# Création de l'énumération des types de paiement avec TextChoices
class SportTypeEnum(models.TextChoices):
    Football = 'CashPayment'
    Handball = 'OnLinePayment'
    Basketball = 'Basketball'
    Natation = 'Natation'
    Equitation = 'Equitation'
    Vollyball = 'Vollyball' 
    Bebenageur = 'Bebenageur'
    

class Sport(models.Model):

  

    sport_type = models.CharField(
        max_length=20,
        choices=SportTypeEnum.choices,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.get_sport_type_display()}'


