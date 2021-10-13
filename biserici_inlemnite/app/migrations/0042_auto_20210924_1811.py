# Generated by Django 3.1.13 on 2021-09-24 15:11

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclatoare', '0013_historicalmaterialinvelitoareturle_materialinvelitoareturle'),
        ('app', '0041_auto_20210924_1750'),
    ]

    operations = [
        migrations.RenameField(
            model_name='istoricpage',
            old_name='datare_secol_detalii',
            new_name='datare_secol_observatii',
        ),
        migrations.RenameField(
            model_name='istoricpage',
            old_name='pisanie_secol_detalii',
            new_name='pisanie_secol_observatii',
        ),
        migrations.AddField(
            model_name='componentaartisticapage',
            name='pictura_exterioara_anul_picturii',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='componentaartisticapage',
            name='pictura_exterioara_datare_observatii',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AddField(
            model_name='componentaartisticapage',
            name='pictura_exterioara_datare_prin_interval_timp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='componentaartisticapage',
            name='pictura_exterioara_datare_secol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_localizari_exterioare', to='nomenclatoare.secol'),
        ),
        migrations.AddField(
            model_name='componentaartisticapage',
            name='pictura_exterioara_localizare',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_localizari_exterioare', to='nomenclatoare.localizarepictura'),
        ),
        migrations.AddField(
            model_name='componentaartisticapage',
            name='pictura_exterioara_localizare_observatii',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AddField(
            model_name='componentaartisticapage',
            name='pictura_exterioara_numar_straturi_pictura',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='componentaartisticapage',
            name='pictura_exterioara_suport',
            field=models.ManyToManyField(blank=True, related_name='p_localizari_exterioare', to='nomenclatoare.SuportPictura'),
        ),
        migrations.AddField(
            model_name='componentaartisticapage',
            name='pictura_exterioara_sursa_datare',
            field=models.ManyToManyField(blank=True, related_name='p_componente_artistice_exterioare', to='nomenclatoare.SursaDatare'),
        ),
        migrations.AddField(
            model_name='componentaartisticapage',
            name='pictura_exterioara_tehnica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_localizari_exterioare', to='nomenclatoare.tehnicapictura'),
        ),
        migrations.AddField(
            model_name='componentaartisticapage',
            name='pictura_interioara_anul_picturii',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='componentaartisticapage',
            name='pictura_interioara_datare_observatii',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AddField(
            model_name='componentaartisticapage',
            name='pictura_interioara_datare_prin_interval_timp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='componentaartisticapage',
            name='pictura_interioara_datare_secol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_localizari_interioare', to='nomenclatoare.secol'),
        ),
        migrations.AddField(
            model_name='componentaartisticapage',
            name='pictura_interioara_localizare',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_localizari_interioare', to='nomenclatoare.localizarepictura', verbose_name='Proporția de suprafață acoperită'),
        ),
        migrations.AddField(
            model_name='componentaartisticapage',
            name='pictura_interioara_localizare_observatii',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Proporția de suprafață acoperită observatii'),
        ),
        migrations.AddField(
            model_name='componentaartisticapage',
            name='pictura_interioara_numar_straturi_pictura',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='componentaartisticapage',
            name='pictura_interioara_suport',
            field=models.ManyToManyField(blank=True, related_name='p_localizari_interioare', to='nomenclatoare.SuportPictura'),
        ),
        migrations.AddField(
            model_name='componentaartisticapage',
            name='pictura_interioara_sursa_datare',
            field=models.ManyToManyField(blank=True, related_name='p_componente_artistice_interioare', to='nomenclatoare.SursaDatare'),
        ),
        migrations.AddField(
            model_name='componentaartisticapage',
            name='pictura_interioara_tehnica_pictura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nomenclatoare.tehnicapictura'),
        ),
    ]