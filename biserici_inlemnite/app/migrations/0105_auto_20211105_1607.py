# Generated by Django 3.1.13 on 2021-11-05 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0104_auto_20211105_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='descrierepage',
            name='model_fotogrametrie',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='descrierepage',
            name='model_nori_de_puncte',
            field=models.TextField(blank=True, null=True),
        ),
    ]
