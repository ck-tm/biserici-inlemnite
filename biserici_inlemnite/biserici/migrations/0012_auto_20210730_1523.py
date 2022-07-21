# Generated by Django 3.1.13 on 2021-07-30 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("biserici", "0011_finisaj_finisaj_tambur_turn"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="finisaj",
            name="finisaj_actual_invelitoare",
        ),
        migrations.RemoveField(
            model_name="finisaj",
            name="finisaj_tambur_turn",
        ),
        migrations.AddField(
            model_name="finisajinvelitoare",
            name="finisaj",
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to="biserici.finisaj"),
            preserve_default=False,
        ),
    ]
