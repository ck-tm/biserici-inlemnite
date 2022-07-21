# Generated by Django 3.1.13 on 2021-09-16 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0062_comment_models_and_pagesubscription"),
        ("nomenclatoare", "0010_historicaltiparcbolta_tiparcbolta"),
        ("app", "0002_auto_20210916_2341"),
    ]

    operations = [
        migrations.CreateModel(
            name="IdentificarePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("adresa", models.CharField(blank=True, max_length=250, null=True)),
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
                (
                    "cult",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="p_biserici",
                        to="nomenclatoare.cultbiserica",
                    ),
                ),
                (
                    "functiune",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="p_biserici",
                        to="nomenclatoare.functiunebiserica",
                    ),
                ),
                (
                    "functiune_initiala",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="p_biserici_initiale",
                        to="nomenclatoare.functiunebiserica",
                    ),
                ),
                (
                    "judet",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="p_biserici",
                        to="nomenclatoare.judet",
                    ),
                ),
                (
                    "localitate",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="p_biserici",
                        to="nomenclatoare.localitate",
                    ),
                ),
                (
                    "proprietate_actuala",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="p_biserici_initiale",
                        to="nomenclatoare.proprietatebiserica",
                    ),
                ),
                (
                    "singularitate",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="p_biserici",
                        to="nomenclatoare.singularitatebiserica",
                    ),
                ),
                (
                    "statut",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="p_biserici",
                        to="nomenclatoare.statutbiserica",
                    ),
                ),
                (
                    "utilizare",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="p_biserici",
                        to="nomenclatoare.utilizarebiserica",
                    ),
                ),
            ],
            options={
                "verbose_name": "Identificare",
                "verbose_name_plural": "Identificare",
            },
            bases=("wagtailcore.page",),
        ),
    ]
