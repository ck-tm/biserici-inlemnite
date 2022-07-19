from django.db import models
from django.contrib import admin
from simple_history.models import HistoricalRecords

class GenericAdmin(admin.ModelAdmin):
    pass


class Judet(models.Model):
    nume = models.CharField(max_length=50)
    cod = models.CharField(max_length=2)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Județe"
        ordering = ['nume']

    def __str__(self):
        return self.nume


class Comuna(models.Model):
    nume = models.CharField(max_length=50)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Comune"
        ordering = ['nume']

    def __str__(self):
        return self.nume


class Localitate(models.Model):
    nume = models.CharField(max_length=50)
    judet = models.ForeignKey('Judet', on_delete=models.CASCADE)
    comuna = models.ForeignKey(
        'Comuna', on_delete=models.CASCADE, null=True, blank=True)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Localități"
        ordering = ['nume']

    def __str__(self):
        if self.comuna:
            return f"{self.nume}, com. {self.comuna.nume}"
        return self.nume


class CategorieObiectiv(models.Model):
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Categorie Obiectiv"
        ordering = ['nume']

    def __str__(self):
        return self.nume

class Statut(models.Model):
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Statut"
        ordering = ['nume']

    def __str__(self):
        return self.nume

class Hram(models.Model):
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Hram"
        ordering = ['nume']

    def __str__(self):
        return self.nume

class Cult(models.Model):
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Cult"
        ordering = ['nume']

    def __str__(self):
        return self.nume

class FrecventaUtilizarii(models.Model):
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Frecvența Utilizării"
        ordering = ['nume']

    def __str__(self):
        return self.nume


class Singularitate(models.Model):
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Singularitate"
        ordering = ['nume']

    def __str__(self):
        return self.nume

class TipArtera(models.Model):
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip arteră"
        ordering = ['nume']

    def __str__(self):
        return self.nume

class TipRegimProprietate(models.Model):
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipul Regimului de Proprietate"
        ordering = ['nume']

    def __str__(self):
        return self.nume


class TipFormaRelief(models.Model):
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipul Formei de Relief"
        ordering = ['nume']

    def __str__(self):
        return self.nume

class TipReperHidrografic(models.Model):
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipul Reperului Hidrografic"
        ordering = ['nume']

    def __str__(self):
        return self.nume


class TipZoneNaturale(models.Model):
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Zone Naturale (Arii Protejate)"
        ordering = ['nume']

    def __str__(self):
        return self.nume



class Bibliografie(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Bibliografie"
        ordering = ['nume']

    def __str__(self):
        return self.nume


class JustificareDatare(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Justificare Datare"
        ordering = ['nume']

    def __str__(self):
        return self.nume



class TipPisanie(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip pisanie"
        ordering = ['nume']

    def __str__(self):
        return self.nume


class Secol(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Secole"
        ordering = ['nume']

    def __str__(self):
        return self.nume


class TipCadruPeisaj(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Cadru Peisaj"
        ordering = ['nume']

    def __str__(self):
        return self.nume


admin.site.register(Judet, GenericAdmin)
admin.site.register(Comuna, GenericAdmin)
admin.site.register(Localitate, GenericAdmin)
admin.site.register(CategorieObiectiv, GenericAdmin)
admin.site.register(Statut, GenericAdmin)
admin.site.register(Hram, GenericAdmin)
admin.site.register(Cult, GenericAdmin)
admin.site.register(FrecventaUtilizarii, GenericAdmin)
admin.site.register(Singularitate, GenericAdmin)
admin.site.register(TipArtera, GenericAdmin)
admin.site.register(TipRegimProprietate, GenericAdmin)
admin.site.register(TipFormaRelief, GenericAdmin)
admin.site.register(TipReperHidrografic, GenericAdmin)
admin.site.register(TipZoneNaturale, GenericAdmin)
admin.site.register(Bibliografie, GenericAdmin)
admin.site.register(JustificareDatare, GenericAdmin)
admin.site.register(TipPisanie, GenericAdmin)
admin.site.register(Secol, GenericAdmin)
admin.site.register(TipCadruPeisaj, GenericAdmin)