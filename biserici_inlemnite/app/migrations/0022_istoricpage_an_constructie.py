# Generated by Django 3.1.13 on 2021-09-24 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0021_auto_20210924_1356"),
    ]

    operations = [
        migrations.AddField(
            model_name="istoricpage",
            name="an_constructie",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
