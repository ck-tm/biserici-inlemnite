# Generated by Django 3.1.13 on 2022-07-20 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "fragmente",
            "0007_amplasareturle_amplasareturn_asezaretalpiturn_dimensiuneturn_elementecomponenteiconostas_esentalemno",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="historicaltipmaterialstructuraboltatavan",
            name="history_user",
        ),
        migrations.DeleteModel(
            name="TipMaterialStructuraBoltaTavan",
        ),
        migrations.DeleteModel(
            name="HistoricalTipMaterialStructuraBoltaTavan",
        ),
    ]
