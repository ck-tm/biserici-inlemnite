# Generated by Django 3.1.13 on 2021-09-28 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclatoare', '0014_historicalmaterialestructura_materialestructura'),
        ('app', '0053_auto_20210927_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='bisericapage',
            name='adresa',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='bisericapage',
            name='conservare',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bisericapage',
            name='latitudine',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bisericapage',
            name='localitate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pp_biserici', to='nomenclatoare.localitate'),
        ),
        migrations.AddField(
            model_name='bisericapage',
            name='longitudine',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bisericapage',
            name='prioritizare',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bisericapage',
            name='valoare',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='identificarepage',
            name='judet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ppp_biserici', to='nomenclatoare.judet'),
        ),
    ]
