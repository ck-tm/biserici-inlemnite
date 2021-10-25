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

        for descriere_page in models.DescrierePage.objects.all():
            print(descriere_page)
            for revision in descriere_page.revisions.all():
                print(revision)
                j = json.loads(revision.content_json)
                if 'materiale' in j.keys():
                    j['materiale'] = None
                    pprint(j['materiale'])
                    revision.content_json = json.dumps(j)
                    revision.save()
