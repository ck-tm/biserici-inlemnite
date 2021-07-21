from django.contrib import admin
from django.contrib.auth.models import Permission
# Register your models here.
from biserici import models
from guardian.admin import GuardedModelAdmin



@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ["name"]


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


@admin.register(models.ProprietateBiserica)
class ProprietateBisericaAdmin(admin.ModelAdmin):
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
    readonly_fields = ['last_edit_date', 'last_edit_user']



class IstoricInline(admin.StackedInline):
    model = models.Istoric
    verbose_name = "Istoric"
    verbose_name_plural = "Istoric"
    readonly_fields = ['last_edit_date', 'last_edit_user']



class DescriereInline(admin.StackedInline):
    model = models.Descriere
    verbose_name = "Descriere"
    verbose_name_plural = "Descriere"
    readonly_fields = ['last_edit_date', 'last_edit_user']



class PatrimoniuInline(admin.StackedInline):
    model = models.Patrimoniu
    verbose_name = "Valoare Patrimoniu Cultural"
    verbose_name_plural = "Valoare Patrimoniu Cultural"
    readonly_fields = ['last_edit_date', 'last_edit_user']



class ConservareInline(admin.StackedInline):
    model = models.Conservare
    verbose_name = "Stare Conservare"
    verbose_name_plural = "Stare Conservare"
    readonly_fields = ['last_edit_date', 'last_edit_user']


@admin.register(models.Biserica)
class BisericaAdmin(GuardedModelAdmin):
    list_display = ['nume', 'update_identificare', 'update_istoric', 'update_descriere', 'update_patrimoniu', 'update_conservare']
    search_fields = ["nume"]
    list_filter = ["identificare__judet"]
    inlines = [
        IdentificareInline,
        IstoricInline,
        DescriereInline,
        PatrimoniuInline,
        ConservareInline
        ]
    readonly_fields = ['last_edit_date', 'last_edit_user']

    def save_model(self, request, obj, form, change):
        try:
            obj.identificare.last_edit_user = request.user
            obj.identificare.save()
            obj.istoric.last_edit_user = request.user
            obj.istoric.save()
            obj.descriere.last_edit_user = request.user
            obj.descriere.save()
            obj.patrimoniu.last_edit_user = request.user
            obj.patrimoniu.save()
            obj.conservare.last_edit_user = request.user
            obj.conservare.save()
        except:
            pass
        obj.last_edit_user = request.user
        obj.save()
        print('saved')

    def update_identificare(self, obj):
        return f"{obj.identificare.last_edit_user} ({obj.identificare.last_edit_date.strftime('%d %b %Y %H:%M:%S')})"

    def update_istoric(self, obj):
        return f"{obj.istoric.last_edit_user} ({obj.istoric.last_edit_date.strftime('%d %b %Y %H:%M:%S')})"

    def update_descriere(self, obj):
        return f"{obj.descriere.last_edit_user} ({obj.descriere.last_edit_date.strftime('%d %b %Y %H:%M:%S')})"

    def update_patrimoniu(self, obj):
        return f"{obj.patrimoniu.last_edit_user} ({obj.patrimoniu.last_edit_date.strftime('%d %b %Y %H:%M:%S')})"

    def update_conservare(self, obj):
        return f"{obj.conservare.last_edit_user} ({obj.conservare.last_edit_date.strftime('%d %b %Y %H:%M:%S')})"