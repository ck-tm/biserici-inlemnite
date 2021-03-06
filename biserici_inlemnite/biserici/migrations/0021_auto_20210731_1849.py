# Generated by Django 3.1.13 on 2021-07-31 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclatoare', '0007_historicalregistruiconostas_historicaltipusiiconostas_registruiconostas_tipusiiconostas'),
        ('biserici', '0020_auto_20210731_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='componentaartistica',
            name='iconostas_naos_altar_registre',
            field=models.ManyToManyField(blank=True, related_name='iconostasuri_naos_altar', to='nomenclatoare.RegistruIconostas', verbose_name='Registru'),
        ),
        migrations.AddField(
            model_name='componentaartistica',
            name='iconostas_naos_altar_tip_usi',
            field=models.ManyToManyField(blank=True, related_name='iconostasuri_naos_altar', to='nomenclatoare.TipUsiIconostas', verbose_name='Tip uși'),
        ),
    ]
