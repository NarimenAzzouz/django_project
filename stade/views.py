from django.shortcuts import render
from .models import Stade
from .serializers import StadeSerializer
from rest_framework import viewsets

# Create your views here.
class StadeView(viewsets.ModelViewSet):
    queryset = Stade.objects.all()
    serializer_class = StadeSerializer