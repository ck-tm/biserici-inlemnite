# Generated by Django 3.1.13 on 2021-07-14 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biserici', '0008_auto_20210714_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identificare',
            name='last_edit_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
