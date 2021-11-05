from wagtail.core.models import Page
from django.core.management.base import BaseCommand
from django.db.models import Count
import csv
from pprint import pprint
from app import models
from nomenclatoare import models as nmodels
from datetime import datetime
import json

class Command(BaseCommand):
    def handle(self, *args, **options):

        for biserica in models.BisericaPage.objects.all():
            biserica.identificare_page = biserica.get_children().type(
                models.IdentificarePage)[0].specific
            biserica.descriere_page = biserica.get_children().type(
                models.DescrierePage)[0].specific
            biserica.istoric_page = biserica.get_children().type(
                models.IstoricPage)[0].specific
            biserica.componenta_artistica_page = biserica.get_children().type(
                models.ComponentaArtisticaPage)[0].specific
            biserica.conservare_page = biserica.get_children().type(
                models.ConservarePage)[0].specific
            biserica.valoare_page = biserica.get_children().type(
                models.ValoarePage)[0].specific
            biserica.save()
            print(biserica)

        for biserica in models.BisericaPage.objects.all():
            print(biserica)
            print(biserica.identificare_page)
            print(biserica.descriere_page)
            print(biserica.istoric_page)
            print(biserica.componenta_artistica_page)
            print(biserica.conservare_page)
            print(biserica.valoare_page)
            print('------')