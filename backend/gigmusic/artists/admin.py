from django.contrib import admin

from .models import Artistas
# Register your models here.

@admin.register(Artistas)
class ArtistasAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'genero', 'subgenero', 'decada')
	search_fields = ('nombre',)