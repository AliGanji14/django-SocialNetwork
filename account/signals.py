from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Profile


@receiver(post_save, sender=get_user_model())
def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
