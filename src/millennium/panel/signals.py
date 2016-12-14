from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.conf import settings

@receiver(user_logged_in)
def sig_user_logged_in(sender, user, request, **kwargs):
    request.session['tenant'] = user.groups.all()[0].id
