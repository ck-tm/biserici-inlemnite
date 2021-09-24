from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver

from app  import models 


@receiver(post_save, sender=models.BisericaPage) 
def create_biserica(sender, instance, created, **kwargs):
    if created:
        print('Create biserica', instance, created)
        identificare = models.IdentificarePage(title="1. Identificare")
        instance.add_child(instance=identificare)
        istoric = models.IstoricPage(title="2. Istoric")
        instance.add_child(instance=istoric)
        descriere = models.DescrierePage(title="3. Descriere Arhitectură / Peisaj")
        instance.add_child(instance=descriere)
        componenta_artistica = models.ComponentaArtisticaPage(title="4. Descriere Componenta Artistică")
        instance.add_child(instance=componenta_artistica)
        conservare = models.ConservarePage(title="5. Conservare")
        instance.add_child(instance=conservare)
        patrimoniu = models.ValoarePage(title="6. Valoare")
        instance.add_child(instance=patrimoniu)
