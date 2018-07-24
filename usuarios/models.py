from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, Group, GroupManager
from django.utils.translation import ugettext_lazy as _
from django.db.models.manager import EmptyManager
from django.core import serializers
from django.forms.models import model_to_dict
import json

import logging

logger = logging.getLogger(__name__)

# https://www.fomfus.com/articles/how-to-use-email-as-username-for-django-authentication-removing-the-username
# https://docs.djangoproject.com/en/dev/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
class UsuarioManager(UserManager):
    """Define un model manager para el modelo Usuario en el cual el atributo username no es requerido."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Crea y guarda un usuario con el correo electrónico y la contraseña especificados."""
        
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Crea y guarda un usuario regular con el correo electrónico y la contraseña especificados."""

        if not password:
            password = self.make_random_password()
        
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Crea y guarda un super usuario con el correo electrónico y la contraseña especificados."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Un super usuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Un super usuario debe tener is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Usuario(AbstractUser):
    """
    Los usuarios de este proyecto son una especializaci�n de la clase AbstractUser usada por el sistema de autenticaci�n de Django.

    El password y el email son requeridos. El username = email
    """
    username = None
    email = models.EmailField(_('email address'), unique=True) # changes email to unique and blank to false
    numero_identificacion = models.CharField(_('número identificación'), max_length=10, unique=True, blank=False, null=False)
    telefono = models.CharField(_('telefono'), max_length=50, blank=False, null=False)
    ocupacion = models.CharField(_('ocupación'), max_length=50, blank=True, null=False)

    fecha_creacion = models.DateTimeField(_('creado'), auto_now_add=True)
    fecha_modificacion = models.DateTimeField(_('modificado'), auto_now=True)

    grupo = models.ForeignKey(
        Group,
        verbose_name=_('grupo'),
        on_delete=models.PROTECT, 
        null=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
    )

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'numero_identificacion', 'telefono' ] # removes email from REQUIRED_FIELDS

    def get_absolute_url(self):
        return reverse('usuario', kwargs={'pk': self.pk})

    # @property
    # def groups(self):
    #     return self._groups

    # AbstractBaseUser
    # password
    # last_login
    # is_active

    # AbstractUser
    # username
    # first_name
    # last_name
    # email
    # is_staff
    # is_active
    # date_joined

    # EMAIL_FIELD
    # USERNAME_FIELD
    # REQUIRED_FIELDS

    # AbstractBaseUser
    # Stores the raw password if set_password() is called so that it can
    # be passed to password_changed() after the model is saved.
    # self.password = make_password(raw_password)
    # self._password = raw_password