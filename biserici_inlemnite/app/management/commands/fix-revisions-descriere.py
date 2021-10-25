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



# x = Page.objects.get(pk=231).specific
# xx =x.revisions.last()
# j['materiale'] = None
# xx.content_json = json.dumps(j)
# xx.save()
# xx.publish()


        #     print(descriere_page.get_parent())

        #     for revision in descriere_page.revisions.all().order_by('-created_at'):
        #         if revision.user == None:
        #             revision.delete()
        #         # print(revision.user, revision.created_at)
        #         # last_revision = descriere_page.revisions.last()
        #         # while last_revision.user == None:
        #         #     last_revision.

        #         # print(last_revision, last_revision.user)
        #         # previous_revision = last_revision.get_previous()
        #         # print(previous_revision, previous_revision.user)
        #         # print(previous_revision.content_json)
        #         j = json.loads(revision.content_json)
        #         j['materiale'] = None
        #         revision.content_json = json.dumps(j)
        #         revision.save()
        #         revision.publish()
        #         break
        #         # print(descriere_page.revisions.all()[0].user)
