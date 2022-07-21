# Generated by Django 3.1.13 on 2022-07-20 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fragmente', '0007_amplasareturle_amplasareturn_asezaretalpiturn_dimensiuneturn_elementecomponenteiconostas_esentalemno'),
        ('biserici', '0064_auto_20220719_0351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interventie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denumire_oficiala', models.CharField(blank=True, max_length=250, null=True, verbose_name='Denumire')),
                ('datat', models.BooleanField(default=False, verbose_name='Datat')),
                ('an', models.IntegerField(blank=True, null=True, verbose_name='An')),
                ('neconforma', models.BooleanField(default=False, verbose_name='Neconformă')),
                ('sursa', models.TextField(blank=True, null=True, verbose_name='Sursa')),
                ('observatii', models.TextField(blank=True, null=True, verbose_name='Observații')),
                ('imagini', models.ManyToManyField(blank=True, to='biserici.Fotografie')),
            ],
        ),
        migrations.CreateModel(
            name='Loc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observatii', models.TextField(blank=True, null=True, verbose_name='Observații')),
                ('imagini', models.ManyToManyField(blank=True, to='biserici.Fotografie')),
                ('tip_loc', models.ManyToManyField(blank=True, to='fragmente.TipLoc')),
            ],
        ),
        migrations.CreateModel(
            name='Toponim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exista', models.BooleanField(default=False, verbose_name='Există')),
                ('denumire', models.TextField(blank=True, null=True, verbose_name='Denumire')),
                ('sursa', models.TextField(blank=True, null=True, verbose_name='Sursă informații')),
                ('observatii', models.TextField(blank=True, null=True, verbose_name='Observații')),
            ],
        ),
        migrations.AlterField(
            model_name='peisajpeisajcultural',
            name='observatii',
            field=models.TextField(blank=True, null=True, verbose_name='Observații'),
        ),
        migrations.CreateModel(
            name='StareDeConservare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriere_degradari', models.TextField(blank=True, null=True, verbose_name='Descriere degradări')),
                ('descriere_risc', models.TextField(blank=True, null=True, verbose_name='Descriere risc')),
                ('observatii', models.TextField(blank=True, null=True, verbose_name='Observații')),
                ('imagini', models.ManyToManyField(blank=True, to='biserici.Fotografie')),
                ('interventii_necesare', models.ManyToManyField(blank=True, to='fragmente.InterventiiNecesare')),
                ('nota', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fragmente.notastareconservare')),
                ('tipul_de_degradari', models.ManyToManyField(blank=True, to='fragmente.TipDegradare')),
                ('tipul_riscului', models.ManyToManyField(blank=True, to='fragmente.TipRisc')),
            ],
        ),
        migrations.CreateModel(
            name='RelatiaCuCimitirul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observatii', models.TextField(blank=True, null=True, verbose_name='Observații')),
                ('tip_relatie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fragmente.tiprelatiecucimitirul')),
            ],
        ),
        migrations.CreateModel(
            name='PeisajAmplasament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interventii', models.ManyToManyField(blank=True, to='biserici.Interventie', verbose_name='Intervenții')),
                ('loc', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='biserici.loc', verbose_name='Loc')),
                ('relatia_cu_cimitirul', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='biserici.relatiacucimitirul', verbose_name='Relația cu cimitirul')),
                ('stare_de_conservare', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='biserici.staredeconservare', verbose_name='Stare de Conservare')),
                ('toponim', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='biserici.toponim', verbose_name='Toponim')),
            ],
        ),
    ]
