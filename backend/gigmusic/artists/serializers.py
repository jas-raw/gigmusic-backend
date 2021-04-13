from rest_framework import serializers

from .models import Artistas

class ArtistasSerializer(serializers.ModelSerializer):

	class Meta:
		model = Artistas
		fields = ('_id','nombre', 'genero', 'subgenero', 'decada', 'canciones')
		read_only_fields = ('_id', )
		lookup_field = 'nombre'