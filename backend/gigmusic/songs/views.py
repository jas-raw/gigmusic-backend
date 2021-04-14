from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import action

import pymongo

from .serializers import CancionesSerializer
from .models import Canciones

# Create your views here.
class CancionesView(viewsets.ModelViewSet):

	filter_backends = (filters.SearchFilter,)
	serializer_class = CancionesSerializer

	@action(detail=True, methods=['get'])
	def get_queryset(self):
		queryset = Canciones.objects.all()
		search = self.request.query_params.get('search')
		queryset = queryset.filter(metadata={'artista':search})
		return queryset