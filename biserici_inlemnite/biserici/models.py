from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from guardian.shortcuts import get_objects_for_user, assign_perm, remove_perm

User = get_user_model()

IDENTIFICARE_DOC_CADASTRALE = (
    (1, 'Da'),
    (2, 'Nu'),
    (3, 'În curs de'),
)

class Judet(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=50)
    cod = models.CharField(max_length=2)
    

    class Meta:
        verbose_name_plural = "Județe"

    def __str__(self):
        return self.nume

class Localitate(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=50)
    judet = models.ForeignKey('Judet', on_delete=models.CASCADE)
    

    class Meta:
        verbose_name_plural = "Localități"


    def __str__(self):
        return self.nume


class Biserica(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=50)

    last_edit_date = models.DateTimeField(auto_now=True)
    last_edit_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Biserici"

    def __str__(self):
        return self.nume


    def completare(self):
        return 0

class FunctiuneBiserica(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Funcțiuni Biserică"

    def __str__(self):
        return self.nume


class StatutBiserica(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Statuturi Biserică"

    def __str__(self):
        return self.nume


class CultBiserica(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Culturi Biserică"

    def __str__(self):
        return self.nume


class UtilizareBiserica(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Utilizări Biserică"

    def __str__(self):
        return self.nume


class SingularitateBiserica(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Singularități Biserică"

    def __str__(self):
        return self.nume


class ProprietateBiserica(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Proprietăți Biserică"

    def __str__(self):
        return self.nume


class Identificare(models.Model):
    """
    Capitol: Identificare Biserica
    """
    biserica = models.OneToOneField('Biserica', on_delete=models.CASCADE)
    judet = models.ForeignKey('Judet', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici')
    localitate = models.ForeignKey('Localitate', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici')
    latitudine = models.FloatField(null=True, blank=True)
    longitudine = models.FloatField(null=True, blank=True)
    statut = models.ForeignKey('StatutBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici')
    denumire_actuala = models.CharField(max_length=150, null=True, blank=True)
    denumire_precedenta = models.CharField(max_length=150, null=True, blank=True)
    denumire_locala = models.CharField(max_length=150, null=True, blank=True)
    denumire_oberservatii = models.TextField(null=True, blank=True)
    cult = models.ForeignKey('CultBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici')
    utilizare = models.ForeignKey('UtilizareBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici')
    utilizare_detalii = models.TextField(null=True, blank=True)
    singularitate = models.ForeignKey('SingularitateBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici')
    singularitate_detalii = models.TextField(null=True, blank=True)
    functiune = models.ForeignKey('FunctiuneBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici')
    functiune_detalii = models.TextField(null=True, blank=True)
    functiune_initiala = models.ForeignKey('FunctiuneBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici_initiale')
    functiune_initiala_detalii = models.TextField(null=True, blank=True)
    proprietate_actuala = models.ForeignKey('ProprietateBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici_initiale')
    proprietate_detalii = models.TextField(null=True, blank=True)
    proprietar_actual = models.TextField(null=True, blank=True)
    inscriere_documente_cadastrale = models.IntegerField(choices=IDENTIFICARE_DOC_CADASTRALE, null=True, blank=True)

    last_edit_date = models.DateTimeField(auto_now=True)
    last_edit_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Identificare Biserici"

    def __str__(self):
        return f"Identificare {self.biserica.nume}"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_judet = self.judet

    def save(self, *args, **kwargs):
        print(kwargs)
        if self.judet:
            if self.__original_judet != self.judet or kwargs.get('force_update', False) == True:
                biserica = self.biserica

                judet_biserica = self.judet.nume
                grup_judet, _ = Group.objects.get_or_create(name=judet_biserica)
                assign_perm('view_biserica', grup_judet, biserica)
                assign_perm('change_biserica', grup_judet, biserica)

                for t in ['identificare', 'istoric', 'descriere', 'patrimoniu', 'conservare']:
                        assign_perm(f'view_{t}', grup_judet, getattr(biserica, t))
                        assign_perm(f'change_{t}', grup_judet, getattr(biserica, t))

                for judet in Group.objects.exclude(name=judet_biserica):
                    remove_perm('view_biserica', judet, biserica)
                    remove_perm('change_biserica', judet, biserica)

                    for t in ['identificare', 'istoric', 'descriere', 'patrimoniu', 'conservare']:
                        remove_perm(f'view_{t}', judet, getattr(biserica, t))
                        remove_perm(f'change_{t}', judet, getattr(biserica, t))
        super().save(*args, **kwargs)

class MutareBiserica(models.Model):
    """
    Description: Model Description
    """
    istoric = models.ForeignKey('Istoric', on_delete=models.CASCADE)
    localitate = models.ForeignKey('Localitate', null=True, blank=True, on_delete=models.SET_NULL)
    latitudine = models.FloatField(null=True, blank=True)
    longitudine = models.FloatField(null=True, blank=True)

    class Meta:
        pass


class Istoric(models.Model):
    """
    Capitol: Istoric Biserica
    """

    biserica = models.OneToOneField('Biserica', on_delete=models.CASCADE)
    ctitor = models.TextField(null=True, blank=True)
    pisanie = models.TextField(null=True, blank=True)
    mesteri = models.TextField(null=True, blank=True)
    zugravi = models.TextField(null=True, blank=True)
    personalitati = models.TextField(null=True, blank=True)

    last_edit_date = models.DateTimeField(auto_now=True)
    last_edit_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Istoric Biserici"

    def __str__(self):
        return f"Istoric {self.biserica.nume}"


class Descriere(models.Model):
    """
    Capitol: Descriere Biserica
    """

    biserica = models.OneToOneField('Biserica', on_delete=models.CASCADE)

    last_edit_date = models.DateTimeField(auto_now=True)
    last_edit_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Descriere Biserici"

    def __str__(self):
        return f"Descriere {self.biserica.nume}"


class Patrimoniu(models.Model):
    """
    Capitol: Valoare Patrimoniu Cultural Biserica
    """
    biserica = models.OneToOneField('Biserica', on_delete=models.CASCADE)
    
    last_edit_date = models.DateTimeField(auto_now=True)
    last_edit_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Valoare patrimoniu cultural Biserici"

    def __str__(self):
        return f"Valoare patrimoniu cultural {self.biserica.nume}"


class Conservare(models.Model):
    """
    Capitol: Stare conservare Biserica
    """
    biserica = models.OneToOneField('Biserica', on_delete=models.CASCADE)

    last_edit_date = models.DateTimeField(auto_now=True)
    last_edit_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Stare conservare Biserici"

    def __str__(self):
        return f"Stare conservare {self.biserica.nume}"