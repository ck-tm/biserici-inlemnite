# Generated by Django 3.1.13 on 2021-08-03 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biserici', '0024_auto_20210803_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='descriere',
            name='numar_accese',
        ),
        migrations.RemoveField(
            model_name='descriere',
            name='numar_geamuri',
        ),
        migrations.RemoveField(
            model_name='historicaldescriere',
            name='numar_accese',
        ),
        migrations.RemoveField(
            model_name='historicaldescriere',
            name='numar_geamuri',
        ),
        migrations.AddField(
            model_name='descriere',
            name='numar_accese_altar',
            field=models.IntegerField(blank=True, null=True, verbose_name='Număr accese altar'),
        ),
        migrations.AddField(
            model_name='descriere',
            name='numar_accese_altar_detalii',
            field=models.TextField(blank=True, null=True, verbose_name='Număr accese altar (observații)'),
        ),
        migrations.AddField(
            model_name='descriere',
            name='numar_accese_naos',
            field=models.IntegerField(blank=True, null=True, verbose_name='Număr accese naos'),
        ),
        migrations.AddField(
            model_name='descriere',
            name='numar_accese_naos_detalii',
            field=models.TextField(blank=True, null=True, verbose_name='Număr accese naos (observații)'),
        ),
        migrations.AddField(
            model_name='descriere',
            name='numar_accese_pridvor',
            field=models.IntegerField(blank=True, null=True, verbose_name='Număr accese pridvor'),
        ),
        migrations.AddField(
            model_name='descriere',
            name='numar_accese_pridvor_detalii',
            field=models.TextField(blank=True, null=True, verbose_name='Număr accese pridvor (observații)'),
        ),
        migrations.AddField(
            model_name='descriere',
            name='numar_accese_pronaos',
            field=models.IntegerField(blank=True, null=True, verbose_name='Număr accese pronaos'),
        ),
        migrations.AddField(
            model_name='descriere',
            name='numar_accese_pronaos_detalii',
            field=models.TextField(blank=True, null=True, verbose_name='Număr accese pronaos (observații)'),
        ),
        migrations.AddField(
            model_name='descriere',
            name='numar_geamuri_altar',
            field=models.IntegerField(blank=True, null=True, verbose_name='Număr geamuri altar'),
        ),
        migrations.AddField(
            model_name='descriere',
            name='numar_geamuri_altar_detalii',
            field=models.TextField(blank=True, null=True, verbose_name='Număr geamuri altar (observații)'),
        ),
        migrations.AddField(
            model_name='descriere',
            name='numar_geamuri_naos',
            field=models.IntegerField(blank=True, null=True, verbose_name='Număr geamuri naos'),
        ),
        migrations.AddField(
            model_name='descriere',
            name='numar_geamuri_naos_detalii',
            field=models.TextField(blank=True, null=True, verbose_name='Număr geamuri naos (observații)'),
        ),
        migrations.AddField(
            model_name='descriere',
            name='numar_geamuri_pridvor',
            field=models.IntegerField(blank=True, null=True, verbose_name='Număr geamuri pridvor'),
        ),
        migrations.AddField(
            model_name='descriere',
            name='numar_geamuri_pridvor_detalii',
            field=models.TextField(blank=True, null=True, verbose_name='Număr geamuri pridvor (observații)'),
        ),
        migrations.AddField(
            model_name='descriere',
            name='numar_geamuri_pronaos',
            field=models.IntegerField(blank=True, null=True, verbose_name='Număr geamuri pronaos'),
        ),
        migrations.AddField(
            model_name='descriere',
            name='numar_geamuri_pronaos_detalii',
            field=models.TextField(blank=True, null=True, verbose_name='Număr geamuri pronaos (observații)'),
        ),
        migrations.AddField(
            model_name='historicaldescriere',
            name='numar_accese_altar',
            field=models.IntegerField(blank=True, null=True, verbose_name='Număr accese altar'),
        ),
        migrations.AddField(
            model_name='historicaldescriere',
            name='numar_accese_altar_detalii',
            field=models.TextField(blank=True, null=True, verbose_name='Număr accese altar (observații)'),
        ),
        migrations.AddField(
            model_name='historicaldescriere',
            name='numar_accese_naos',
            field=models.IntegerField(blank=True, null=True, verbose_name='Număr accese naos'),
        ),
        migrations.AddField(
            model_name='historicaldescriere',
            name='numar_accese_naos_detalii',
            field=models.TextField(blank=True, null=True, verbose_name='Număr accese naos (observații)'),
        ),
        migrations.AddField(
            model_name='historicaldescriere',
            name='numar_accese_pridvor',
            field=models.IntegerField(blank=True, null=True, verbose_name='Număr accese pridvor'),
        ),
        migrations.AddField(
            model_name='historicaldescriere',
            name='numar_accese_pridvor_detalii',
            field=models.TextField(blank=True, null=True, verbose_name='Număr accese pridvor (observații)'),
        ),
        migrations.AddField(
            model_name='historicaldescriere',
            name='numar_accese_pronaos',
            field=models.IntegerField(blank=True, null=True, verbose_name='Număr accese pronaos'),
        ),
        migrations.AddField(
            model_name='historicaldescriere',
            name='numar_accese_pronaos_detalii',
            field=models.TextField(blank=True, null=True, verbose_name='Număr accese pronaos (observații)'),
        ),
        migrations.AddField(
            model_name='historicaldescriere',
            name='numar_geamuri_altar',
            field=models.IntegerField(blank=True, null=True, verbose_name='Număr geamuri altar'),
        ),
        migrations.AddField(
            model_name='historicaldescriere',
            name='numar_geamuri_altar_detalii',
            field=models.TextField(blank=True, null=True, verbose_name='Număr geamuri altar (observații)'),
        ),
        migrations.AddField(
            model_name='historicaldescriere',
            name='numar_geamuri_naos',
            field=models.IntegerField(blank=True, null=True, verbose_name='Număr geamuri naos'),
        ),
        migrations.AddField(
            model_name='historicaldescriere',
            name='numar_geamuri_naos_detalii',
            field=models.TextField(blank=True, null=True, verbose_name='Număr geamuri naos (observații)'),
        ),
        migrations.AddField(
            model_name='historicaldescriere',
            name='numar_geamuri_pridvor',
            field=models.IntegerField(blank=True, null=True, verbose_name='Număr geamuri pridvor'),
        ),
        migrations.AddField(
            model_name='historicaldescriere',
            name='numar_geamuri_pridvor_detalii',
            field=models.TextField(blank=True, null=True, verbose_name='Număr geamuri pridvor (observații)'),
        ),
        migrations.AddField(
            model_name='historicaldescriere',
            name='numar_geamuri_pronaos',
            field=models.IntegerField(blank=True, null=True, verbose_name='Număr geamuri pronaos'),
        ),
        migrations.AddField(
            model_name='historicaldescriere',
            name='numar_geamuri_pronaos_detalii',
            field=models.TextField(blank=True, null=True, verbose_name='Număr geamuri pronaos (observații)'),
        ),
    ]