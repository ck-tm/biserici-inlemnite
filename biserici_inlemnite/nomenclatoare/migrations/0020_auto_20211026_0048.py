# Generated by Django 3.1.13 on 2021-10-25 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import wagtail.search.index


class Migration(migrations.Migration):

    dependencies = [
        ('biserici', '0052_auto_20210916_2325'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0077_auto_20211026_0032'),
        ('nomenclatoare', '0019_auto_20211026_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialBolta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Materiale Boltă',
                'ordering': ['nume'],
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
        migrations.CreateModel(
            name='MaterialCruci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Materiale Cruci',
                'ordering': ['nume'],
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
        migrations.RenameModel(
            old_name='ElementBiserica',
            new_name='ElementInteriorBiserică',
        ),
        migrations.RenameModel(
            old_name='HistoricalElementBiserica',
            new_name='HistoricalElementInteriorBiserică',
        ),
        migrations.AlterModelOptions(
            name='finisaj',
            options={'ordering': ['nume'], 'verbose_name_plural': 'Finisaje biserică'},
        ),
        migrations.AlterModelOptions(
            name='historicalelementinteriorbiserică',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical element interior biserică'},
        ),
        migrations.AlterModelOptions(
            name='peisagisticasit',
            options={'ordering': ['nume'], 'verbose_name_plural': 'Peisagistica sitului'},
        ),
        migrations.AlterModelOptions(
            name='relatiecimitir',
            options={'ordering': ['nume'], 'verbose_name_plural': 'Relația cu cimitirul'},
        ),
        migrations.CreateModel(
            name='HistoricalMaterialCruci',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('nume', models.CharField(max_length=150)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical material cruci',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalMaterialBolta',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('nume', models.CharField(max_length=150)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical material bolta',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
