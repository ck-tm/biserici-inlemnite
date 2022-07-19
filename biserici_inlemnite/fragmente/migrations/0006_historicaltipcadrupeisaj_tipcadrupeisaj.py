# Generated by Django 3.1.13 on 2022-07-18 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fragmente', '0005_bibliografie_historicalbibliografie_historicaljustificaredatare_historicalsecol_historicaltippisanie'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipCadruPeisaj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Tip Cadru Peisaj',
                'ordering': ['nume'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalTipCadruPeisaj',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('nume', models.CharField(max_length=300)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical tip cadru peisaj',
                'verbose_name_plural': 'historical Tip Cadru Peisaj',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]