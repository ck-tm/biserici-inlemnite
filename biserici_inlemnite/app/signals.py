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
        descriere = models.DescrierePage(title="2. Descriere Arhitecturală")
        instance.add_child(instance=descriere)
        finisaj = models.FinisajPage(title="2.1 Finisaj")
        instance.add_child(instance=finisaj)
        componenta_artistica = models.ComponentaArtisticaPage(title="2.2 Componenta Artistică")
        instance.add_child(instance=componenta_artistica)
        istoric = models.IstoricPage(title="3. Istoric")
        instance.add_child(instance=istoric)
        conservare = models.ConservarePage(title="4. Conservare")
        instance.add_child(instance=conservare)
        patrimoniu = models.PatrimoniuPage(title="5. Patrimoniu")
        instance.add_child(instance=patrimoniu)
