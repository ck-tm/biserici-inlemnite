from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver

from app  import models 


@receiver(post_save, sender=models.BisericaPage) 
def create_biserica(sender, instance, created, **kwargs):
    if created:
        print('Create biserica', instance, created)
        instance.add_child(instance=models.IdentificarePage(title="Identificare"))
        instance.add_child(instance=models.DescrierePage(title="Descriere Arhitecturală"))
        instance.add_child(instance=models.IstoricPage(title="Istoric"))
        instance.add_child(instance=models.PatrimoniuPage(title="Patrimoniu"))
        instance.add_child(instance=models.ConservarePage(title="Conservare"))
        instance.add_child(instance=models.FinisajPage(title="Finisaj"))
        instance.add_child(instance=models.ComponentaArtisticaPage(title="Componenta Artistică"))
