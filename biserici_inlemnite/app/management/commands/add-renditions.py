from wagtail.core.models import Page
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType

from django.db.models import Count
import csv
from pprint import pprint
from app import models
from nomenclatoare import models as nmodels
from datetime import datetime
import json


class Command(BaseCommand):
    def handle(self, *args, **options):

        # for poza in models.Poza.all():
        #     print(poza)
        content_poza = models.Poza
        content_types = ContentType.objects.filter(app_label=content_poza._meta.app_label)
        poza_models = [ct.model_class() for ct in content_types]
        poza_models += [
            models.PozeBiserica,
            models.PozeElementAnsambluConstruit,
            models.PozeElementImportantAnsambluConstruit,
            models.PozeClopot,
            models.PozeFinisajPortic,
            models.PozeFinisajPronaos,
            models.PozeFinisajNaos,
            models.PozeFinisajAltar,
            models.PozeEtapeIstoriceVizibile,
            models.PozeCtitori,
            models.PozeMesteri,
            models.PozeZugravi,
            models.PozePersonalitati,
            models.PozeArtisticEtapeIstoriceVizibile,
        ]
        for model in poza_models:
            if "Poze" in str(model) or (
                model is not None and issubclass(model, content_poza) and model is not content_poza
            ):
                for poza in model.objects.all():
                    print(model, poza)
                    try:
                        rendition = poza.poza.get_rendition("width-1279")
                        poza.rendition = {
                            "url": rendition.url,
                            "width": rendition.width,
                            "height": rendition.height,
                            "alt": rendition.alt,
                        }
                        poza.save()
                        print(poza.rendition)
                    except Exception as e:
                        pass
