# Generated by Django 3.1.13 on 2021-11-05 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0103_auto_20211105_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='pozeartisticetapeistoricevizibile',
            name='rendition',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pozebiserica',
            name='rendition',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pozeclopot',
            name='rendition',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pozectitori',
            name='rendition',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pozeelementansambluconstruit',
            name='rendition',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pozeelementimportantansambluconstruit',
            name='rendition',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pozeetapeistoricevizibile',
            name='rendition',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pozefinisajaltar',
            name='rendition',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pozefinisajnaos',
            name='rendition',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pozefinisajportic',
            name='rendition',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pozefinisajpronaos',
            name='rendition',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pozemesteri',
            name='rendition',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pozepersonalitati',
            name='rendition',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pozezugravi',
            name='rendition',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
