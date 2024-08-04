from django.shortcuts import render
from .models import Paiement
from .serializers import PaiementSerializer
from rest_framework import viewsets

# Create your views here.
class PaiementView(viewsets.ModelViewSet):
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer