# Generated by Django 3.1.13 on 2021-10-05 14:43

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0023_add_choose_permissions"),
        ("app", "0057_auto_20211005_1736"),
    ]

    operations = [
        migrations.CreateModel(
            name="PozeEtapeIstoriceVizibile",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("sort_order", models.IntegerField(blank=True, editable=False, null=True)),
                ("observatii", wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name="Observații")),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="poze", to="app.etapeistoricevizibile"
                    ),
                ),
                (
                    "poza",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]
