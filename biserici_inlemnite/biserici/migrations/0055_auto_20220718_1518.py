# Generated by Django 3.1.13 on 2022-07-18 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "fragmente",
            "0002_categorieobiectiv_cult_frecventautilizarii_historicalcategorieobiectiv_historicalcult_historicalfrec",
        ),
        ("nomenclatoare", "0030_auto_20220718_1503"),
        ("biserici", "0054_auto_20220718_1503"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="historicalidentificare",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical Identificare / Denumire / Funcțiune",
                "verbose_name_plural": "historical Identificare / Denumire / Funcțiune",
            },
        ),
        migrations.AlterModelOptions(
            name="identificare",
            options={
                "ordering": ["biserica__the_order"],
                "verbose_name": "Identificare / Denumire / Funcțiune",
                "verbose_name_plural": "Identificare / Denumire / Funcțiune",
            },
        ),
        migrations.RemoveField(
            model_name="historicalidentificare",
            name="adresa",
        ),
        migrations.RemoveField(
            model_name="historicalidentificare",
            name="completare",
        ),
        migrations.RemoveField(
            model_name="historicalidentificare",
            name="denumire_actuala",
        ),
        migrations.RemoveField(
            model_name="historicalidentificare",
            name="denumire_locala",
        ),
        migrations.RemoveField(
            model_name="historicalidentificare",
            name="denumire_oberservatii",
        ),
        migrations.RemoveField(
            model_name="historicalidentificare",
            name="denumire_precedenta",
        ),
        migrations.RemoveField(
            model_name="historicalidentificare",
            name="functiune",
        ),
        migrations.RemoveField(
            model_name="historicalidentificare",
            name="functiune_detalii",
        ),
        migrations.RemoveField(
            model_name="historicalidentificare",
            name="functiune_initiala",
        ),
        migrations.RemoveField(
            model_name="historicalidentificare",
            name="functiune_initiala_detalii",
        ),
        migrations.RemoveField(
            model_name="historicalidentificare",
            name="inscriere_documente_cadastrale",
        ),
        migrations.RemoveField(
            model_name="historicalidentificare",
            name="judet",
        ),
        migrations.RemoveField(
            model_name="historicalidentificare",
            name="latitudine",
        ),
        migrations.RemoveField(
            model_name="historicalidentificare",
            name="localitate",
        ),
        migrations.RemoveField(
            model_name="historicalidentificare",
            name="longitudine",
        ),
        migrations.RemoveField(
            model_name="historicalidentificare",
            name="missing_fields",
        ),
        migrations.RemoveField(
            model_name="historicalidentificare",
            name="proprietar_actual",
        ),
        migrations.RemoveField(
            model_name="historicalidentificare",
            name="proprietate_actuala",
        ),
        migrations.RemoveField(
            model_name="historicalidentificare",
            name="proprietate_detalii",
        ),
        migrations.RemoveField(
            model_name="historicalidentificare",
            name="singularitate_detalii",
        ),
        migrations.RemoveField(
            model_name="historicalidentificare",
            name="utilizare",
        ),
        migrations.RemoveField(
            model_name="historicalidentificare",
            name="utilizare_detalii",
        ),
        migrations.RemoveField(
            model_name="identificare",
            name="adresa",
        ),
        migrations.RemoveField(
            model_name="identificare",
            name="completare",
        ),
        migrations.RemoveField(
            model_name="identificare",
            name="denumire_actuala",
        ),
        migrations.RemoveField(
            model_name="identificare",
            name="denumire_locala",
        ),
        migrations.RemoveField(
            model_name="identificare",
            name="denumire_oberservatii",
        ),
        migrations.RemoveField(
            model_name="identificare",
            name="denumire_precedenta",
        ),
        migrations.RemoveField(
            model_name="identificare",
            name="functiune",
        ),
        migrations.RemoveField(
            model_name="identificare",
            name="functiune_detalii",
        ),
        migrations.RemoveField(
            model_name="identificare",
            name="functiune_initiala",
        ),
        migrations.RemoveField(
            model_name="identificare",
            name="functiune_initiala_detalii",
        ),
        migrations.RemoveField(
            model_name="identificare",
            name="inscriere_documente_cadastrale",
        ),
        migrations.RemoveField(
            model_name="identificare",
            name="judet",
        ),
        migrations.RemoveField(
            model_name="identificare",
            name="latitudine",
        ),
        migrations.RemoveField(
            model_name="identificare",
            name="localitate",
        ),
        migrations.RemoveField(
            model_name="identificare",
            name="longitudine",
        ),
        migrations.RemoveField(
            model_name="identificare",
            name="missing_fields",
        ),
        migrations.RemoveField(
            model_name="identificare",
            name="proprietar_actual",
        ),
        migrations.RemoveField(
            model_name="identificare",
            name="proprietate_actuala",
        ),
        migrations.RemoveField(
            model_name="identificare",
            name="proprietate_detalii",
        ),
        migrations.RemoveField(
            model_name="identificare",
            name="singularitate_detalii",
        ),
        migrations.RemoveField(
            model_name="identificare",
            name="utilizare",
        ),
        migrations.RemoveField(
            model_name="identificare",
            name="utilizare_detalii",
        ),
        migrations.AddField(
            model_name="descriere",
            name="adresa",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="descriere",
            name="judet",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="biserici",
                to="nomenclatoare.judet",
            ),
        ),
        migrations.AddField(
            model_name="descriere",
            name="latitudine",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="descriere",
            name="localitate",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="biserici",
                to="nomenclatoare.localitate",
            ),
        ),
        migrations.AddField(
            model_name="descriere",
            name="longitudine",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="historicaldescriere",
            name="adresa",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="historicaldescriere",
            name="judet",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="nomenclatoare.judet",
            ),
        ),
        migrations.AddField(
            model_name="historicaldescriere",
            name="latitudine",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="historicaldescriere",
            name="localitate",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="nomenclatoare.localitate",
            ),
        ),
        migrations.AddField(
            model_name="historicaldescriere",
            name="longitudine",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="historicalidentificare",
            name="categoria",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="fragmente.categorieobiectiv",
            ),
        ),
        migrations.AddField(
            model_name="historicalidentificare",
            name="codul_lmi",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="historicalidentificare",
            name="denumire_oficiala",
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name="Denumire oficială actuală LMI"),
        ),
        migrations.AddField(
            model_name="historicalidentificare",
            name="frecventa_utilizarii",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="fragmente.frecventautilizarii",
                verbose_name="Frecvența utilizării",
            ),
        ),
        migrations.AddField(
            model_name="historicalidentificare",
            name="hram",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="fragmente.hram",
            ),
        ),
        migrations.AddField(
            model_name="identificare",
            name="categoria",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="biserici",
                to="fragmente.categorieobiectiv",
            ),
        ),
        migrations.AddField(
            model_name="identificare",
            name="codul_lmi",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="identificare",
            name="denumire_oficiala",
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name="Denumire oficială actuală LMI"),
        ),
        migrations.AddField(
            model_name="identificare",
            name="frecventa_utilizarii",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="biserici",
                to="fragmente.frecventautilizarii",
                verbose_name="Frecvența utilizării",
            ),
        ),
        migrations.AddField(
            model_name="identificare",
            name="hram",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="biserici",
                to="fragmente.hram",
            ),
        ),
        migrations.AlterField(
            model_name="historicalidentificare",
            name="cult",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="fragmente.cult",
            ),
        ),
        migrations.AlterField(
            model_name="historicalidentificare",
            name="singularitate",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="fragmente.singularitate",
            ),
        ),
        migrations.AlterField(
            model_name="historicalidentificare",
            name="statut",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="fragmente.statut",
            ),
        ),
        migrations.AlterField(
            model_name="identificare",
            name="cult",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="biserici",
                to="fragmente.cult",
            ),
        ),
        migrations.AlterField(
            model_name="identificare",
            name="singularitate",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="biserici",
                to="fragmente.singularitate",
            ),
        ),
        migrations.AlterField(
            model_name="identificare",
            name="statut",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="biserici",
                to="fragmente.statut",
            ),
        ),
    ]
