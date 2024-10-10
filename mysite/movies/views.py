from django.shortcuts import render
from rest_framework import viewsets
from .models import Moviedata
from .serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset=Moviedata.objects.all()
    serializer_class=MovieSerializer
# Create your views here.
