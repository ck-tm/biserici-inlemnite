from django.core.management.base import BaseCommand
from django.db.models import Count
import csv
from pprint import pprint
from biserici import models
from nomenclatoare import models as nmodels
from datetime import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting import..")
        for biserica in models.Biserica.objects.all():
            print(biserica, "identificare")
            biserica.identificare.save()
            print(biserica, "descriere")
            biserica.descriere.save()
            print(biserica, "istoric")
            biserica.istoric.save()
            print(biserica, "patrimoniu")
            biserica.patrimoniu.save()
            print(biserica, "conservare")
            biserica.conservare.save()
            print(biserica, "fotografii")
            biserica.fotografii.save()
            print(biserica, "finisaj")
            biserica.finisaj.save()
            print(biserica, "componentaartistica")
            biserica.componentaartistica.save()
