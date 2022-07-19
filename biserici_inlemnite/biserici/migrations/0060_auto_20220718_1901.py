# Generated by Django 3.1.13 on 2022-07-18 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biserici', '0059_auto_20220718_1901'),
        ('nomenclatoare', '0031_auto_20220718_1901'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fragmente', '0005_bibliografie_historicalbibliografie_historicaljustificaredatare_historicalsecol_historicaltippisanie'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Istoric',
        ),
        migrations.DeleteModel(
            name='PovesteBiserica',
        ),
        migrations.AddField(
            model_name='istoricscurtistoricjustificaredatare',
            name='categorie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='biserici', to='fragmente.justificaredatare', verbose_name='Justificare Datare'),
        ),
        migrations.AddField(
            model_name='istoricscurtistoricjustificaredatare',
            name='foto',
            field=models.ManyToManyField(blank=True, to='biserici.Fotografie'),
        ),
        migrations.AddField(
            model_name='istoricscurtistoricdatare',
            name='secol',
            field=models.ManyToManyField(blank=True, related_name='biserici', to='fragmente.Secol', verbose_name='Secol'),
        ),
        migrations.AddField(
            model_name='istoricscurtistoric',
            name='bibliografie',
            field=models.ManyToManyField(blank=True, related_name='biserici', to='fragmente.Bibliografie', verbose_name='Bibliografie'),
        ),
        migrations.AddField(
            model_name='istoricscurtistoric',
            name='datare',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biserici.istoricscurtistoricdatare', verbose_name='Pisanie'),
        ),
        migrations.AddField(
            model_name='istoricscurtistoric',
            name='justificare_datare',
            field=models.ManyToManyField(blank=True, to='biserici.IstoricScurtIstoricJustificareDatare', verbose_name='Pisanie'),
        ),
        migrations.AddField(
            model_name='istoricpisanie',
            name='tip',
            field=models.ManyToManyField(blank=True, related_name='biserici', to='fragmente.TipPisanie', verbose_name='Tip Pisanie'),
        ),
        migrations.AddField(
            model_name='istoricpersoana',
            name='foto',
            field=models.ManyToManyField(blank=True, to='biserici.Fotografie'),
        ),
        migrations.AddField(
            model_name='istoricmutare',
            name='localitate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='biserici', to='fragmente.localitate', verbose_name='Tipul Formei de Relief'),
        ),
        migrations.AddField(
            model_name='istoricb',
            name='biserica',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='istoricb', to='biserici.biserica'),
        ),
        migrations.AddField(
            model_name='istoricb',
            name='ctitori',
            field=models.ManyToManyField(blank=True, related_name='ctitori', to='biserici.IstoricPersoana', verbose_name='Ctitori'),
        ),
        migrations.AddField(
            model_name='istoricb',
            name='evenimente',
            field=models.ManyToManyField(blank=True, related_name='evenimente', to='biserici.IstoricEveniment', verbose_name='Evenimente'),
        ),
        migrations.AddField(
            model_name='istoricb',
            name='mesteri',
            field=models.ManyToManyField(blank=True, related_name='mesteri', to='biserici.IstoricPersoana', verbose_name='Meșteri'),
        ),
        migrations.AddField(
            model_name='istoricb',
            name='mutari',
            field=models.ManyToManyField(blank=True, related_name='mutari', to='biserici.IstoricMutare', verbose_name='Mutări'),
        ),
        migrations.AddField(
            model_name='istoricb',
            name='personalitati',
            field=models.ManyToManyField(blank=True, related_name='personalitati', to='biserici.IstoricPersoana', verbose_name='Personalități'),
        ),
        migrations.AddField(
            model_name='istoricb',
            name='pisanie',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biserici.istoricpisanie', verbose_name='Pisanie'),
        ),
        migrations.AddField(
            model_name='istoricb',
            name='scurt_istoric',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biserici.istoricscurtistoric', verbose_name='Scurt Istoric'),
        ),
        migrations.AddField(
            model_name='istoricb',
            name='zugravi',
            field=models.ManyToManyField(blank=True, related_name='zugravi', to='biserici.IstoricPersoana', verbose_name='Zugravi'),
        ),
        migrations.AddField(
            model_name='historicalistoricb',
            name='biserica',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='biserici.biserica'),
        ),
        migrations.AddField(
            model_name='historicalistoricb',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalistoricb',
            name='pisanie',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='biserici.istoricpisanie', verbose_name='Pisanie'),
        ),
        migrations.AddField(
            model_name='historicalistoricb',
            name='scurt_istoric',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='biserici.istoricscurtistoric', verbose_name='Scurt Istoric'),
        ),
        migrations.AddField(
            model_name='historicalfotografie',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]