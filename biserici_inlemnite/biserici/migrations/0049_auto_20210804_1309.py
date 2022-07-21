# Generated by Django 3.1.13 on 2021-08-04 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("biserici", "0048_auto_20210804_1305"),
    ]

    operations = [
        migrations.AddField(
            model_name="conservare",
            name="completare",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="descriere",
            name="completare",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="finisaj",
            name="completare",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="fotografii",
            name="completare",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="historicalconservare",
            name="completare",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="historicaldescriere",
            name="completare",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="historicalfinisaj",
            name="completare",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="historicalfotografii",
            name="completare",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="historicalidentificare",
            name="completare",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="historicalpatrimoniu",
            name="completare",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="identificare",
            name="completare",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="patrimoniu",
            name="completare",
            field=models.FloatField(default=0),
        ),
    ]
