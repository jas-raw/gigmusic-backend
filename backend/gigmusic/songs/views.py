from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets

from .serializers import CancionesSerializer
from .models import Canciones

# Create your views here.
class CancionesView(viewsets.ModelViewSet):
    serializer_class = CancionesSerializer
    queryset = Canciones.objects.all()

    @require_http_methods(["GET"])
    def get_viewset(self, request, cancion=None):
    	cancion = self.kwargs.get('cancion', None)
    	queryset = Canciones.objects.filter(Metadata__startswith={'cancion':'cancion'})
    	return queryset
