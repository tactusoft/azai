from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Usuario


class CustomUserCreationForm(forms.ModelForm):

    """A form for creating new users."""

    class Meta:
        model = Usuario
        fields = ('grupo', 'email', 'first_name', 'last_name',
                  'numero_identificacion', 'telefono', 'ocupacion', 'is_active', 'is_staff')
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': _('Correo')}),
            'first_name': forms.TextInput(attrs={'placeholder': _('Nombres')}),
            'last_name': forms.TextInput(attrs={'placeholder': _('Apellidos')}),
            'numero_identificacion': forms.TextInput(attrs={'placeholder': _('Número identificación')}),
            'telefono': forms.TextInput(attrs={'placeholder': _('Teléfono')}),
        }
        labels = {
            'email': _('Correo'),
            'first_name': '',
            'last_name': '',
            'numero_identificacion': '',
            'telefono': '',
        }

    def save(self, commit=True):
        # Save the provided password in hashed format
        usuario = super().save(commit=False)
        # usuario.set_password("")
        # user.password_primera_vez = self.cleaned_data["password1"]

        if commit:
            user.save()
        return user


class CustomUserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    class Meta:
        model = Usuario
        fields = ('grupo', 'email', 'first_name', 'last_name',
                  'numero_identificacion', 'telefono', 'ocupacion', 'is_active', 'is_staff')
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': _('Correo')}),
            'first_name': forms.TextInput(attrs={'placeholder': _('Nombres')}),
            'last_name': forms.TextInput(attrs={'placeholder': _('Apellidos')}),
            'numero_identificacion': forms.TextInput(attrs={'placeholder': _('Número identificación')}),
            'telefono': forms.TextInput(attrs={'placeholder': _('Teléfono')}),
        }
        labels = {
            'email': _('Correo'),
            # 'first_name': '',
            # 'last_name': '',
            # 'numero_identificacion': '',
            # 'telefono': '',
        }                  
