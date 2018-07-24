from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.forms.widgets import PasswordInput, EmailInput
from django.utils.translation import ugettext_lazy as _


class CustomAuthForm(AuthenticationForm):
    username = forms.EmailField(
        max_length=254,
        widget=EmailInput(attrs={'class':'form-control','placeholder': 'Correo', 'autofocus': True})
    )
    password = forms.CharField(
        strip=False,
        widget=PasswordInput(attrs={'class':'form-control ultimo','placeholder':_('Contraseña')})
    )

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Correo"), 
        max_length=254,
        widget=EmailInput(attrs={'class':'form-control ultimo','placeholder': 'Correo', 'autofocus': True})
    )