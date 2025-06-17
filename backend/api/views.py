from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Creator
from .serializers import CreatorSerializer
from .filters import CreatorFilter

class CreatorListCreate(generics.ListCreateAPIView):
    queryset         = Creator.objects.all().order_by("-id")
    serializer_class = CreatorSerializer
    filterset_class  = CreatorFilter