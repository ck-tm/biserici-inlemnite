from django.core.management.base import BaseCommand
from django.db.models import Count
import csv
from pprint import pprint
from app import models
from nomenclatoare import models as nmodels
from datetime import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting import..")
        biserica = models.BisericaPage.objects.get(pk=821)
        print(biserica)
        print(biserica.get_children())
        for capitol in biserica.get_children():
            print(capitol, capitol.path)
        