# Generated by Django 3.1.13 on 2021-07-29 13:49

import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Biserica",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nume", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name_plural": "Biserici",
            },
        ),
        migrations.CreateModel(
            name="Conservare",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "stare_cimitir",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_cimitir_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_monumente_funerare_valoroase",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_monumente_funerare_valoroase_detalii", models.TextField(blank=True, null=True)),
                (
                    "vegetatie_invaziva",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                (
                    "vegetatie_invaziva_detalii",
                    models.TextField(
                        blank=True, help_text="Vegetație invazivă ce poate pune monumentul în pericol", null=True
                    ),
                ),
                (
                    "stare_elemente_arhitecturale",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_elemente_arhitecturale_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_teren",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_teren_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_fundatii",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_fundatii_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_corp_biserica",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_corp_biserica_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_bolti",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_bolti_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_sarpanta_peste_corp_biserica",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_sarpanta_peste_corp_biserica_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_structura_turn",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                (
                    "stare_structura_turn_detalii",
                    models.TextField(
                        blank=True, help_text="tarea structurii turnului, inclusiv a tălpilor și a coifului", null=True
                    ),
                ),
                (
                    "stare_invelitoare",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_invelitoare_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_finisaj_peste_corp",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_finisaj_peste_corp_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_finisaj_tambur_turn",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_finisaj_tambur_turn_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_pardoseli_interioare",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_pardoseli_interioare_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_usi_si_ferestre",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_usi_si_ferestre_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_picturi_exterioare",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_picturi_exterioare_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_picturi_interioare",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_picturi_interioare_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_icoane_istorice",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_icoane_istorice_detalii", models.TextField(blank=True, null=True)),
                (
                    "starea_obiecte_de_cult",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("starea_obiecte_de_cult_detalii", models.TextField(blank=True, null=True)),
                (
                    "starea_mobilier",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("starea_mobilier_detalii", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name_plural": "Stare conservare Biserici",
            },
        ),
        migrations.CreateModel(
            name="Descriere",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("toponim", models.CharField(blank=True, help_text="denumirea locului", max_length=150, null=True)),
            ],
            options={
                "verbose_name_plural": "Descriere Biserici",
            },
        ),
        migrations.CreateModel(
            name="HistoricalBiserica",
            fields=[
                ("id", models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name="ID")),
                ("nume", models.CharField(max_length=50)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")], max_length=1),
                ),
            ],
            options={
                "verbose_name": "historical biserica",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalConservare",
            fields=[
                ("id", models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name="ID")),
                (
                    "stare_cimitir",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_cimitir_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_monumente_funerare_valoroase",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_monumente_funerare_valoroase_detalii", models.TextField(blank=True, null=True)),
                (
                    "vegetatie_invaziva",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                (
                    "vegetatie_invaziva_detalii",
                    models.TextField(
                        blank=True, help_text="Vegetație invazivă ce poate pune monumentul în pericol", null=True
                    ),
                ),
                (
                    "stare_elemente_arhitecturale",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_elemente_arhitecturale_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_teren",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_teren_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_fundatii",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_fundatii_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_corp_biserica",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_corp_biserica_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_bolti",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_bolti_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_sarpanta_peste_corp_biserica",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_sarpanta_peste_corp_biserica_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_structura_turn",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                (
                    "stare_structura_turn_detalii",
                    models.TextField(
                        blank=True, help_text="tarea structurii turnului, inclusiv a tălpilor și a coifului", null=True
                    ),
                ),
                (
                    "stare_invelitoare",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_invelitoare_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_finisaj_peste_corp",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_finisaj_peste_corp_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_finisaj_tambur_turn",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_finisaj_tambur_turn_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_pardoseli_interioare",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_pardoseli_interioare_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_usi_si_ferestre",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_usi_si_ferestre_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_picturi_exterioare",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_picturi_exterioare_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_picturi_interioare",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_picturi_interioare_detalii", models.TextField(blank=True, null=True)),
                (
                    "stare_icoane_istorice",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("stare_icoane_istorice_detalii", models.TextField(blank=True, null=True)),
                (
                    "starea_obiecte_de_cult",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("starea_obiecte_de_cult_detalii", models.TextField(blank=True, null=True)),
                (
                    "starea_mobilier",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("starea_mobilier_detalii", models.TextField(blank=True, null=True)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")], max_length=1),
                ),
            ],
            options={
                "verbose_name": "historical conservare",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalDescriere",
            fields=[
                ("id", models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name="ID")),
                ("toponim", models.CharField(blank=True, help_text="denumirea locului", max_length=150, null=True)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")], max_length=1),
                ),
            ],
            options={
                "verbose_name": "historical descriere",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalIdentificare",
            fields=[
                ("id", models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name="ID")),
                ("latitudine", models.FloatField(blank=True, null=True)),
                ("longitudine", models.FloatField(blank=True, null=True)),
                ("denumire_actuala", models.CharField(blank=True, max_length=150, null=True)),
                ("denumire_precedenta", models.CharField(blank=True, max_length=150, null=True)),
                ("denumire_locala", models.CharField(blank=True, max_length=150, null=True)),
                ("denumire_oberservatii", models.TextField(blank=True, null=True)),
                ("utilizare_detalii", models.TextField(blank=True, null=True)),
                ("singularitate_detalii", models.TextField(blank=True, null=True)),
                ("functiune_detalii", models.TextField(blank=True, null=True)),
                ("functiune_initiala_detalii", models.TextField(blank=True, null=True)),
                ("proprietate_detalii", models.TextField(blank=True, null=True)),
                ("proprietar_actual", models.TextField(blank=True, null=True)),
                (
                    "inscriere_documente_cadastrale",
                    models.IntegerField(blank=True, choices=[(1, "Da"), (2, "Nu"), (3, "În curs de")], null=True),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")], max_length=1),
                ),
            ],
            options={
                "verbose_name": "historical identificare",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalIstoric",
            fields=[
                ("id", models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name="ID")),
                ("anul_constructiei", models.IntegerField(blank=True, null=True)),
                ("datare_prin_interval_timp", models.CharField(blank=True, max_length=50, null=True)),
                ("datare_secol_detalii", models.TextField(blank=True, null=True)),
                ("datare_secol_sursa", models.TextField(blank=True, null=True)),
                ("pisanie_traducere", models.TextField(blank=True, null=True)),
                ("pisanie_secol_detalii", models.TextField(blank=True, null=True)),
                ("pisanie_secol_sursa", models.TextField(blank=True, null=True)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")], max_length=1),
                ),
            ],
            options={
                "verbose_name": "historical istoric",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalPatrimoniu",
            fields=[
                ("id", models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name="ID")),
                (
                    "vechime",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        help_text="Printr-un algorim definit se va da automat o notă de la 1-5 în funcție de vechimea monumentului si a picturii descrise conform OMCC2682/2003 ETC",
                        null=True,
                    ),
                ),
                ("vechime_detalii", models.TextField(blank=True, null=True)),
                (
                    "integritate",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        help_text="Integritate / Autenticitate",
                        null=True,
                    ),
                ),
                ("integritate_detalii", models.TextField(blank=True, null=True)),
                (
                    "unicitate",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        help_text="Unicitate / raritate",
                        null=True,
                    ),
                ),
                ("unicitate_detalii", models.TextField(blank=True, null=True)),
                (
                    "valoare_memoriala",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        help_text="evenimente, personalități",
                        null=True,
                    ),
                ),
                ("valoare_memoriala_detalii", models.TextField(blank=True, null=True)),
                (
                    "peisaj_cultural",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        help_text="Parte definitorie a peisajului cultural al zonei",
                        null=True,
                    ),
                ),
                ("peisaj_cultural_detalii", models.TextField(blank=True, null=True)),
                (
                    "valoare_sit",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        help_text="Valoarea sitului împreună cu toate componentele ansamblului din care face parte, ținând cont de integritate, autenticitate, estetică peisageră, biodiversitate, etc. SUBIECTIV",
                        null=True,
                    ),
                ),
                (
                    "valoare_sit_detalii",
                    models.TextField(blank=True, help_text="Descriere a elementelor valoroase, particulare", null=True),
                ),
                (
                    "estetica",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        help_text="Estetică / Arhitectură",
                        null=True,
                    ),
                ),
                ("estetica_detalii", models.TextField(blank=True, null=True)),
                (
                    "mestesug",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        help_text="Meșteșug (calitatea muncii -  a se vedea golurile dintre lemne (dintre bârne în general dar în special la așezarea elementelor orizontale peste cele verticale))",
                        null=True,
                    ),
                ),
                ("mestesug_detalii", models.TextField(blank=True, null=True)),
                (
                    "pictura",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("pictura_detalii", models.TextField(blank=True, null=True)),
                (
                    "folosinta_actuala",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, 1), (3, 3), (5, 5)],
                        help_text="Folosință actuală / singura biserică din sat / loc al patrimoniului imaterial",
                        null=True,
                    ),
                ),
                ("folosinta_actuala_detalii", models.TextField(blank=True, null=True)),
                (
                    "relevanta_actuala",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, 1), (3, 3), (5, 5)],
                        help_text="Relevanța actuală pentru comunitatea locală (prin reprezentanții săi: preot, crâsnic, învățător, familii de bază)",
                        null=True,
                    ),
                ),
                ("relevanta_actuala_detalii", models.TextField(blank=True, null=True)),
                (
                    "potential",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, 1), (3, 3), (5, 5)],
                        help_text="Potențialul de beneficii aduse comunității locale",
                        null=True,
                    ),
                ),
                ("potential_detalii", models.TextField(blank=True, null=True)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")], max_length=1),
                ),
            ],
            options={
                "verbose_name": "historical patrimoniu",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalUser",
            fields=[
                ("id", models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name="ID")),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        db_index=True,
                        error_messages={"unique": "A user with that username already exists."},
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                        verbose_name="username",
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=150, verbose_name="first name")),
                ("last_name", models.CharField(blank=True, max_length=150, verbose_name="last name")),
                ("email", models.EmailField(blank=True, max_length=254, verbose_name="email address")),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                ("date_joined", models.DateTimeField(default=django.utils.timezone.now, verbose_name="date joined")),
                ("name", models.CharField(blank=True, max_length=255, verbose_name="Name of User")),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")], max_length=1),
                ),
            ],
            options={
                "verbose_name": "historical user",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="Identificare",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("latitudine", models.FloatField(blank=True, null=True)),
                ("longitudine", models.FloatField(blank=True, null=True)),
                ("denumire_actuala", models.CharField(blank=True, max_length=150, null=True)),
                ("denumire_precedenta", models.CharField(blank=True, max_length=150, null=True)),
                ("denumire_locala", models.CharField(blank=True, max_length=150, null=True)),
                ("denumire_oberservatii", models.TextField(blank=True, null=True)),
                ("utilizare_detalii", models.TextField(blank=True, null=True)),
                ("singularitate_detalii", models.TextField(blank=True, null=True)),
                ("functiune_detalii", models.TextField(blank=True, null=True)),
                ("functiune_initiala_detalii", models.TextField(blank=True, null=True)),
                ("proprietate_detalii", models.TextField(blank=True, null=True)),
                ("proprietar_actual", models.TextField(blank=True, null=True)),
                (
                    "inscriere_documente_cadastrale",
                    models.IntegerField(blank=True, choices=[(1, "Da"), (2, "Nu"), (3, "În curs de")], null=True),
                ),
            ],
            options={
                "verbose_name_plural": "Identificare Biserici",
            },
        ),
        migrations.CreateModel(
            name="Patrimoniu",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "vechime",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        help_text="Printr-un algorim definit se va da automat o notă de la 1-5 în funcție de vechimea monumentului si a picturii descrise conform OMCC2682/2003 ETC",
                        null=True,
                    ),
                ),
                ("vechime_detalii", models.TextField(blank=True, null=True)),
                (
                    "integritate",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        help_text="Integritate / Autenticitate",
                        null=True,
                    ),
                ),
                ("integritate_detalii", models.TextField(blank=True, null=True)),
                (
                    "unicitate",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        help_text="Unicitate / raritate",
                        null=True,
                    ),
                ),
                ("unicitate_detalii", models.TextField(blank=True, null=True)),
                (
                    "valoare_memoriala",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        help_text="evenimente, personalități",
                        null=True,
                    ),
                ),
                ("valoare_memoriala_detalii", models.TextField(blank=True, null=True)),
                (
                    "peisaj_cultural",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        help_text="Parte definitorie a peisajului cultural al zonei",
                        null=True,
                    ),
                ),
                ("peisaj_cultural_detalii", models.TextField(blank=True, null=True)),
                (
                    "valoare_sit",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        help_text="Valoarea sitului împreună cu toate componentele ansamblului din care face parte, ținând cont de integritate, autenticitate, estetică peisageră, biodiversitate, etc. SUBIECTIV",
                        null=True,
                    ),
                ),
                (
                    "valoare_sit_detalii",
                    models.TextField(blank=True, help_text="Descriere a elementelor valoroase, particulare", null=True),
                ),
                (
                    "estetica",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        help_text="Estetică / Arhitectură",
                        null=True,
                    ),
                ),
                ("estetica_detalii", models.TextField(blank=True, null=True)),
                (
                    "mestesug",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        help_text="Meșteșug (calitatea muncii -  a se vedea golurile dintre lemne (dintre bârne în general dar în special la așezarea elementelor orizontale peste cele verticale))",
                        null=True,
                    ),
                ),
                ("mestesug_detalii", models.TextField(blank=True, null=True)),
                (
                    "pictura",
                    models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
                ),
                ("pictura_detalii", models.TextField(blank=True, null=True)),
                (
                    "folosinta_actuala",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, 1), (3, 3), (5, 5)],
                        help_text="Folosință actuală / singura biserică din sat / loc al patrimoniului imaterial",
                        null=True,
                    ),
                ),
                ("folosinta_actuala_detalii", models.TextField(blank=True, null=True)),
                (
                    "relevanta_actuala",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, 1), (3, 3), (5, 5)],
                        help_text="Relevanța actuală pentru comunitatea locală (prin reprezentanții săi: preot, crâsnic, învățător, familii de bază)",
                        null=True,
                    ),
                ),
                ("relevanta_actuala_detalii", models.TextField(blank=True, null=True)),
                (
                    "potential",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, 1), (3, 3), (5, 5)],
                        help_text="Potențialul de beneficii aduse comunității locale",
                        null=True,
                    ),
                ),
                ("potential_detalii", models.TextField(blank=True, null=True)),
                ("biserica", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="biserici.biserica")),
            ],
            options={
                "verbose_name_plural": "Valoare Patrimoniu",
            },
        ),
        migrations.CreateModel(
            name="Istoric",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("anul_constructiei", models.IntegerField(blank=True, null=True)),
                ("datare_prin_interval_timp", models.CharField(blank=True, max_length=50, null=True)),
                ("datare_secol_detalii", models.TextField(blank=True, null=True)),
                ("datare_secol_sursa", models.TextField(blank=True, null=True)),
                ("pisanie_traducere", models.TextField(blank=True, null=True)),
                ("pisanie_secol_detalii", models.TextField(blank=True, null=True)),
                ("pisanie_secol_sursa", models.TextField(blank=True, null=True)),
                ("biserica", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="biserici.biserica")),
            ],
            options={
                "verbose_name_plural": "storic Biserici",
            },
        ),
    ]
