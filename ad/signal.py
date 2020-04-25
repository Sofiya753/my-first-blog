from django.db.models import signals
from django.dispatch import receiver
from .models import Ad

# pre_save method signal
@receiver(signals.pre_save, sender=Ad)
def check_ad_description(sender, instance, **kwargs):
    if not instance.description:
        instance.description = 'This is Default Description'

# post_save method
@receiver(signals.post_save, sender=Ad)
def create_ad(sender, instance, created, **kwargs):
    print("Save method is called")
