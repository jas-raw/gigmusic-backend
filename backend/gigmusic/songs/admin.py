from django.contrib import admin

from .models import Canciones
# Register your models here

@admin.register(Canciones)
class CancionesAdmin(admin.ModelAdmin):

	nombre = Canciones.metadata
	list_display = ('metadata', 'canción')