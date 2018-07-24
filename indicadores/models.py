from django.db import models

# Create your models here.
class Dominio(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=1000)
    valor = models.CharField(max_length=1000)
    grupo = models.CharField(max_length=255)
    estado = models.IntegerField()

class TipoIndicador(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=1000)
    estado = models.IntegerField()

class Indicador(models.Model):
    nombre_indicador = models.CharField(max_length=255)
    descripcion_indicador = models.CharField(max_length=1000)
    tipo_indicador = models.ForeignKey(TipoIndicador, on_delete=models.PROTECT)
    dominio = models.ForeignKey(Dominio, on_delete=models.PROTECT)
    estado = models.IntegerField()
