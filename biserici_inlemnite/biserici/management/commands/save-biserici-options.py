from django.core.management.base import BaseCommand
from django.db.models import Count
import csv
from pprint import pprint
from biserici import models
from nomenclatoare import models as nmodels
from datetime import datetime
from biserici.api.views import BisericiViewSet
from django.test.client import RequestFactory
from django.contrib.auth import get_user_model
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting OPTIONS..")

        rf = RequestFactory()
        c = rf.get("/api/biserici/1")
        c.META["SERVER_NAME"] = "localhost"
        c.user = get_user_model().objects.get(username="admin")
        c.method = "OPTIONS"
        a = BisericiViewSet

        x = a.as_view({"post": "list"})(c).data
        json_data = json.dumps(x, indent=4)

        with open("frontend/src/models_biserici.js", "w") as f:
            f.write(json_data)
