# Generated by Django 3.1.13 on 2021-07-30 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biserici', '0006_auto_20210730_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografii',
            name='foto1',
            field=models.ManyToManyField(blank=True, null=True, related_name='foto1', to='biserici.FotografieDetaliuPod'),
        ),
        migrations.AlterField(
            model_name='fotografii',
            name='foto2',
            field=models.ManyToManyField(blank=True, null=True, related_name='foto2', to='biserici.FotografieDetaliuPod'),
        ),
    ]
