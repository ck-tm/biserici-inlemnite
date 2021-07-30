# Generated by Django 3.1.13 on 2021-07-30 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclatoare', '0005_boltapestealtar_historicalboltapestealtar_historicaltipboltapestealtar_historicaltipboltapronaos_tip'),
        ('biserici', '0015_auto_20210730_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descriere',
            name='sistem_in_catei',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='biserici', to='nomenclatoare.tipstructuracatei', verbose_name='Sistem structural al corpului bisericii În căței'),
        ),
        migrations.AlterField(
            model_name='historicaldescriere',
            name='sistem_in_catei',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='nomenclatoare.tipstructuracatei', verbose_name='Sistem structural al corpului bisericii În căței'),
        ),
    ]
