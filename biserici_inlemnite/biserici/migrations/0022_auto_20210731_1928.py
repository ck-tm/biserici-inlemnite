# Generated by Django 3.1.13 on 2021-07-31 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nomenclatoare", "0008_historicalmobilier_historicalobiectcult_mobilier_obiectcult"),
        ("biserici", "0021_auto_20210731_1849"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="historicalcomponentaartistica",
            name="mobiliere",
        ),
        migrations.RemoveField(
            model_name="historicalcomponentaartistica",
            name="obiecte_de_cult",
        ),
        migrations.RemoveField(
            model_name="componentaartistica",
            name="mobiliere",
        ),
        migrations.AddField(
            model_name="componentaartistica",
            name="mobiliere",
            field=models.ManyToManyField(blank=True, to="nomenclatoare.Material", verbose_name="Mobilier"),
        ),
        migrations.AlterField(
            model_name="componentaartistica",
            name="mobiliere_detalii",
            field=models.TextField(
                blank=True,
                help_text="strane, scaun arhieresc, tetrapoade, bănucuțe, cuiere, anvone, cafas, cor",
                null=True,
            ),
        ),
        migrations.RemoveField(
            model_name="componentaartistica",
            name="obiecte_de_cult",
        ),
        migrations.AddField(
            model_name="componentaartistica",
            name="obiecte_de_cult",
            field=models.ManyToManyField(blank=True, to="nomenclatoare.ObiectCult", verbose_name="Obiecte de cult"),
        ),
        migrations.AlterField(
            model_name="historicalcomponentaartistica",
            name="mobiliere_detalii",
            field=models.TextField(
                blank=True,
                help_text="strane, scaun arhieresc, tetrapoade, bănucuțe, cuiere, anvone, cafas, cor",
                null=True,
            ),
        ),
    ]
