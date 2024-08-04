from django.shortcuts import render
from .models import Reclamation
from .serializers import ReclamationSerializer
from rest_framework import viewsets

# Create your views here.
class ReclamationView(viewsets.ModelViewSet):
    queryset = Reclamation.objects.all()
    serializer_class = ReclamationSerializer
