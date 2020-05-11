# frrom what signal IN
# firedf after post_save when user is created
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# what can got signal OUT
from django.dispatch import receiver
from .models import Profile

# when user is save then sand signal post_save
# and then signal will be recived by create_profile
# that take arg (sender, instance, created, **kwargs)
# then if user created create user with user=instance
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()
