from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Usuario

@receiver(post_save, sender=Usuario)
def notificacion_creacion_nuevo_usuario(sender, instance, created, **kwargs):
    if created:
    #     UserProfile.objects.create(user=instance)
    # instance.profile.save()

    subject = 'Welcome to MyApp!'
    from_email = 'no-reply@myapp.com'
    to = instance.email
    plaintext = get_template('email/welcome.txt')
    html = get_template('email/welcome.html')

    d = {'email': instance.email}

    text_content = plaintext.render(d)
    html_content = html.render(d)

    try:
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    except BadHeaderError:
        return HttpResponse('Invalid header found.')