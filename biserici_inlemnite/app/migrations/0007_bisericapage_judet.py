# Generated by Django 3.1.13 on 2021-09-16 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclatoare', '0010_historicaltiparcbolta_tiparcbolta'),
        ('app', '0006_componentaartisticapage_conservarepage_descrierepage_finisajpage_istoricpage_patrimoniupage'),
    ]

    operations = [
        migrations.AddField(
            model_name='bisericapage',
            name='judet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pp_biserici', to='nomenclatoare.judet'),
        ),
    ]
