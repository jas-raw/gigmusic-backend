from djongo import models

from django import forms

# Create your models here.
class CancionArtista(models.Model):
    cancion = models.CharField()

    class Meta:
        abstract = True

class CancionArtistaForm(forms.ModelForm):

    class Meta:
        model = CancionArtista
        fields = (
            'cancion',
        )

class Artistas(models.Model):
    '''Modelo de artistas'''

    _id = models.ObjectIdField()
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=30)
    subgenero = models.CharField(max_length=20, blank=True)
    decada = models.CharField(max_length=20, blank=True)
    canciones = models.ArrayField(
        model_container=CancionArtista,
        model_form_class=CancionArtistaForm
    )

    def __str__(self):
        #Return nombre artista
        return self.nombre
