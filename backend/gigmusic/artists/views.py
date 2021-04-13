from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets

from .serializers import ArtistasSerializer
from .models import Artistas

# Create your views here.
class ArtistasView(viewsets.ModelViewSet):
    serializer_class = ArtistasSerializer
    queryset = Artistas.objects.all()
    lookup_field = 'nombre'

    @require_http_methods(["GET"])
    def get_viewset(self, request, nombre=None):
    	nombre = self.kwargs.get('nombre', None)
    	queryset = Artistas.objects.filter(nombre=nombre)
    	return queryset
