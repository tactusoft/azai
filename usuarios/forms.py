from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from .models import Usuario

_widgets = {
    'grupo': forms.Select(attrs={'class':'form-control custom-select d-block w-100'}),
    'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': _('correo')}),
    'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': _('nombres')}),
    'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': _('apellidos')}),
    'numero_identificacion': forms.TextInput(attrs={'class':'form-control', 'placeholder': _('número identificación')}),
    'telefono': forms.TextInput(attrs={'class':'form-control', 'placeholder': _('teléfono')}),
    'ocupacion': forms.TextInput(attrs={'class':'form-control', 'placeholder': _('ocupación')}),
}


class CustomUserCreationForm(forms.ModelForm):

    """A form for creating new users."""

    class Meta:
        model = get_user_model()
        fields = ('grupo', 'email', 'first_name', 'last_name',
                  'numero_identificacion', 'telefono', 'ocupacion', 'is_active')
        widgets = _widgets
        labels = {
            'grupo': _('rol'),
        }                  

    def save(self, commit=True):
        # Save the provided password in hashed format
        usuario = super().save(commit=False)

        if commit:
            usuario.save()
        return usuario


class CustomUserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    class Meta:
        model = get_user_model()
        fields = ('grupo', 'email', 'first_name', 'last_name',
                  'numero_identificacion', 'telefono', 'ocupacion', 'is_active')
        widgets = _widgets

        labels = {
            'grupo': _('rol'),
        }
