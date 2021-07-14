from django.contrib import admin

# Register your models here.
from biserici import models


@admin.register(models.Localitate)
class LocalitateAdmin(admin.ModelAdmin):
    list_display = ['nume', 'nr_biserici']
    search_fields = ["nume"]
    list_filter = ["judet"]

    def nr_biserici(self, obj):
        return obj.biserici.count()


@admin.register(models.Judet)
class JudetAdmin(admin.ModelAdmin):
    list_display = ['nume', 'cod', 'nr_biserici']
    search_fields = ["nume"]

    def nr_biserici(self, obj):
       return obj.biserici.count()


@admin.register(models.StatutBiserica)
class StatutBisericaAdmin(admin.ModelAdmin):
    list_display = ['nume', 'nr_biserici']
    search_fields = ["nume"]

    def nr_biserici(self, obj):
       return obj.biserici.count()


@admin.register(models.CultBiserica)
class CultBisericaAdmin(admin.ModelAdmin):
    list_display = ['nume', 'nr_biserici']
    search_fields = ["nume"]

    def nr_biserici(self, obj):
       return obj.biserici.count()


@admin.register(models.UtilizareBiserica)
class UtilizareBisericaAdmin(admin.ModelAdmin):
    list_display = ['nume', 'nr_biserici']
    search_fields = ["nume"]

    def nr_biserici(self, obj):
       return obj.biserici.count()


@admin.register(models.SingularitateBiserica)
class SingularitateBisericaAdmin(admin.ModelAdmin):
    list_display = ['nume', 'nr_biserici']
    search_fields = ["nume"]

    def nr_biserici(self, obj):
       return obj.biserici.count()


@admin.register(models.FunctiuneBiserica)
class FunctiuneBisericaAdmin(admin.ModelAdmin):
    list_display = ['nume', 'nr_biserici', 'nr_biserici_initiale']
    search_fields = ["nume"]

    def nr_biserici(self, obj):
       return obj.biserici.count()

    def nr_biserici_initiale(self, obj):
       return obj.biserici_initiale.count()


class IdentificareInline(admin.StackedInline):
    model = models.Identificare
    verbose_name = "Identificare"
    verbose_name_plural = "Identificare"

@admin.register(models.Biserica)
class BisericaAdmin(admin.ModelAdmin):
    list_display = ['nume']
    search_fields = ["nume"]
    list_filter = ["identificare__judet"]
    inlines = [IdentificareInline]