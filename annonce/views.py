from django.shortcuts import render
from .models import Annonce
from .serializers import AnnonceSerializer
from rest_framework import viewsets

# Create your views here.
class AnnonceView(viewsets.ModelViewSet):
    queryset = Annonce.objects.all()
    serializer_class = AnnonceSerializer
