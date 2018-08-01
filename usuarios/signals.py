
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import get_template
from .models import Usuario

# https://stackoverflow.com/questions/45418124/django-send-welcome-email-after-user-created-using-signals
# https://stackoverflow.com/questions/5594197/trigger-password-reset-email-in-django-without-browser
@receiver(post_save)
def usuario_post_save(sender, instance, created, **kwargs):
    if created:
        self.reset_password(instance.email, 'proyecto.azai@gmail.com' )

def reset_password(email, from_email, template='email/welcome.html'):
    """
    Reset the password for all (active) users with given E-Mail adress
    """
    form = PasswordResetForm({'email': email})
    form.is_valid()
    return form.save(from_email=from_email, email_template_name=template)
