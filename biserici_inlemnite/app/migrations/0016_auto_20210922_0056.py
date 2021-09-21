# Generated by Django 3.1.13 on 2021-09-21 21:56

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20210922_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='conservarepage',
            name='tamplarii',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Stare'),
        ),
        migrations.AddField(
            model_name='conservarepage',
            name='tamplarii_detalii',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AddField(
            model_name='conservarepage',
            name='tamplarii_pericol',
            field=models.BooleanField(default=False, verbose_name='Pericol'),
        ),
    ]
