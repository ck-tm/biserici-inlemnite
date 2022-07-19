# Generated by Django 3.1.13 on 2022-07-18 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('fragmente', '0003_historicaltipartera_historicaltipregimproprietate_tipartera_tipregimproprietate'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('biserici', '0056_auto_20220718_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalizareAdresaCoordonateGPS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitudine', models.FloatField(blank=True, null=True)),
                ('longitudine', models.FloatField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Unități Teritoriale',
            },
        ),
        migrations.CreateModel(
            name='LocalizareReferinteCadastrale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr_carte_funciara', models.CharField(blank=True, max_length=50, null=True, verbose_name='Număr carte funciară')),
                ('nr_cadastru', models.IntegerField(blank=True, null=True, verbose_name='Număr cadastru')),
                ('nr_cop_cadastru', models.CharField(blank=True, max_length=150, null=True, verbose_name='Număr cop conform cadastru')),
                ('nr_parcela', models.IntegerField(blank=True, null=True, verbose_name='Număr parcelă / topografic')),
                ('suprafata_parcela', models.IntegerField(blank=True, null=True, verbose_name='Suprafață parcelă')),
                ('observatii', models.TextField(blank=True, null=True, verbose_name='Observații')),
            ],
            options={
                'verbose_name': 'Referințe Cadastrale',
            },
        ),
        migrations.CreateModel(
            name='LocalizareUnitatiTeritoriale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat', models.CharField(blank=True, max_length=50, null=True)),
                ('regiune', models.CharField(blank=True, max_length=50, null=True)),
                ('uat_1', models.CharField(blank=True, max_length=50, null=True, verbose_name='UAT 1 (superior)')),
                ('uat', models.CharField(blank=True, max_length=50, null=True, verbose_name='UAT (intermediar)')),
                ('uat_2', models.CharField(blank=True, max_length=50, null=True, verbose_name='UAT 2 (inferior)')),
                ('ut', models.CharField(blank=True, max_length=50, null=True, verbose_name='UT')),
            ],
            options={
                'verbose_name': 'Unități Teritoriale',
            },
        ),
        migrations.AlterField(
            model_name='descriere',
            name='bolta_peste_altar_observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='descriere',
            name='bolta_peste_naos_observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='descriere',
            name='bolta_peste_pronaos_observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='descriere',
            name='cor_observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='descriere',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='descriere',
            name='turn_observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='finisaj',
            name='finisaj_exterior_observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='finisajactualinvelitoare',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='finisajaltar',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='finisajanteriorinvelitoare',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='finisajbolti',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='finisajinvelitoareturn',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='finisajnaos',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='finisajpardosea',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='finisajperetiinterior',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='finisajportic',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='finisajpronaos',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='finisajtamburturn',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='finisajtavan',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='historicaldescriere',
            name='bolta_peste_altar_observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='historicaldescriere',
            name='bolta_peste_naos_observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='historicaldescriere',
            name='bolta_peste_pronaos_observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='historicaldescriere',
            name='cor_observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='historicaldescriere',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='historicaldescriere',
            name='turn_observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='historicalfinisaj',
            name='finisaj_exterior_observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='historicalfinisajactualinvelitoare',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='historicalfinisajaltar',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='historicalfinisajanteriorinvelitoare',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='historicalfinisajbolti',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='historicalfinisajinvelitoareturn',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='historicalfinisajnaos',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='historicalfinisajpardosea',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='historicalfinisajperetiinterior',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='historicalfinisajportic',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='historicalfinisajpronaos',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='historicalfinisajtamburturn',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='historicalfinisajtavan',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='identificarefrecventautilizarii',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='identificaresingularitate',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.AlterField(
            model_name='interventiebiserica',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.CreateModel(
            name='LocalizareRegimulDeProprietate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observatii', models.TextField(blank=True, null=True, verbose_name='Observații')),
                ('tip_regim', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='biserici', to='fragmente.tipregimproprietate', verbose_name='Tipul Regimului de Proprietate')),
            ],
            options={
                'verbose_name': 'Regimul de Proprietate',
            },
        ),
        migrations.CreateModel(
            name='LocalizareAdresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denumire_artera', models.CharField(blank=True, max_length=50, null=True, verbose_name='Denumire Arteră')),
                ('nr_postal', models.IntegerField(blank=True, null=True, verbose_name='Număr Poștal')),
                ('cod_postal', models.IntegerField(blank=True, null=True, verbose_name='Cod Poștal')),
                ('observatii', models.TextField(blank=True, null=True, verbose_name='Observații')),
                ('coordonate_gps', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biserici.localizareadresacoordonategps', verbose_name='Coordonate GPS')),
                ('tip_artera', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='biserici', to='fragmente.tipartera')),
            ],
            options={
                'verbose_name': 'Adresă',
            },
        ),
        migrations.CreateModel(
            name='Localizare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresa', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biserici.localizareadresa', verbose_name='Adresă')),
                ('biserica', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='biserici.biserica')),
                ('referinte_cadastrale', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biserici.localizarereferintecadastrale', verbose_name='Referințe Cadastrale')),
                ('regim_proprietate', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biserici.localizareregimuldeproprietate', verbose_name='Regimul de Proprietate')),
                ('unitati_teritoriale', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biserici.localizareunitatiteritoriale', verbose_name='Unități Teritoriale')),
            ],
            options={
                'verbose_name': 'Localizare / Proprietate',
                'verbose_name_plural': 'Localizare / Proprietate',
                'ordering': ['biserica__the_order'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalLocalizare',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('adresa', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='biserici.localizareadresa', verbose_name='Adresă')),
                ('biserica', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='biserici.biserica')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('referinte_cadastrale', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='biserici.localizarereferintecadastrale', verbose_name='Referințe Cadastrale')),
                ('regim_proprietate', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='biserici.localizareregimuldeproprietate', verbose_name='Regimul de Proprietate')),
                ('unitati_teritoriale', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='biserici.localizareunitatiteritoriale', verbose_name='Unități Teritoriale')),
            ],
            options={
                'verbose_name': 'historical Localizare / Proprietate',
                'verbose_name_plural': 'historical Localizare / Proprietate',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]