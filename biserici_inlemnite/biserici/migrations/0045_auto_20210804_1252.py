# Generated by Django 3.1.13 on 2021-08-04 09:52

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("biserici", "0044_auto_20210803_1738"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalistoric",
            name="completare",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="historicalistoric",
            name="missing_fields",
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="istoric",
            name="completare",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="istoric",
            name="missing_fields",
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
