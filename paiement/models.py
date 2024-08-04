from enum import Enum
from django.db import models


# Create your models here.

# Création de l'énumération des types de paiement avec TextChoices
class PaymentTypeEnum(models.TextChoices):
    CashPayment = 'CashPayment'
    OnlinePayment = 'OnLinePayment'
    

class Paiement(models.Model):

  

    montant = models.IntegerField(null=False,blank=False)
    payment_type = models.CharField(
        max_length=20,
        choices=PaymentTypeEnum.choices,
        null=True,
        blank=True
    )


    def __str__(self):
        return f'Paiement: {self.montant} - {self.get_payment_type_display()}'
