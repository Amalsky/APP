from .models import Profile, User, downloadApp, App, AdminUser
from django.dispatch import receiver

from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if not isinstance(instance, AdminUser):
        Profile.objects.get_or_create(user=instance)
    else:
        # Handle the case for AdminUser here
        pass


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if not isinstance(instance, AdminUser):
        instance.profile.save()
