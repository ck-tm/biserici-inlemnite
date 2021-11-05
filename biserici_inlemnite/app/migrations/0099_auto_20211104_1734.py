# Generated by Django 3.1.13 on 2021-11-04 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0098_auto_20211103_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='bisericapage',
            name='componenta_artistica_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.componentaartisticapage'),
        ),
        migrations.AddField(
            model_name='bisericapage',
            name='conservare_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.conservarepage'),
        ),
        migrations.AddField(
            model_name='bisericapage',
            name='descriere_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.descrierepage'),
        ),
        migrations.AddField(
            model_name='bisericapage',
            name='identificare_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.identificarepage'),
        ),
        migrations.AddField(
            model_name='bisericapage',
            name='istoric_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.istoricpage'),
        ),
        migrations.AddField(
            model_name='bisericapage',
            name='valoare_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.valoarepage'),
        ),
    ]
