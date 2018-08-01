import django_tables2 as tables
from django_tables2.utils import A
from .models import Usuario

class UsuarioTable(tables.Table):
    nombres = tables.LinkColumn(accessor='get_full_name', viewname='usuario_view',  args=[A('pk')])
    email = tables.Column()
    fecha_modificacion = tables.DateTimeColumn("DATETIME_FORMAT",False)
    
    class Meta:
        model = Usuario
        fields = ('id','nombres', 'ocupacion', 'email', 'fecha_modificacion')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "No se encontraron datos"