# Generated by Django 3.1.13 on 2021-07-30 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biserici', '0018_auto_20210731_0202'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='componentaartistica',
            options={'ordering': ['biserica__the_order'], 'verbose_name_plural': 'Componenta Artistică'},
        ),
        migrations.AlterModelOptions(
            name='conservare',
            options={'ordering': ['biserica__the_order'], 'verbose_name_plural': 'Stare conservare Biserici'},
        ),
        migrations.AlterModelOptions(
            name='descriere',
            options={'ordering': ['biserica__the_order'], 'verbose_name_plural': 'Descriere Biserici'},
        ),
        migrations.AlterModelOptions(
            name='finisaj',
            options={'ordering': ['biserica__the_order'], 'verbose_name_plural': 'Finisaje'},
        ),
        migrations.AlterModelOptions(
            name='fotografii',
            options={'ordering': ['biserica__the_order'], 'verbose_name_plural': 'Fotografii'},
        ),
        migrations.AlterModelOptions(
            name='identificare',
            options={'ordering': ['biserica__the_order'], 'verbose_name_plural': 'Identificare Biserici'},
        ),
        migrations.AlterModelOptions(
            name='istoric',
            options={'ordering': ['biserica__the_order'], 'verbose_name_plural': 'Istoric Biserici'},
        ),
        migrations.AlterModelOptions(
            name='patrimoniu',
            options={'ordering': ['biserica__the_order'], 'verbose_name_plural': 'Valoare Patrimoniu'},
        ),
        migrations.AlterField(
            model_name='biserica',
            name='the_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='historicalbiserica',
            name='the_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
