from django.contrib import admin
from django.contrib.auth.models import Permission
# Register your models here.
from biserici import models
from nomenclatoare.admin import (
    CtitorBisericaInline,
    MesterBisericaInline,
    ZugravBisericaInline,
    PersonalitateBisericaInline,
    EvenimentBisericaInline,
    MutareBisericaInline,
    StudiuIstoricInline,
    )
from guardian.admin import GuardedModelAdmin

from simple_history.admin import SimpleHistoryAdmin

class HistoryChangedFields(object):
    history_list_display = ["changed_fields"]
    def changed_fields(self, obj):
        if obj.prev_record:
            delta = obj.diff_against(obj.prev_record)
            return delta.changed_fields
        return None


class IdentificareInline(admin.StackedInline):
    model = models.Identificare
    verbose_name = "Identificare"
    verbose_name_plural = "Identificare"


@admin.register(models.Identificare)
class IdentificareAdmin(GuardedModelAdmin, HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['biserica']
    search_fields = ["biserica__nume"]


class IstoricInline(admin.StackedInline):
    model = models.Istoric
    verbose_name = "Istoric"
    verbose_name_plural = "Istoric"


@admin.register(models.Istoric)
class IstoricAdmin(GuardedModelAdmin, HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['biserica']
    search_fields = ["biserica__nume"]
    exclude = ['biserica']
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


@admin.register(models.Descriere)
class DescriereAdmin(GuardedModelAdmin, HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['biserica']
    search_fields = ["biserica__nume"]
    exclude = ['biserica']


class PatrimoniuInline(admin.StackedInline):
    model = models.Patrimoniu
    verbose_name = "Valoare Patrimoniu Cultural"
    verbose_name_plural = "Valoare Patrimoniu Cultural"


@admin.register(models.Patrimoniu)
class PatrimoniuAdmin(GuardedModelAdmin, HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['biserica']
    search_fields = ["biserica__nume"]
    exclude = ['biserica']


class ConservareInline(admin.StackedInline):
    model = models.Conservare
    verbose_name = "Stare Conservare"
    verbose_name_plural = "Stare Conservare"


@admin.register(models.Conservare)
class ConservareAdmin(GuardedModelAdmin, HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['biserica']
    search_fields = ["biserica__nume"]
    exclude = ['biserica']
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


    def update_identificare(self, obj):
        last_update = obj.identificare.history.last()
        if last_update:
            return f"{last_update.history_user} ({last_update.history_date.strftime('%d %b %Y %H:%M:%S')})"
        return '-'

    def update_istoric(self, obj):
        last_update = obj.istoric.history.last()
        if last_update:
            return f"{last_update.history_user} ({last_update.history_date.strftime('%d %b %Y %H:%M:%S')})"
        return '-'

    def update_descriere(self, obj):
        last_update = obj.descriere.history.last()
        if last_update:
            return f"{last_update.history_user} ({last_update.history_date.strftime('%d %b %Y %H:%M:%S')})"
        return '-'

    def update_patrimoniu(self, obj):
        last_update = obj.patrimoniu.history.last()
        if last_update:
            return f"{last_update.history_user} ({last_update.history_date.strftime('%d %b %Y %H:%M:%S')})"
        return '-'

    def update_conservare(self, obj):
        last_update = obj.conservare.history.last()
        if last_update:
            return f"{last_update.history_user} ({last_update.history_date.strftime('%d %b %Y %H:%M:%S')})"
        return '-'
