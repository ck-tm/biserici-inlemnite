# Generated by Django 3.1.13 on 2021-10-25 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0083_auto_20211026_0121"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="componentaartisticapage",
            name="altar_decor",
        ),
    ]
