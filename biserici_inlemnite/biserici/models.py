from django.db import models






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
    Description: Model Description
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


    class Meta:
        verbose_name_plural = "Identificări Biserici"

    def __str__(self):
        return f"Identificare {self.biserica.nume}"