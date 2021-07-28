from django.contrib import admin
from django.contrib.auth.models import Permission
# Register your models here.
from biserici import models
from guardian.admin import GuardedModelAdmin
from reversion_compare.admin import CompareVersionAdmin
from simple_history.admin import SimpleHistoryAdmin

class HistoryChangedFields(object):
    history_list_display = ["changed_fields"]
    def changed_fields(self, obj):
        if obj.prev_record:
            delta = obj.diff_against(obj.prev_record)
            return delta.changed_fields
        return None

@admin.register(Permission)
class PermissionAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["name"]


@admin.register(models.Localitate)
class LocalitateAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume', 'nr_biserici']
    search_fields = ["nume"]
    list_filter = ["judet"]

    def nr_biserici(self, obj):
        return obj.biserici.count()


@admin.register(models.Judet)
class JudetAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume', 'cod', 'nr_biserici']
    search_fields = ["nume"]

    def nr_biserici(self, obj):
       return obj.biserici.count()


@admin.register(models.StatutBiserica)
class StatutBisericaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume', 'nr_biserici']
    search_fields = ["nume"]

    def nr_biserici(self, obj):
       return obj.biserici.count()


@admin.register(models.CultBiserica)
class CultBisericaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume', 'nr_biserici']
    search_fields = ["nume"]

    def nr_biserici(self, obj):
       return obj.biserici.count()


@admin.register(models.UtilizareBiserica)
class UtilizareBisericaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume', 'nr_biserici']
    search_fields = ["nume"]

    def nr_biserici(self, obj):
       return obj.biserici.count()


@admin.register(models.SingularitateBiserica)
class SingularitateBisericaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume', 'nr_biserici']
    search_fields = ["nume"]

    def nr_biserici(self, obj):
       return obj.biserici.count()


@admin.register(models.ProprietateBiserica)
class ProprietateBisericaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume', 'nr_biserici']
    search_fields = ["nume"]

    def nr_biserici(self, obj):
       return obj.biserici.count()


@admin.register(models.FunctiuneBiserica)
class FunctiuneBisericaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
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



@admin.register(models.Identificare)
class IdentificareAdmin(GuardedModelAdmin, HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['biserica']
    search_fields = ["biserica__nume"]



@admin.register(models.SursaDatare)
class SursaDatareAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume', 'nr_biserici', 'nr_biserici_initiale']
    search_fields = ["nume"]

    def nr_biserici(self, obj):
       return obj.biserici.count()

    def nr_biserici_initiale(self, obj):
       return obj.biserici_initiale.count()


@admin.register(models.Secol)
class SecolAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume', 'nr_biserici', 'nr_biserici_initiale']
    search_fields = ["nume"]

    def nr_biserici(self, obj):
       return obj.biserici.count()

    def nr_biserici_initiale(self, obj):
       return obj.biserici_initiale.count()


@admin.register(models.StudiuDendocronologic)
class StudiuDendocronologicAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume', 'fisier']
    search_fields = ["nume"]


@admin.register(models.Persoana)
class PersoanaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume']
    search_fields = ["nume"]


@admin.register(models.Eveniment)
class EvenimentAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume']
    search_fields = ["nume"]


@admin.register(models.Studiu)
class StudiuAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume']
    search_fields = ["nume"]


class IstoricInline(admin.StackedInline):
    model = models.Istoric
    verbose_name = "Istoric"
    verbose_name_plural = "Istoric"
    readonly_fields = ['last_edit_date', 'last_edit_user']


class CtitorBisericaInline(admin.StackedInline):
    model = models.CtitorBiserica
    verbose_name = "Ctitor"
    verbose_name_plural = "Ctitori"
    extra = 1

class MesterBisericaInline(admin.StackedInline):
    model = models.MesterBiserica
    verbose_name = "Meșter"
    verbose_name_plural = "Meșteri"
    extra = 1

class ZugravBisericaInline(admin.StackedInline):
    model = models.ZugravBiserica
    verbose_name = "Zugrav"
    verbose_name_plural = "Zugravi"
    extra = 1

class PersonalitateBisericaInline(admin.StackedInline):
    model = models.PersonalitateBiserica
    verbose_name = "Personalitate"
    verbose_name_plural = "Personalități"
    extra = 1

class EvenimentBisericaInline(admin.StackedInline):
    model = models.EvenimentBiserica
    verbose_name = "Eveniment"
    verbose_name_plural = "Evenimente"
    extra = 1


class MutareBisericaInline(admin.StackedInline):
    model = models.MutareBiserica
    verbose_name = "Mutare biserică"
    verbose_name_plural = "Mutări biserică"
    extra = 1



class StudiuIstoricInline(admin.StackedInline):
    model = models.StudiuIstoric
    verbose_name = "Studiu istoric"
    verbose_name_plural = "Studii istorice"
    extra = 1


@admin.register(models.Istoric)
class IstoricAdmin(GuardedModelAdmin, HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['biserica']
    search_fields = ["biserica__nume"]
    exclude = ['biserica', 'last_edit_user']
    inlines = [
        CtitorBisericaInline,
        MesterBisericaInline,
        ZugravBisericaInline,
        PersonalitateBisericaInline,
        EvenimentBisericaInline,
        MutareBisericaInline,
        StudiuIstoricInline
    ]



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




@admin.register(models.Patrimoniu)
class PatrimoniuAdmin(GuardedModelAdmin, HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['biserica']
    search_fields = ["biserica__nume"]
    exclude = ['biserica', 'last_edit_user']


class ConservareInline(admin.StackedInline):
    model = models.Conservare
    verbose_name = "Stare Conservare"
    verbose_name_plural = "Stare Conservare"
    readonly_fields = ['last_edit_date', 'last_edit_user']


@admin.register(models.Conservare)
class ConservareAdmin(GuardedModelAdmin, HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['biserica']
    search_fields = ["biserica__nume"]
    exclude = ['biserica', 'last_edit_user']
    inlines = [
    ]
    fieldsets = (
        ('Sit', {
           'fields': ('stare_cimitir', 'stare_cimitir_detalii', 'stare_monumente_funerare_valoroase', 'stare_monumente_funerare_valoroase_detalii', 'vegetatie_invaziva', 'vegetatie_invaziva_detalii', 'stare_elemente_arhitecturale', 'stare_elemente_arhitecturale_detalii')
        }),
        ('Structura bisericii', {
           'fields': ("stare_teren", "stare_teren_detalii", "stare_fundatii", "stare_fundatii_detalii", "stare_corp_biserica", "stare_corp_biserica_detalii", "stare_bolti", "stare_bolti_detalii", "stare_sarpanta_peste_corp_biserica", "stare_sarpanta_peste_corp_biserica_detalii", "stare_structura_turn", "stare_structura_turn_detalii")
        }),
        ('Finisaje de arhitectură', {
           'fields': ("stare_invelitoare", "stare_invelitoare_detalii", "stare_finisaj_peste_corp", "stare_finisaj_peste_corp_detalii", "stare_finisaj_tambur_turn", "stare_finisaj_tambur_turn_detalii", "stare_pardoseli_interioare", "stare_pardoseli_interioare_detalii", "stare_usi_si_ferestre", "stare_usi_si_ferestre_detalii")
        }),
        ('Starea stratului pictural', {
           'fields': ("stare_picturi_exterioare", "stare_picturi_exterioare_detalii", "stare_picturi_interioare", "stare_picturi_interioare_detalii")
        }),
        ('Obiecte de cult', {
           'fields': ("stare_icoane_istorice", "stare_icoane_istorice_detalii", "starea_obiecte_de_cult", "starea_obiecte_de_cult_detalii", "starea_mobilier", "starea_mobilier_detalii")
        }),
        
    )


@admin.register(models.Biserica)
class BisericaAdmin(GuardedModelAdmin, HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume', 'update_identificare', 'update_istoric', 'update_descriere', 'update_patrimoniu', 'update_conservare']
    search_fields = ["nume"]
    list_filter = ["identificare__judet"]
    inlines = [
        # IdentificareInline,
        # IstoricInline,
        # DescriereInline,
        # PatrimoniuInline,
        # ConservareInline
        ]
    readonly_fields = ['last_edit_date', 'last_edit_user']

    # def save_model(self, request, obj, form, change):
    #     try:
    #         obj.identificare.last_edit_user = request.user
    #         obj.identificare.save()
    #         obj.istoric.last_edit_user = request.user
    #         obj.istoric.save()
    #         obj.descriere.last_edit_user = request.user
    #         obj.descriere.save()
    #         obj.patrimoniu.last_edit_user = request.user
    #         obj.patrimoniu.save()
    #         obj.conservare.last_edit_user = request.user
    #         obj.conservare.save()
    #     except:
    #         pass
    #     obj.last_edit_user = request.user
    #     obj.save()
    #     print('saved')

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

