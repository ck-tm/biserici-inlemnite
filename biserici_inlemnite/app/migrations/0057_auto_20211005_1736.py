# Generated by Django 3.1.13 on 2021-10-05 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclatoare', '0015_auto_20211005_1736'),
        ('app', '0056_auto_20210929_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descrierepage',
            name='interventii_invelitoare_etape_anterioare_vizibile',
            field=models.BooleanField(default=False, verbose_name='Vizibile'),
        ),
        migrations.AlterField(
            model_name='descrierepage',
            name='interventii_invelitoare_sindrila_cu_horj',
            field=models.BooleanField(default=False, verbose_name='Cu horj'),
        ),
        migrations.AlterField(
            model_name='descrierepage',
            name='interventii_invelitoare_sindrila_cu_tesitura',
            field=models.BooleanField(default=False, verbose_name='Cu teșitură'),
        ),
        migrations.AlterField(
            model_name='descrierepage',
            name='interventii_invelitoare_sindrila_numar_straturi',
            field=models.IntegerField(blank=True, null=True, verbose_name='Număr straturi'),
        ),
        migrations.AlterField(
            model_name='descrierepage',
            name='interventii_invelitoare_sindrila_pasul_latuirii',
            field=models.IntegerField(blank=True, null=True, verbose_name='Pasul lățuirii'),
        ),
        migrations.AlterField(
            model_name='descrierepage',
            name='interventii_invelitoare_sindrlia_esenta_lemnoasa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='interventii_invelitoare', to='nomenclatoare.esentalemnoasa', verbose_name='Esența lemnoasă'),
        ),
        migrations.AlterField(
            model_name='descrierepage',
            name='interventii_invelitoare_sindrlia_forma_botului',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='interventii_invelitoare', to='nomenclatoare.tipbotsindrila', verbose_name='Forma botului'),
        ),
        migrations.AlterField(
            model_name='descrierepage',
            name='interventii_invelitoare_sindrlia_tipul_de_batere',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='interventii_invelitoare', to='nomenclatoare.tipbateresindrila', verbose_name='Tipul de batere'),
        ),
    ]
