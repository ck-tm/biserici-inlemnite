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
        instance.identificare_page = identificare
        instance.save()
        istoric = models.IstoricPage(title="2. Istoric")
        instance.add_child(instance=istoric)
        instance.istoric_page = istoric
        instance.save()
        descriere = models.DescrierePage(title="3. Descriere Arhitectură / Peisaj")
        instance.add_child(instance=descriere)
        instance.descriere_page = descriere
        instance.save()
        componenta_artistica = models.ComponentaArtisticaPage(title="4. Descriere Componenta Artistică")
        instance.add_child(instance=componenta_artistica)
        instance.componenta_artistica_page = componenta_artistica
        instance.save()
        conservare = models.ConservarePage(title="5. Conservare")
        instance.add_child(instance=conservare)
        instance.conservare_page = conservare
        instance.save()
        valoare = models.ValoarePage(title="6. Valoare")
        instance.add_child(instance=valoare)
        instance.valoare_page = valoare
        instance.save()


@receiver(post_save) 
def create_rendition(sender, instance, created, **kwargs):
    if created:
        if issubclass(sender, models.Poza):
            rendition = instance.poza.get_rendition('width-1280')
            instance.rendition = {
                "url": rendition.url,
                "width": rendition.width,
                "height": rendition.height,
                "alt": rendition.alt
            }
            instance.save()
