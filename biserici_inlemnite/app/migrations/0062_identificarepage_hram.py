# Generated by Django 3.1.13 on 2021-10-14 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclatoare', '0016_historicalhram_hram'),
        ('app', '0061_auto_20211005_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='identificarepage',
            name='hram',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_biserici', to='nomenclatoare.hram'),
        ),
    ]
