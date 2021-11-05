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
        for model in poza_models:
            if (model is not None and issubclass(model, content_poza) and model is not content_poza):
                for poza in model.objects.all():
                    print(poza)
                    try:
                        rendition = poza.poza.get_rendition('width-1280')
                        poza.rendition = {
                            "url": rendition.url,
                            "width": rendition.width,
                            "height": rendition.height,
                            "alt": rendition.alt
                        }
                        poza.save()
                        print(poza.rendition)
                    except Exception as e:
                        print('--', e)