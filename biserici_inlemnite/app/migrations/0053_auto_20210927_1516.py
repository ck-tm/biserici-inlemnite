# Generated by Django 3.1.13 on 2021-09-27 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclatoare', '0014_historicalmaterialestructura_materialestructura'),
        ('app', '0052_auto_20210927_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descrierepage',
            name='materiale',
            field=models.ManyToManyField(blank=True, help_text='Materiale folosite in construcția bisericii', to='nomenclatoare.MaterialeStructura'),
        ),
    ]