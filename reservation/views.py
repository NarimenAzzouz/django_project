from django.shortcuts import render
from .models import Reservation
from .serializers import ReservationSerializer
from rest_framework import viewsets

# Create your views here.
class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer