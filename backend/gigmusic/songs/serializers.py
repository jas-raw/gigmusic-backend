from rest_framework import serializers

from .models import Canciones

class CancionesSerializer(serializers.ModelSerializer):

	class Meta:
		model = Canciones
		fields = ('_id','metadata', 'canción')
		read_only_fields = ('_id', )