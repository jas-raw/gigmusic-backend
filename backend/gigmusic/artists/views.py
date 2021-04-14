from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import action

from .serializers import ArtistasSerializer
from .models import Artistas

# Create your views here.
class ArtistasView(viewsets.ModelViewSet):

	search_fields = ['nombre', 'genero']
	filter_backends = (filters.SearchFilter,)
	serializer_class = ArtistasSerializer
	lookup_field = 'nombre'

	@action(detail=True, methods=['get'])
	def get_queryset(self):
		queryset = Artistas.objects.all()
		return queryset
