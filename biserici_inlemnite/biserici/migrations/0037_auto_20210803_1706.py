# Generated by Django 3.1.13 on 2021-08-03 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biserici', '0036_finisajaltar_finisajnaos_finisajportic_finisajpronaos_historicalfinisajaltar_historicalfinisajnaos_h'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finisajnaos',
            name='finisaj',
        ),
        migrations.RemoveField(
            model_name='finisajnaos',
            name='material',
        ),
        migrations.RemoveField(
            model_name='finisajportic',
            name='finisaj',
        ),
        migrations.RemoveField(
            model_name='finisajportic',
            name='material',
        ),
        migrations.RemoveField(
            model_name='finisajpronaos',
            name='finisaj',
        ),
        migrations.RemoveField(
            model_name='finisajpronaos',
            name='material',
        ),
        migrations.RemoveField(
            model_name='historicalfinisajaltar',
            name='finisaj',
        ),
        migrations.RemoveField(
            model_name='historicalfinisajaltar',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalfinisajaltar',
            name='material',
        ),
        migrations.RemoveField(
            model_name='historicalfinisajnaos',
            name='finisaj',
        ),
        migrations.RemoveField(
            model_name='historicalfinisajnaos',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalfinisajnaos',
            name='material',
        ),
        migrations.RemoveField(
            model_name='historicalfinisajportic',
            name='finisaj',
        ),
        migrations.RemoveField(
            model_name='historicalfinisajportic',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalfinisajportic',
            name='material',
        ),
        migrations.RemoveField(
            model_name='historicalfinisajpronaos',
            name='finisaj',
        ),
        migrations.RemoveField(
            model_name='historicalfinisajpronaos',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalfinisajpronaos',
            name='material',
        ),
        migrations.DeleteModel(
            name='FinisajAltar',
        ),
        migrations.DeleteModel(
            name='FinisajNaos',
        ),
        migrations.DeleteModel(
            name='FinisajPortic',
        ),
        migrations.DeleteModel(
            name='FinisajPronaos',
        ),
        migrations.DeleteModel(
            name='HistoricalFinisajAltar',
        ),
        migrations.DeleteModel(
            name='HistoricalFinisajNaos',
        ),
        migrations.DeleteModel(
            name='HistoricalFinisajPortic',
        ),
        migrations.DeleteModel(
            name='HistoricalFinisajPronaos',
        ),
    ]
