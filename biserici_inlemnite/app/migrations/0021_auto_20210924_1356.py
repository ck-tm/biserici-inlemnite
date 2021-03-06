# Generated by Django 3.1.13 on 2021-09-24 10:56

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclatoare', '0010_historicaltiparcbolta_tiparcbolta'),
        ('app', '0020_auto_20210924_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='istoricpage',
            name='datare_prin_interval_timp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='istoricpage',
            name='datare_secol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_biserici', to='nomenclatoare.secol'),
        ),
        migrations.AddField(
            model_name='istoricpage',
            name='datare_secol_detalii',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AddField(
            model_name='istoricpage',
            name='datare_secol_sursa',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Sursa'),
        ),
        migrations.AddField(
            model_name='istoricpage',
            name='pisanie_secol_detalii',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AddField(
            model_name='istoricpage',
            name='pisanie_secol_sursa',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Sursa'),
        ),
        migrations.AddField(
            model_name='istoricpage',
            name='pisanie_traducere',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Traducere'),
        ),
        migrations.AddField(
            model_name='istoricpage',
            name='studiu_dendocronologic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nomenclatoare.studiudendocronologic'),
        ),
        migrations.AddField(
            model_name='istoricpage',
            name='sursa_datare',
            field=models.ManyToManyField(blank=True, related_name='p_biserici', to='nomenclatoare.SursaDatare'),
        ),
        migrations.CreateModel(
            name='Ctitori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('nume', models.CharField(max_length=250)),
                ('detalii', wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Observații')),
                ('sursa', wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Observații')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='ctitori', to='app.istoricpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
