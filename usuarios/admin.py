from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import (Ocupacion, Usuario)
from .forms import (CustomUserCreationForm, CustomUserChangeForm)

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



    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     (_('Personal info'), {'fields': ('first_name', 'last_name')}),
    #     (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
    #                                    'groups', 'user_permissions')}),
    #     (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2'),
    #     }),
    # )
    # list_display = ('email', 'first_name', 'last_name', 'is_staff')
    # search_fields = ('email', 'first_name', 'last_name')
    # 

    # # The forms to add and change user instances



    # # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # # overrides get_fieldsets to use this attribute when creating a user.
    # add_fieldsets = (
    #     ('Informaci�n b�sica', {'classes': ('wide',), 'fields': ('rol','email','password1', 'password2')}),
    #     ('Datos personales', {'classes': ('wide',), 'fields': ('nombres', 'numero_identificacion', 'telefono', 'ocupacion')}),
    # )
    # fieldsets = (
    #     ('Informaci�n b�sica', {'fields': ('rol', 'email')}),
    #     ('Datos personales', {'fields': ('nombres', 'numero_identificacion', 'telefono', 'ocupacion')}),
    # )

    # search_fields = ()
    # ordering = ('email',)
    
    

# Register your models here.
admin.site.register(Ocupacion)