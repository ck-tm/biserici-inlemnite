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
        for x in models.ConservarePage.objects.all():
            x.save()
        for x in models.ValoarePage.objects.all():
            x.save()