# Generated by Django 3.1.13 on 2021-09-21 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0014_auto_20210922_0034"),
    ]

    operations = [
        migrations.RenameField(
            model_name="conservarepage",
            old_name="sarpanta_turn",
            new_name="turn",
        ),
        migrations.RenameField(
            model_name="conservarepage",
            old_name="structura_turn_detalii",
            new_name="turn_detalii",
        ),
        migrations.RenameField(
            model_name="conservarepage",
            old_name="sarpanta_turn_pericol",
            new_name="turn_pericol",
        ),
        migrations.RemoveField(
            model_name="conservarepage",
            name="sarpanta_turn_detalii",
        ),
        migrations.RemoveField(
            model_name="conservarepage",
            name="structura_turn",
        ),
        migrations.RemoveField(
            model_name="conservarepage",
            name="structura_turn_pericol",
        ),
    ]
