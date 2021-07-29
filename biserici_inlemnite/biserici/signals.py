from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver

from biserici.models import (
    Biserica,
    Identificare,
    Descriere,
    Istoric,
    Patrimoniu,
    Conservare,
    Fotografii
    )


@receiver(post_save, sender=Biserica) 
def create_biserica(sender, instance, created, **kwargs):
    print('Create biserica', instance, created)
    if created:
        Identificare.objects.create(biserica=instance)
        Descriere.objects.create(biserica=instance)
        Istoric.objects.create(biserica=instance)
        Patrimoniu.objects.create(biserica=instance)
        Conservare.objects.create(biserica=instance)
        Fotografii.objects.create(biserica=instance)
