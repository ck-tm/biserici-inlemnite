# Generated by Django 3.1.13 on 2021-08-03 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biserici', '0027_auto_20210803_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalpicturainterioara',
            old_name='tehnica',
            new_name='tehnica_pictura',
        ),
        migrations.RenameField(
            model_name='picturainterioara',
            old_name='tehnica',
            new_name='tehnica_pictura',
        ),
    ]
