# Generated by Django 3.1.13 on 2021-07-14 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biserica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Judet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=50)),
                ('cod', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Localitate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=50)),
                ('judet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biserici.judet')),
            ],
        ),
        migrations.CreateModel(
            name='Identificare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitudine', models.FloatField(blank=True, null=True)),
                ('longitudine', models.FloatField(blank=True, null=True)),
                ('statut', models.CharField(blank=True, choices=[(1, 'Clasat UNESCO (importanță mondială)'), (2, 'Clasat Categoria A (importanță națională)'), (3, 'Clasat Categoria B (importanță regională)'), (4, 'Neclasat'), (5, 'În curs de clasare'), (6, 'În curs de declasare'), (7, 'Decalasat parțial')], max_length=2, null=True)),
                ('biserica', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='biserici.biserica')),
                ('judet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biserici.judet')),
                ('localitate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biserici.localitate')),
            ],
        ),
    ]
