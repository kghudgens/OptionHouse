# Fires the signal when something is saved
from django.db.models.signals import post_save
#Need the user model to be saved; its the sender
from django.contrib.auth.models import User
# receives the User signal
from django.dispatch import receiver
# Deals with the potential object does not exist error
from django.core.exceptions import ObjectDoesNotExist
# Associated model
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)














