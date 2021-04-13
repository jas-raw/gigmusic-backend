from djongo import models

from django import forms

# Create your models here. 
class Contenido(models.Model):

    notas = models.CharField(max_length=12)
    espacio = models.CharField()
    letra = models.CharField()

    class Meta:
        abstract = True

class ContenidoForm(forms.ModelForm):

    class Meta:
        model = Contenido
        fields = (
            'notas', 'espacio', 'letra'
        )

class Cancion(models.Model):

    tipo = models.CharField(max_length=25)
    contenido = models.ArrayField(
        model_container=Contenido,
        model_form_class=ContenidoForm
    )

    class Meta:
        abstract = True

class CancionForm(forms.ModelForm):

    class Meta:
        model = Cancion
        fields = (
            'tipo', 'contenido'
        )

class Metadata(models.Model):

    artista = models.CharField()
    cancion = models.CharField()
    genero = models.CharField()
    subgenero = models.CharField()
    album = models.CharField()
    año = models.CharField()
    tonalidad = models.CharField()
    capo = models.CharField()

    class Meta:
        abstract = True

class MetadataForm(forms.ModelForm):

    class Meta:
        model = Metadata
        fields = (
            'artista', 'cancion', 'genero', 'subgenero', 
            'album', 'año', 'tonalidad', 'capo'
        )

class Canciones(models.Model):
    '''Modelo de canciones'''

    _id = models.ObjectIdField()
    metadata = models.EmbeddedField(
        model_container=Metadata,
        model_form_class=MetadataForm
    )
    canción = models.ArrayField(
        model_container=Cancion,
        model_form_class=CancionForm
    )
    
    def __str__(self):
        #Return username.
        return self.metadata
