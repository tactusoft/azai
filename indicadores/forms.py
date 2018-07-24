from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Indicador

_widgets = {
    'nombre_indicador': forms.TextInput(attrs={'class':'form-control', 'placeholder': _('Nombre del Indicador')}),
    'descripcion_indicador': forms.Textarea(attrs={'class':'form-control', 'placeholder': _('Nombre del Indicador'),'rows':2}),
    'periodicidad': forms.Select(attrs={'class':'form-control custom-select d-block w-100'}),
}

class CustomIndicadorCreationForm(forms.ModelForm):
    class Meta:
        model = Indicador
        fields = ('nombre_indicador','descripcion_indicador','periodicidad')
        widgets = _widgets
        labels = {
            'nombre': _('Nombre del Indicador'),
        }
        