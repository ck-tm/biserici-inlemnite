from django.core.management.base import BaseCommand
from django.db.models import Count
import csv
from pprint import pprint
from app import models
from nomenclatoare import models as nmodels
from datetime import datetime
from biserici import models as b_models


BISERICI = [
    "Baia",
    "Bodești",
    "Brazii",
    "Bruznic",
    "Buceava-șoimuș",
    "Budești",
    "Ciuntești",
    "Corbesti",
    "Cristești",
    "Groși",
    "Groșeni",
    "Groșii noi",
    "Hălmăgel ",
    "Iercoșeni",
    "Ionești",
    "Iosășel",
    "Julița1",
    "Julița2",
    "Luncșoara-Vojdoci",
    "Luncșoara",
    "Mădrigești",
    "Minead",
    "Poiana",
    "Roșia nouă",
    "Seliște ",
    "Tisa",
    "Troaș",
    "Țărmure",
    "Valea mare",
    "Vidra ",
    "Zăbalț",
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting import..")

        judet, _ = nmodels.Judet.objects.get_or_create(nume="Arad")
        # print(models.BisericaPage.objects.all().delete())
        biserici_index = models.HomePage.objects.last()
        for biserica_old in b_models.Biserica.objects.all():
            nume = biserica_old.nume
            print(f"Create: {nume}")

            biserica = models.BisericaPage.objects.filter(title=nume)
            if not biserica.exists():
                biserica = models.BisericaPage()
                biserica.title = nume
                biserica.judet = judet
                # biserica._generate_slug()
                biserici_index.add_child(instance=biserica)
            else:
                biserica = biserica[0]
