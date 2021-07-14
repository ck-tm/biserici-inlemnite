from django.db import models
from django.contrib.auth import get_user_model


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



class Istoric(models.Model):
    """
    Capitol: Istoric Biserica
    """
    biserica = models.OneToOneField('Biserica', on_delete=models.CASCADE)
    
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


class ValoarePatrimoniuCultural(models.Model):
    """
    Capitol: Valoare Patrimoniu Cultural Biserica
    """
    biserica = models.OneToOneField('Biserica', on_delete=models.CASCADE, related_name='patrimoniu')
    
    last_edit_date = models.DateTimeField(auto_now=True)
    last_edit_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Valoare patrimoniu cultural Biserici"

    def __str__(self):
        return f"Valoare patrimoniu cultural {self.biserica.nume}"


class StareConservare(models.Model):
    """
    Capitol: Stare conservare Biserica
    """
    biserica = models.OneToOneField('Biserica', on_delete=models.CASCADE, related_name='conservare')
    
    last_edit_date = models.DateTimeField(auto_now=True)
    last_edit_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Stare conservare Biserici"

    def __str__(self):
        return f"Stare conservare {self.biserica.nume}"