# Generated by Django 3.1.13 on 2021-11-05 15:35

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0105_auto_20211105_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='descrierepage',
            name='sistem_structural_observatii',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Observații'),
        ),
    ]
