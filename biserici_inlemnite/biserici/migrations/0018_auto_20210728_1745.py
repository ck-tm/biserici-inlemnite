# Generated by Django 3.1.13 on 2021-07-28 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biserici', '0017_auto_20210728_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='istoric',
            name='anul_constructiei',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='istoric',
            name='ctitori',
            field=models.ManyToManyField(related_name='ctitor', through='biserici.CtitorBiserica', to='biserici.Persoana'),
        ),
        migrations.AddField(
            model_name='istoric',
            name='datare_prin_interval_timp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='istoric',
            name='datare_secol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biserici.secol'),
        ),
        migrations.AddField(
            model_name='istoric',
            name='datare_secol_detalii',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='istoric',
            name='datare_secol_sursa',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='istoric',
            name='evenimente',
            field=models.ManyToManyField(through='biserici.EvenimentIstoric', to='biserici.Eveniment'),
        ),
        migrations.AddField(
            model_name='istoric',
            name='mesteri',
            field=models.ManyToManyField(related_name='mester', through='biserici.MesterBiserica', to='biserici.Persoana'),
        ),
        migrations.AddField(
            model_name='istoric',
            name='mutari_biserica',
            field=models.ManyToManyField(through='biserici.MutareBiserica', to='biserici.Localitate'),
        ),
        migrations.AddField(
            model_name='istoric',
            name='personalitati',
            field=models.ManyToManyField(related_name='personalitate', through='biserici.PersonalitateBiserica', to='biserici.Persoana'),
        ),
        migrations.AddField(
            model_name='istoric',
            name='pisanie_secol_detalii',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='istoric',
            name='pisanie_secol_sursa',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='istoric',
            name='pisanie_traducere',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='istoric',
            name='studii_anterioare',
            field=models.ManyToManyField(through='biserici.StudiuIstoric', to='biserici.Studiu'),
        ),
        migrations.AddField(
            model_name='istoric',
            name='studiu_dendocronologic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biserici.studiudendocronologic'),
        ),
        migrations.AddField(
            model_name='istoric',
            name='sursa_datare',
            field=models.ManyToManyField(to='biserici.SursaDatare'),
        ),
        migrations.AddField(
            model_name='istoric',
            name='zugravi',
            field=models.ManyToManyField(related_name='zugrav', through='biserici.ZugravBiserica', to='biserici.Persoana'),
        ),
    ]
