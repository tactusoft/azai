from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import Usuario
from .forms import CustomUserCreationForm, CustomUserChangeForm

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    """Defina el modelo de administrador para el modelo de usuario personalizado sin campo username."""
    readonly_fields = ('last_login', 'fecha_creacion', 'fecha_modificacion')

    list_display = ('get_full_name', 'ocupacion', 'email', 'fecha_modificacion')
    list_filter = ()
    search_fields = ()
    ordering = ('email',)
    filter_horizontal = ()
    filter_vertical = ()

    add_form = CustomUserCreationForm
    add_fieldsets = (
        (_('Información básica'), {
            'classes': ('wide',),
            'fields': (('grupo', 'email')),
        }),
        (_('Datos personales'), {
            'classes': ('wide',),
            'fields': (('first_name', 'last_name'), 'numero_identificacion', 'telefono', 'ocupacion'),
        }),
        (_('Opciones avanzadas'), {
            'classes': ('collapse',),
            'fields': ('is_staff','is_active','is_superuser'),
        }),
    )

    form = CustomUserChangeForm
    fieldsets = (
        (_('Información básica'), {
            'classes': ('wide',),
            'fields': (('grupo', 'email')),
        }),
        (_('Datos personales'), {
            'classes': ('wide',),
            'fields': (('first_name', 'last_name'), 'numero_identificacion', 'telefono', 'ocupacion'),
        }),
        (_('Opciones avanzadas'), {
            'classes': ('collapse',),
            'fields': ('is_staff','is_active','is_superuser'),
        }),
    )

# Register your models here.