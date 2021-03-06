# Generated by Django 3.1.13 on 2021-09-24 12:41

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclatoare', '0011_formasarpanteturle_historicalformasarpanteturle_historicalpozitionareturle_pozitionareturle'),
        ('app', '0027_auto_20210924_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='descrierepage',
            name='turle_exista',
            field=models.BooleanField(default=False, verbose_name='Există'),
        ),
        migrations.AddField(
            model_name='descrierepage',
            name='turle_forma_sarpanta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='biserici', to='nomenclatoare.formasarpanteturle', verbose_name='Formă șarpantă'),
        ),
        migrations.AddField(
            model_name='descrierepage',
            name='turle_numar',
            field=models.IntegerField(blank=True, null=True, verbose_name='Număr'),
        ),
        migrations.AddField(
            model_name='descrierepage',
            name='turle_numar_goluri',
            field=models.IntegerField(blank=True, null=True, verbose_name='Număr goluri'),
        ),
        migrations.AddField(
            model_name='descrierepage',
            name='turle_observatii',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AddField(
            model_name='descrierepage',
            name='turle_pozitionare',
            field=models.ManyToManyField(blank=True, related_name='biserici', to='nomenclatoare.PozitionareTurle', verbose_name='Poziționare'),
        ),
    ]
