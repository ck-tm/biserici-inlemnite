# Generated by Django 3.1.13 on 2021-08-03 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biserici', '0032_auto_20210803_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='descriere',
            name='solee_detalii',
            field=models.TextField(blank=True, null=True, verbose_name='Solee (observații)'),
        ),
        migrations.AddField(
            model_name='historicaldescriere',
            name='solee_detalii',
            field=models.TextField(blank=True, null=True, verbose_name='Solee (observații)'),
        ),
    ]
