# Generated by Django 3.1.13 on 2021-10-29 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0095_bisericapage_utitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='bisericapage',
            name='datare_an',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
