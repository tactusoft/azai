from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Dominio(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=1000)
    valor = models.CharField(max_length=1000)
    grupo = models.CharField(max_length=255)
    estado = models.IntegerField()
    fecha_creacion = models.DateTimeField(_('creado'), auto_now_add=True)
    fecha_modificacion = models.DateTimeField(_('modificado'), auto_now=True)

    def __str__(self):
        return self.nombre

class TipoIndicador(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=1000)
    estado = models.IntegerField()
    fecha_creacion = models.DateTimeField(_('creado'), auto_now_add=True)
    fecha_modificacion = models.DateTimeField(_('modificado'), auto_now=True)

class Indicador(models.Model):
    nombre_indicador = models.CharField(max_length=255)
    descripcion_indicador = models.CharField(max_length=1000)
    tipo_indicador = models.ForeignKey(TipoIndicador, on_delete=models.PROTECT)
    periodicidad = models.ForeignKey(Dominio, on_delete=models.PROTECT)
    estado = models.IntegerField()
    fecha_creacion = models.DateTimeField(_('creado'), auto_now_add=True)
    fecha_modificacion = models.DateTimeField(_('modificado'), auto_now=True)
