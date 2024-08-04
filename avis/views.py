from django.shortcuts import render
from .models import Avis
from .serializers import AvisSerializer
from rest_framework import viewsets

# Create your views here.
class AvisView(viewsets.ModelViewSet):
    queryset = Avis.objects.all()
    serializer_class = AvisSerializer