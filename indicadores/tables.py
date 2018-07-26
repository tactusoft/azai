import django_tables2 as tables
from django_tables2.utils import A
from .models import TipoIndicador

class TipoIndicadorTable(tables.Table):
    nombre = tables.LinkColumn(viewname='indicador_list', args=[A('pk')])
    fecha_modificacion = tables.DateTimeColumn(verbose_name= 'Fecha', format ='d M Y')

    class Meta:
        model = TipoIndicador
        fields = ('nombre', 'descripcion', 'fecha_modificacion')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "No se encontraron datos"

class IndicadorTable(tables.Table):
    nombre_indicador = tables.LinkColumn(viewname='indicador_list', args=[A('pk')])

    class Meta:
        model = TipoIndicador
        fields = ('nombre_indicador', 'periodicidad')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "No se encontraron datos"        