# Generated by Django 3.1.13 on 2022-07-18 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biserici', '0053_auto_20211028_2308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalbiserica',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical biserica', 'verbose_name_plural': 'historical  Biserici'},
        ),
        migrations.AlterModelOptions(
            name='historicalcomponentaartistica',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical componenta artistica', 'verbose_name_plural': 'historical 3.3 Componenta Artistică'},
        ),
        migrations.AlterModelOptions(
            name='historicalconservare',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical conservare', 'verbose_name_plural': 'historical 5. Stare de conservare'},
        ),
        migrations.AlterModelOptions(
            name='historicaldescriere',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical descriere', 'verbose_name_plural': 'historical 3. Descriere'},
        ),
        migrations.AlterModelOptions(
            name='historicalfinisaj',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical finisaj', 'verbose_name_plural': 'historical 3.2 Finisaje'},
        ),
        migrations.AlterModelOptions(
            name='historicalfinisajactualinvelitoare',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical finisaj actual invelitoare', 'verbose_name_plural': 'historical finisaj actual invelitoares'},
        ),
        migrations.AlterModelOptions(
            name='historicalfinisajaltar',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical finisaj altar', 'verbose_name_plural': 'historical finisaj altars'},
        ),
        migrations.AlterModelOptions(
            name='historicalfinisajanteriorinvelitoare',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical finisaj anterior invelitoare', 'verbose_name_plural': 'historical finisaj anterior invelitoares'},
        ),
        migrations.AlterModelOptions(
            name='historicalfinisajbolti',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical finisaj bolti', 'verbose_name_plural': 'historical finisaj boltis'},
        ),
        migrations.AlterModelOptions(
            name='historicalfinisajinvelitoareturn',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical finisaj invelitoare turn', 'verbose_name_plural': 'historical finisaj invelitoare turns'},
        ),
        migrations.AlterModelOptions(
            name='historicalfinisajnaos',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical finisaj naos', 'verbose_name_plural': 'historical finisaj naoss'},
        ),
        migrations.AlterModelOptions(
            name='historicalfinisajpardosea',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical finisaj pardosea', 'verbose_name_plural': 'historical finisaj pardoseas'},
        ),
        migrations.AlterModelOptions(
            name='historicalfinisajperetiinterior',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical finisaj pereti interior', 'verbose_name_plural': 'historical finisaj pereti interiors'},
        ),
        migrations.AlterModelOptions(
            name='historicalfinisajportic',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical finisaj portic', 'verbose_name_plural': 'historical finisaj portics'},
        ),
        migrations.AlterModelOptions(
            name='historicalfinisajpronaos',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical finisaj pronaos', 'verbose_name_plural': 'historical finisaj pronaoss'},
        ),
        migrations.AlterModelOptions(
            name='historicalfinisajtamburturn',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical finisaj tambur turn', 'verbose_name_plural': 'historical finisaj tambur turns'},
        ),
        migrations.AlterModelOptions(
            name='historicalfinisajtavan',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical finisaj tavan', 'verbose_name_plural': 'historical finisaj tavans'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografieansamblu',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie ansamblu', 'verbose_name_plural': 'historical fotografie ansamblus'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografiecheotoar',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie cheotoar', 'verbose_name_plural': 'historical fotografie cheotoars'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografiecrucebiserica',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie cruce biserica', 'verbose_name_plural': 'historical fotografie cruce bisericas'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografiedegradariexterioare',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie degradari exterioare', 'verbose_name_plural': 'historical fotografie degradari exterioares'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografiedegradariinterior',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie degradari interior', 'verbose_name_plural': 'historical fotografie degradari interiors'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografiedegradaripod',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie degradari pod', 'verbose_name_plural': 'historical fotografie degradari pods'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografiedetaliubolta',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie detaliu bolta', 'verbose_name_plural': 'historical fotografie detaliu boltas'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografiedetaliuimaginepereti',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie detaliu imagine pereti', 'verbose_name_plural': 'historical fotografie detaliu imagine peretis'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografiedetaliupod',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie detaliu pod', 'verbose_name_plural': 'historical fotografie detaliu pods'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografiedetaliusculptura',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie detaliu sculptura', 'verbose_name_plural': 'historical fotografie detaliu sculpturas'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografiefatada',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie fatada', 'verbose_name_plural': 'historical fotografie fatadas'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografiefereastra',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie fereastra', 'verbose_name_plural': 'historical fotografie fereastras'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografieicoana',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie icoana', 'verbose_name_plural': 'historical fotografie icoanas'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografieiconostasaltar',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie iconostas altar', 'verbose_name_plural': 'historical fotografie iconostas altars'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografieiconostasnaos',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie iconostas naos', 'verbose_name_plural': 'historical fotografie iconostas naoss'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografieinteriordesfasurat',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie interior desfasurat', 'verbose_name_plural': 'historical fotografie interior desfasurats'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografieinvelitoare',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie invelitoare', 'verbose_name_plural': 'historical fotografie invelitoares'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografiemobiliercandelabre',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie mobilier candelabre', 'verbose_name_plural': 'historical fotografie mobilier candelabres'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografieobiectcult',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie obiect cult', 'verbose_name_plural': 'historical fotografie obiect cults'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografiepisanieinscriptiectitormester',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie pisanie inscriptie ctitor mester', 'verbose_name_plural': 'historical fotografie pisanie inscriptie ctitor mesters'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografieportal',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie portal', 'verbose_name_plural': 'historical fotografie portals'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografieportalnaos',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie portal naos', 'verbose_name_plural': 'historical fotografie portal naoss'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografieportalpronaos',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie portal pronaos', 'verbose_name_plural': 'historical fotografie portal pronaoss'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografieprogramiconografic',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie program iconografic', 'verbose_name_plural': 'historical fotografie program iconografics'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografiestreasina',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie streasina', 'verbose_name_plural': 'historical fotografie streasinas'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografietalpa',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie talpa', 'verbose_name_plural': 'historical fotografie talpas'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografieturn',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie turn', 'verbose_name_plural': 'historical fotografie turns'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografieurmesemnesimboluri',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografie urme semne simboluri', 'verbose_name_plural': 'historical fotografie urme semne simboluris'},
        ),
        migrations.AlterModelOptions(
            name='historicalfotografii',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical fotografii', 'verbose_name_plural': 'historical 3.1 Fotografii'},
        ),
        migrations.AlterModelOptions(
            name='historicalidentificare',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical identificare', 'verbose_name_plural': 'historical 1. Identificare'},
        ),
        migrations.AlterModelOptions(
            name='historicalistoric',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical istoric', 'verbose_name_plural': 'historical 2. Istoric'},
        ),
        migrations.AlterModelOptions(
            name='historicalpatrimoniu',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical patrimoniu', 'verbose_name_plural': 'historical 4. Valoare Patrimoniu Cultural'},
        ),
        migrations.AlterModelOptions(
            name='historicalpicturaexterioara',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical pictura exterioara', 'verbose_name_plural': 'historical pictura exterioaras'},
        ),
        migrations.AlterModelOptions(
            name='historicalpicturainterioara',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical pictura interioara', 'verbose_name_plural': 'historical pictura interioaras'},
        ),
        migrations.AlterModelOptions(
            name='historicalpovestebiserica',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical poveste biserica', 'verbose_name_plural': 'historical Povești Biserică'},
        ),
        migrations.AlterModelOptions(
            name='historicaluser',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical user', 'verbose_name_plural': 'historical users'},
        ),
        migrations.AlterField(
            model_name='historicalbiserica',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalcomponentaartistica',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalconservare',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicaldescriere',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfinisaj',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfinisajactualinvelitoare',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfinisajaltar',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfinisajanteriorinvelitoare',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfinisajbolti',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfinisajinvelitoareturn',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfinisajnaos',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfinisajpardosea',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfinisajperetiinterior',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfinisajportic',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfinisajpronaos',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfinisajtamburturn',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfinisajtavan',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografieansamblu',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografiecheotoar',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografiecrucebiserica',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografiedegradariexterioare',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografiedegradariinterior',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografiedegradaripod',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografiedetaliubolta',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografiedetaliuimaginepereti',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografiedetaliupod',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografiedetaliusculptura',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografiefatada',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografiefereastra',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografieicoana',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografieiconostasaltar',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografieiconostasnaos',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografieinteriordesfasurat',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografieinvelitoare',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografiemobiliercandelabre',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografieobiectcult',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografiepisanieinscriptiectitormester',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografieportal',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografieportalnaos',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografieportalpronaos',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografieprogramiconografic',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografiestreasina',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografietalpa',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografieturn',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografieurmesemnesimboluri',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfotografii',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalidentificare',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalistoric',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalpatrimoniu',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalpicturaexterioara',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalpicturainterioara',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalpovestebiserica',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicaluser',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]