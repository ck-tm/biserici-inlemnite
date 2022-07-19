# Generated by Django 3.1.13 on 2022-07-18 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('fragmente', '0006_historicaltipcadrupeisaj_tipcadrupeisaj'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('biserici', '0062_auto_20220718_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalistoric',
            name='cadru',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Nume'),
        ),
        migrations.AddField(
            model_name='istoric',
            name='cadru',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Nume'),
        ),
        migrations.AlterField(
            model_name='historicalidentificare',
            name='codul_lmi',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Codul LMI'),
        ),
        migrations.AlterField(
            model_name='identificare',
            name='codul_lmi',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Codul LMI'),
        ),
        migrations.CreateModel(
            name='PeisajPeisajCulturalPatrimoniuImaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exista', models.BooleanField(default=False, verbose_name='Există')),
                ('descriere', models.TextField(blank=True, null=True, verbose_name='Descriere')),
                ('foto', models.ManyToManyField(blank=True, to='biserici.Fotografie')),
            ],
        ),
        migrations.CreateModel(
            name='PeisajPeisajCulturalCadru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ManyToManyField(blank=True, to='biserici.Fotografie')),
                ('tip', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='fragmente.tipcadrupeisaj', verbose_name='Tip Cadru')),
            ],
        ),
        migrations.CreateModel(
            name='PeisajPeisajCultural',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sinteza', models.TextField(blank=True, null=True, verbose_name='Sinteză')),
                ('observatii', models.TextField(blank=True, null=True, verbose_name='observații')),
                ('cadru', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='biserici.peisajpeisajculturalcadru')),
                ('patrimoniu_imaterial', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='biserici.peisajpeisajculturalpatrimoniuimaterial', verbose_name='Patrimoniu Imaterial')),
            ],
        ),
        migrations.CreateModel(
            name='Peisaj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biserica', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='peisaj', to='biserici.biserica')),
                ('peisaj_cultural', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biserici.peisajpeisajcultural', verbose_name='Scurt Istoric')),
            ],
            options={
                'verbose_name': 'Peisaj',
                'verbose_name_plural': 'Peisaj',
                'ordering': ['biserica__the_order'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalPeisaj',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('biserica', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='biserici.biserica')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('peisaj_cultural', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='biserici.peisajpeisajcultural', verbose_name='Scurt Istoric')),
            ],
            options={
                'verbose_name': 'historical Peisaj',
                'verbose_name_plural': 'historical Peisaj',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]