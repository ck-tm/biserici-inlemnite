# Generated by Django 3.1.13 on 2021-10-25 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0086_auto_20211026_0130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='componentaartisticapage',
            old_name='altar_piciorul_mesei_new',
            new_name='altar_piciorul_mesei',
        ),
        migrations.RenameField(
            model_name='componentaartisticapage',
            old_name='altar_placa_mesei_new',
            new_name='altar_placa_mesei',
        ),
        migrations.RenameField(
            model_name='componentaartisticapage',
            old_name='iconostas_naos_altar_materiale_new',
            new_name='iconostas_naos_altar_materiale',
        ),
        migrations.RenameField(
            model_name='componentaartisticapage',
            old_name='mobiliere_new',
            new_name='mobiliere',
        ),
        migrations.RenameField(
            model_name='descrierepage',
            old_name='bolta_peste_altar_material_new',
            new_name='bolta_peste_altar_material',
        ),
        migrations.RenameField(
            model_name='descrierepage',
            old_name='bolta_peste_naos_material_new',
            new_name='bolta_peste_naos_material',
        ),
        migrations.RenameField(
            model_name='descrierepage',
            old_name='bolta_peste_pronaos_material_new',
            new_name='bolta_peste_pronaos_material',
        ),
        migrations.RenameField(
            model_name='descrierepage',
            old_name='cor_material_new',
            new_name='cor_material',
        ),
        migrations.RenameField(
            model_name='descrierepage',
            old_name='inchidere_tambur_turn_material_new',
            new_name='inchidere_tambur_turn_material',
        ),
        migrations.RenameField(
            model_name='descrierepage',
            old_name='invelitoare_corp_material_new',
            new_name='invelitoare_corp_material',
        ),
        migrations.RenameField(
            model_name='descrierepage',
            old_name='invelitoare_turle_material_new',
            new_name='invelitoare_turle_material',
        ),
        migrations.RenameField(
            model_name='descrierepage',
            old_name='invelitoare_turn_material_new',
            new_name='invelitoare_turn_material',
        ),
        migrations.RenameField(
            model_name='descrierepage',
            old_name='sarpanta_material_cruci_new',
            new_name='sarpanta_material_cruci',
        ),
    ]
