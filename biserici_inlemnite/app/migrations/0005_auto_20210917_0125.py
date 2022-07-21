# Generated by Django 3.1.13 on 2021-09-16 22:25

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_auto_20210917_0038"),
    ]

    operations = [
        migrations.AlterField(
            model_name="identificarepage",
            name="denumire_actuala",
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name="Actuală"),
        ),
        migrations.AlterField(
            model_name="identificarepage",
            name="denumire_locala",
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name="Locală"),
        ),
        migrations.AlterField(
            model_name="identificarepage",
            name="denumire_oberservatii",
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name="Observații"),
        ),
        migrations.AlterField(
            model_name="identificarepage",
            name="denumire_precedenta",
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name="Precendentă"),
        ),
    ]
