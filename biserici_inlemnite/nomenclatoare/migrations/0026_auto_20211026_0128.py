# Generated by Django 3.1.13 on 2021-10-25 22:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import wagtail.search.index


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nomenclatoare', '0025_auto_20211026_0125'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialIconostas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Materiale Iconostas',
                'ordering': ['nume'],
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
        migrations.AlterModelOptions(
            name='obiectcult',
            options={'ordering': ['nume'], 'verbose_name_plural': 'Obiecte de Cult'},
        ),
        migrations.AlterModelOptions(
            name='tehnicaiconostas',
            options={'ordering': ['nume'], 'verbose_name_plural': 'Tehnici Iconostas'},
        ),
        migrations.CreateModel(
            name='HistoricalMaterialIconostas',
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
                'verbose_name': 'historical material iconostas',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
