from django.shortcuts import render
from rest_framework import generics
from .serializers import ModelSerializer
from .models import ModelOne

# Create your views here.


class ModelOneView(generics.CreateAPIView):
    queryset = ModelOne.objects.all()
    serializer_class = ModelSerializer
