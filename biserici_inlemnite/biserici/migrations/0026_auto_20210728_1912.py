# Generated by Django 3.1.13 on 2021-07-28 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biserici', '0025_auto_20210728_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='patrimoniu',
            name='estetica',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], help_text='Estetică / Arhitectură', null=True),
        ),
        migrations.AddField(
            model_name='patrimoniu',
            name='estetica_detalii',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patrimoniu',
            name='folosinta_actuala',
            field=models.IntegerField(blank=True, choices=[(1, 1), (3, 3), (5, 5)], help_text='Folosință actuală / singura biserică din sat / loc al patrimoniului imaterial', null=True),
        ),
        migrations.AddField(
            model_name='patrimoniu',
            name='folosinta_actuala_detalii',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patrimoniu',
            name='integritate',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], help_text='Integritate / Autenticitate', null=True),
        ),
        migrations.AddField(
            model_name='patrimoniu',
            name='integritate_detalii',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patrimoniu',
            name='mestesug',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], help_text='Meșteșug (calitatea muncii -  a se vedea golurile dintre lemne (dintre bârne în general dar în special la așezarea elementelor orizontale peste cele verticale))', null=True),
        ),
        migrations.AddField(
            model_name='patrimoniu',
            name='mestesug_detalii',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patrimoniu',
            name='peisaj_cultural',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], help_text='Parte definitorie a peisajului cultural al zonei', null=True),
        ),
        migrations.AddField(
            model_name='patrimoniu',
            name='peisaj_cultural_detalii',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patrimoniu',
            name='pictura',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
        ),
        migrations.AddField(
            model_name='patrimoniu',
            name='pictura_detalii',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patrimoniu',
            name='potential',
            field=models.IntegerField(blank=True, choices=[(1, 1), (3, 3), (5, 5)], help_text='Potențialul de beneficii aduse comunității locale', null=True),
        ),
        migrations.AddField(
            model_name='patrimoniu',
            name='potential_detalii',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patrimoniu',
            name='relevanta_actuala',
            field=models.IntegerField(blank=True, choices=[(1, 1), (3, 3), (5, 5)], help_text='Relevanța actuală pentru comunitatea locală (prin reprezentanții săi: preot, crâsnic, învățător, familii de bază)', null=True),
        ),
        migrations.AddField(
            model_name='patrimoniu',
            name='relevanta_actuala_detalii',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patrimoniu',
            name='unicitate',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], help_text='Unicitate / raritate', null=True),
        ),
        migrations.AddField(
            model_name='patrimoniu',
            name='unicitate_detalii',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patrimoniu',
            name='valoare_memoriala',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], help_text='evenimente, personalități', null=True),
        ),
        migrations.AddField(
            model_name='patrimoniu',
            name='valoare_memoriala_detalii',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patrimoniu',
            name='valoare_sit',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], help_text='Valoarea sitului împreună cu toate componentele ansamblului din care face parte, ținând cont de integritate, autenticitate, estetică peisageră, biodiversitate, etc. SUBIECTIV', null=True),
        ),
        migrations.AddField(
            model_name='patrimoniu',
            name='valoare_sit_detalii',
            field=models.TextField(blank=True, help_text='Descriere a elementelor valoroase, particulare', null=True),
        ),
        migrations.AddField(
            model_name='patrimoniu',
            name='vechime',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], help_text='printr-un algorim definit se va da automat o notă de la 1-5 în funcție de vechimea monumentului si a picturii descrise) conform OMCC2682/2003 ETC', null=True),
        ),
        migrations.AddField(
            model_name='patrimoniu',
            name='vechime_detalii',
            field=models.TextField(blank=True, null=True),
        ),
    ]
