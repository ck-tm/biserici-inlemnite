# Generated by Django 3.1.13 on 2021-10-25 22:21

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclatoare', '0024_historicalmaterialmobilier_materialmobilier'),
        ('app', '0082_auto_20211026_0119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='componentaartisticapage',
            name='mobiliere',
        ),
        migrations.AddField(
            model_name='componentaartisticapage',
            name='mobiliere_new',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='nomenclatoare.MaterialMobilier', verbose_name='Mobilier'),
        ),
    ]
