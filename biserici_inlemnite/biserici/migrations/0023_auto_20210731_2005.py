# Generated by Django 3.1.13 on 2021-07-31 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("biserici", "0022_auto_20210731_1928"),
    ]

    operations = [
        migrations.AlterField(
            model_name="conservare",
            name="stare_bolti",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="conservare",
            name="stare_cimitir",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="conservare",
            name="stare_corp_biserica",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="conservare",
            name="stare_elemente_arhitecturale",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="conservare",
            name="stare_finisaj_peste_corp",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="conservare",
            name="stare_finisaj_tambur_turn",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="conservare",
            name="stare_fundatii",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="conservare",
            name="stare_icoane_istorice",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="conservare",
            name="stare_invelitoare",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="conservare",
            name="stare_monumente_funerare_valoroase",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="conservare",
            name="stare_pardoseli_interioare",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="conservare",
            name="stare_picturi_exterioare",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="conservare",
            name="stare_picturi_interioare",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="conservare",
            name="stare_sarpanta_peste_corp_biserica",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="conservare",
            name="stare_structura_turn",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="conservare",
            name="stare_teren",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="conservare",
            name="stare_usi_si_ferestre",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="conservare",
            name="starea_mobilier",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="conservare",
            name="starea_obiecte_de_cult",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="conservare",
            name="vegetatie_invaziva",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="historicalconservare",
            name="stare_bolti",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="historicalconservare",
            name="stare_cimitir",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="historicalconservare",
            name="stare_corp_biserica",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="historicalconservare",
            name="stare_elemente_arhitecturale",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="historicalconservare",
            name="stare_finisaj_peste_corp",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="historicalconservare",
            name="stare_finisaj_tambur_turn",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="historicalconservare",
            name="stare_fundatii",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="historicalconservare",
            name="stare_icoane_istorice",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="historicalconservare",
            name="stare_invelitoare",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="historicalconservare",
            name="stare_monumente_funerare_valoroase",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="historicalconservare",
            name="stare_pardoseli_interioare",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="historicalconservare",
            name="stare_picturi_exterioare",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="historicalconservare",
            name="stare_picturi_interioare",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="historicalconservare",
            name="stare_sarpanta_peste_corp_biserica",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="historicalconservare",
            name="stare_structura_turn",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="historicalconservare",
            name="stare_teren",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="historicalconservare",
            name="stare_usi_si_ferestre",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="historicalconservare",
            name="starea_mobilier",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="historicalconservare",
            name="starea_obiecte_de_cult",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="historicalconservare",
            name="vegetatie_invaziva",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="historicalpatrimoniu",
            name="estetica",
            field=models.IntegerField(
                blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], help_text="Estetică / Arhitectură", null=True
            ),
        ),
        migrations.AlterField(
            model_name="historicalpatrimoniu",
            name="folosinta_actuala",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "A"), (2, "B"), (3, "C")],
                help_text="Folosință actuală / singura biserică din sat / loc al patrimoniului imaterial",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalpatrimoniu",
            name="integritate",
            field=models.IntegerField(
                blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], help_text="Integritate / Autenticitate", null=True
            ),
        ),
        migrations.AlterField(
            model_name="historicalpatrimoniu",
            name="mestesug",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "A"), (2, "B"), (3, "C")],
                help_text="Meșteșug (calitatea muncii -  a se vedea golurile dintre lemne (dintre bârne în general dar în special la așezarea elementelor orizontale peste cele verticale))",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalpatrimoniu",
            name="peisaj_cultural",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "A"), (2, "B"), (3, "C")],
                help_text="Parte definitorie a peisajului cultural al zonei",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalpatrimoniu",
            name="pictura",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="historicalpatrimoniu",
            name="potential",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "A"), (2, "B"), (3, "C")],
                help_text="Potențialul de beneficii aduse comunității locale",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalpatrimoniu",
            name="relevanta_actuala",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "A"), (2, "B"), (3, "C")],
                help_text="Relevanța actuală pentru comunitatea locală (prin reprezentanții săi: preot, crâsnic, învățător, familii de bază)",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalpatrimoniu",
            name="unicitate",
            field=models.IntegerField(
                blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], help_text="Unicitate / raritate", null=True
            ),
        ),
        migrations.AlterField(
            model_name="historicalpatrimoniu",
            name="valoare_memoriala",
            field=models.IntegerField(
                blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], help_text="evenimente, personalități", null=True
            ),
        ),
        migrations.AlterField(
            model_name="historicalpatrimoniu",
            name="valoare_sit",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "A"), (2, "B"), (3, "C")],
                help_text="Valoarea sitului împreună cu toate componentele ansamblului din care face parte, ținând cont de integritate, autenticitate, estetică peisageră, biodiversitate, etc. SUBIECTIV",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalpatrimoniu",
            name="vechime",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "A"), (2, "B"), (3, "C")],
                help_text="Printr-un algorim definit se va da automat o notă de la 1-5 în funcție de vechimea monumentului si a picturii descrise conform OMCC2682/2003 ETC",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="patrimoniu",
            name="estetica",
            field=models.IntegerField(
                blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], help_text="Estetică / Arhitectură", null=True
            ),
        ),
        migrations.AlterField(
            model_name="patrimoniu",
            name="folosinta_actuala",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "A"), (2, "B"), (3, "C")],
                help_text="Folosință actuală / singura biserică din sat / loc al patrimoniului imaterial",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="patrimoniu",
            name="integritate",
            field=models.IntegerField(
                blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], help_text="Integritate / Autenticitate", null=True
            ),
        ),
        migrations.AlterField(
            model_name="patrimoniu",
            name="mestesug",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "A"), (2, "B"), (3, "C")],
                help_text="Meșteșug (calitatea muncii -  a se vedea golurile dintre lemne (dintre bârne în general dar în special la așezarea elementelor orizontale peste cele verticale))",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="patrimoniu",
            name="peisaj_cultural",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "A"), (2, "B"), (3, "C")],
                help_text="Parte definitorie a peisajului cultural al zonei",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="patrimoniu",
            name="pictura",
            field=models.IntegerField(blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], null=True),
        ),
        migrations.AlterField(
            model_name="patrimoniu",
            name="potential",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "A"), (2, "B"), (3, "C")],
                help_text="Potențialul de beneficii aduse comunității locale",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="patrimoniu",
            name="relevanta_actuala",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "A"), (2, "B"), (3, "C")],
                help_text="Relevanța actuală pentru comunitatea locală (prin reprezentanții săi: preot, crâsnic, învățător, familii de bază)",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="patrimoniu",
            name="unicitate",
            field=models.IntegerField(
                blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], help_text="Unicitate / raritate", null=True
            ),
        ),
        migrations.AlterField(
            model_name="patrimoniu",
            name="valoare_memoriala",
            field=models.IntegerField(
                blank=True, choices=[(1, "A"), (2, "B"), (3, "C")], help_text="evenimente, personalități", null=True
            ),
        ),
        migrations.AlterField(
            model_name="patrimoniu",
            name="valoare_sit",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "A"), (2, "B"), (3, "C")],
                help_text="Valoarea sitului împreună cu toate componentele ansamblului din care face parte, ținând cont de integritate, autenticitate, estetică peisageră, biodiversitate, etc. SUBIECTIV",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="patrimoniu",
            name="vechime",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "A"), (2, "B"), (3, "C")],
                help_text="Printr-un algorim definit se va da automat o notă de la 1-5 în funcție de vechimea monumentului si a picturii descrise conform OMCC2682/2003 ETC",
                null=True,
            ),
        ),
    ]
