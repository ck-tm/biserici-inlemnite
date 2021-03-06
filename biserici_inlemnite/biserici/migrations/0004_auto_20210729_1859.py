# Generated by Django 3.1.13 on 2021-07-29 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclatoare', '0003_auto_20210729_1859'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('biserici', '0003_auto_20210729_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='descriere',
            name='detalii_elemente',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='descriere',
            name='detalii_elemente_importante',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='descriere',
            name='elemente',
            field=models.ManyToManyField(help_text='Elemente ansamblu construit', to='nomenclatoare.ElementBiserica'),
        ),
        migrations.AddField(
            model_name='descriere',
            name='elemente_importante',
            field=models.ManyToManyField(help_text='Elemente ansamblu construit', to='nomenclatoare.ElementImportant'),
        ),
        migrations.AddField(
            model_name='descriere',
            name='peisagistica_sitului',
            field=models.ManyToManyField(to='nomenclatoare.PeisagisticaSit'),
        ),
        migrations.AddField(
            model_name='descriere',
            name='relatia_cu_cimitirul',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nomenclatoare.relatiecimitir'),
        ),
        migrations.AddField(
            model_name='descriere',
            name='toponim_sursa',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicaldescriere',
            name='detalii_elemente',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicaldescriere',
            name='detalii_elemente_importante',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicaldescriere',
            name='relatia_cu_cimitirul',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='nomenclatoare.relatiecimitir'),
        ),
        migrations.AddField(
            model_name='historicaldescriere',
            name='toponim_sursa',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='PovesteBiserica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalii', models.TextField()),
                ('sursa', models.TextField()),
                ('istoric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.istoric')),
            ],
            options={
                'verbose_name_plural': 'Pove??ti Biseric??',
            },
        ),
        migrations.CreateModel(
            name='InterventieBiserica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datat', models.BooleanField(default=False)),
                ('an', models.IntegerField(blank=True, null=True)),
                ('observatii', models.TextField(blank=True, null=True)),
                ('sursa', models.TextField(blank=True, null=True)),
                ('este_ultima_interventie', models.BooleanField(default=False)),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomenclatoare.elementbiserica')),
                ('istoric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.istoric')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalPovesteBiserica',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('detalii', models.TextField()),
                ('sursa', models.TextField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('istoric', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='biserici.istoric')),
            ],
            options={
                'verbose_name': 'historical poveste biserica',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Fotografii',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biserica', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='biserici.biserica')),
            ],
        ),
        migrations.CreateModel(
            name='FotografieTurn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
        migrations.CreateModel(
            name='FotografieTalpa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
        migrations.CreateModel(
            name='FotografieStreasina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
        migrations.CreateModel(
            name='FotografiePortalPronaos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
        migrations.CreateModel(
            name='FotografiePortalNaos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
        migrations.CreateModel(
            name='FotografiePortal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
        migrations.CreateModel(
            name='FotografiePisanieInscriptieCtitorMester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
        migrations.CreateModel(
            name='FotografieObiectCult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
        migrations.CreateModel(
            name='FotografieMobilierCandelabre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
        migrations.CreateModel(
            name='FotografieInvelitoare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
        migrations.CreateModel(
            name='FotografieInteriorDesfasurat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
        migrations.CreateModel(
            name='FotografieIconostasNaos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
        migrations.CreateModel(
            name='FotografieIconostasAltar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
        migrations.CreateModel(
            name='FotografieIcoana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
        migrations.CreateModel(
            name='FotografieFereastra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
        migrations.CreateModel(
            name='FotografieFatada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
        migrations.CreateModel(
            name='FotografieDetaliuPod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('detaliu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomenclatoare.detaliupodturn')),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
        migrations.CreateModel(
            name='FotografieDetaliuBolta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
        migrations.CreateModel(
            name='FotografieDegradariPod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
        migrations.CreateModel(
            name='FotografieDegradariInterior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
        migrations.CreateModel(
            name='FotografieDegradariExterioare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
        migrations.CreateModel(
            name='FotografieCruceBiserica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
        migrations.CreateModel(
            name='FotografieCheotoar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
        migrations.CreateModel(
            name='FotografieAnsamblu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poza', models.ImageField(max_length=250, upload_to='fotografii')),
                ('detalii', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('fotografii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.fotografii')),
            ],
        ),
    ]
