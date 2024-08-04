from django.shortcuts import render
from .models import Sport
from .serializers import SportSerializer
from rest_framework import viewsets

# Create your views here.
class SportView(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer