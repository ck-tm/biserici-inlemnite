# Generated by Django 3.1.13 on 2022-07-18 16:01

from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('biserici', '0058_historicalreperegeografice_reperegeografice_reperegeograficeformarelief_reperegeograficereperhidrogr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fotografie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlu', models.CharField(blank=True, max_length=150, null=True)),
                ('fisier', models.ImageField(max_length=200, upload_to='fotografii')),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'verbose_name_plural': 'Fotografii',
            },
        ),
        migrations.CreateModel(
            name='HistoricalFotografie',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('titlu', models.CharField(blank=True, max_length=150, null=True)),
                ('fisier', models.TextField(max_length=200)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical fotografie',
                'verbose_name_plural': 'historical Fotografii',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalIstoricB',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Istoric',
                'verbose_name_plural': 'historical Istoric',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='IstoricB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Istoric',
                'verbose_name_plural': 'Istoric',
                'ordering': ['biserica__the_order'],
            },
        ),
        migrations.CreateModel(
            name='IstoricEveniment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observatii', models.TextField(blank=True, null=True, verbose_name='Observații')),
            ],
        ),
        migrations.CreateModel(
            name='IstoricMutare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresa', models.TextField(blank=True, null=True, verbose_name='Adresa')),
                ('latitudine', models.FloatField(blank=True, null=True)),
                ('longitudine', models.FloatField(blank=True, null=True)),
                ('observatii', models.TextField(blank=True, null=True, verbose_name='Observații')),
                ('sursa', models.TextField(blank=True, null=True, verbose_name='Sursa')),
            ],
        ),
        migrations.CreateModel(
            name='IstoricPersoana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nume')),
                ('observatii', models.TextField(blank=True, null=True, verbose_name='Observații')),
                ('sursa', models.TextField(blank=True, null=True, verbose_name='Sursa')),
            ],
        ),
        migrations.CreateModel(
            name='IstoricPisanie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Text')),
            ],
        ),
        migrations.CreateModel(
            name='IstoricScurtIstoric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sinteza', models.TextField(blank=True, null=True, verbose_name='Sinteză istorică')),
            ],
        ),
        migrations.CreateModel(
            name='IstoricScurtIstoricDatare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('an', models.IntegerField(blank=True, null=True, verbose_name='An')),
                ('interval_timp', models.CharField(blank=True, max_length=50, null=True, verbose_name='Datare prin interval de timp')),
            ],
        ),
        migrations.CreateModel(
            name='IstoricScurtIstoricJustificareDatare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observatii', models.TextField(blank=True, null=True, verbose_name='Observații')),
            ],
        ),
        migrations.RemoveField(
            model_name='historicalpovestebiserica',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalpovestebiserica',
            name='istoric',
        ),
        migrations.RemoveField(
            model_name='interventiebiserica',
            name='element',
        ),
        migrations.RemoveField(
            model_name='interventiebiserica',
            name='istoric',
        ),
        migrations.RemoveField(
            model_name='istoric',
            name='biserica',
        ),
        migrations.RemoveField(
            model_name='istoric',
            name='ctitori',
        ),
        migrations.RemoveField(
            model_name='istoric',
            name='datare_secol',
        ),
        migrations.RemoveField(
            model_name='istoric',
            name='evenimente',
        ),
        migrations.RemoveField(
            model_name='istoric',
            name='mesteri',
        ),
        migrations.RemoveField(
            model_name='istoric',
            name='mutari_biserica',
        ),
        migrations.RemoveField(
            model_name='istoric',
            name='personalitati',
        ),
        migrations.RemoveField(
            model_name='istoric',
            name='studiu_dendocronologic',
        ),
        migrations.RemoveField(
            model_name='istoric',
            name='sursa_datare',
        ),
        migrations.RemoveField(
            model_name='istoric',
            name='zugravi',
        ),
        migrations.RemoveField(
            model_name='povestebiserica',
            name='istoric',
        ),
        migrations.RemoveField(
            model_name='componentaartistica',
            name='completare',
        ),
        migrations.RemoveField(
            model_name='componentaartistica',
            name='missing_fields',
        ),
        migrations.RemoveField(
            model_name='conservare',
            name='completare',
        ),
        migrations.RemoveField(
            model_name='conservare',
            name='missing_fields',
        ),
        migrations.RemoveField(
            model_name='descriere',
            name='completare',
        ),
        migrations.RemoveField(
            model_name='descriere',
            name='missing_fields',
        ),
        migrations.RemoveField(
            model_name='finisaj',
            name='completare',
        ),
        migrations.RemoveField(
            model_name='finisaj',
            name='missing_fields',
        ),
        migrations.RemoveField(
            model_name='fotografii',
            name='completare',
        ),
        migrations.RemoveField(
            model_name='fotografii',
            name='missing_fields',
        ),
        migrations.RemoveField(
            model_name='historicalcomponentaartistica',
            name='completare',
        ),
        migrations.RemoveField(
            model_name='historicalcomponentaartistica',
            name='missing_fields',
        ),
        migrations.RemoveField(
            model_name='historicalconservare',
            name='completare',
        ),
        migrations.RemoveField(
            model_name='historicalconservare',
            name='missing_fields',
        ),
        migrations.RemoveField(
            model_name='historicaldescriere',
            name='completare',
        ),
        migrations.RemoveField(
            model_name='historicaldescriere',
            name='missing_fields',
        ),
        migrations.RemoveField(
            model_name='historicalfinisaj',
            name='completare',
        ),
        migrations.RemoveField(
            model_name='historicalfinisaj',
            name='missing_fields',
        ),
        migrations.RemoveField(
            model_name='historicalfotografii',
            name='completare',
        ),
        migrations.RemoveField(
            model_name='historicalfotografii',
            name='missing_fields',
        ),
        migrations.RemoveField(
            model_name='historicalpatrimoniu',
            name='completare',
        ),
        migrations.RemoveField(
            model_name='historicalpatrimoniu',
            name='missing_fields',
        ),
        migrations.RemoveField(
            model_name='patrimoniu',
            name='completare',
        ),
        migrations.RemoveField(
            model_name='patrimoniu',
            name='missing_fields',
        ),
        migrations.AlterField(
            model_name='reperegeografice',
            name='biserica',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='repere_geografice', to='biserici.biserica'),
        ),
        migrations.DeleteModel(
            name='HistoricalIstoric',
        ),
        migrations.DeleteModel(
            name='HistoricalPovesteBiserica',
        ),
        migrations.DeleteModel(
            name='InterventieBiserica',
        ),
    ]