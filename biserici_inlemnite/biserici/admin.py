from django.contrib import admin
from django.contrib.auth.models import Permission
# Register your models here.
from biserici import models
from nomenclatoare import admin as nadmin
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


class PovesteBisericaInline(admin.StackedInline):
    model = models.PovesteBiserica
    verbose_name = "Poveste"
    verbose_name_plural = "Povești"
    extra = 1

class InterventieBisericaInline(admin.StackedInline):
    model = models.InterventieBiserica
    verbose_name = "Intervenție"
    verbose_name_plural = "Intervenții"
    extra = 1


@admin.register(models.Istoric)
class IstoricAdmin(GuardedModelAdmin, HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['biserica']
    search_fields = ["biserica__nume"]
    exclude = ['biserica']
    inlines = [
        nadmin.CtitorBisericaInline,
        nadmin.MesterBisericaInline,
        nadmin.ZugravBisericaInline,
        nadmin.PersonalitateBisericaInline,
        nadmin.EvenimentBisericaInline,
        nadmin.MutareBisericaInline,
        nadmin.StudiuIstoricInline,
        PovesteBisericaInline,
        InterventieBisericaInline
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



class InterventieBisericaInline(admin.StackedInline):
    model = models.InterventieBiserica
    verbose_name = "Intervenție"
    verbose_name_plural = "Intervenții"
    extra = 1


class FotografieAnsambluInline(admin.StackedInline):
    model = models.FotografieAnsamblu
    verbose_name = 'Fotografie Ansamblu'
    verbose_name_plural = 'Ansamblu'
    extra = 1


class FotografieFatadaInline(admin.StackedInline):
    model = models.FotografieFatada
    verbose_name = 'Fotografie Fatada'
    verbose_name_plural = 'Fatada'
    extra = 1


class FotografiePortalInline(admin.StackedInline):
    model = models.FotografiePortal
    verbose_name = 'Fotografie Portal'
    verbose_name_plural = 'Portal'
    extra = 1


class FotografieFereastraInline(admin.StackedInline):
    model = models.FotografieFereastra
    verbose_name = 'Fotografie Fereastra'
    verbose_name_plural = 'Fereastra'
    extra = 1


class FotografieCheotoarInline(admin.StackedInline):
    model = models.FotografieCheotoar
    verbose_name = 'Fotografie Cheotoar'
    verbose_name_plural = 'Cheotoar'
    extra = 1


class FotografieTalpaInline(admin.StackedInline):
    model = models.FotografieTalpa
    verbose_name = 'Fotografie Talpa'
    verbose_name_plural = 'Talpa'
    extra = 1


class FotografieStreasinaInline(admin.StackedInline):
    model = models.FotografieStreasina
    verbose_name = 'Fotografie Streasina'
    verbose_name_plural = 'Streasina'
    extra = 1


class FotografieInvelitoareInline(admin.StackedInline):
    model = models.FotografieInvelitoare
    verbose_name = 'Fotografie Invelitoare'
    verbose_name_plural = 'Invelitoare'
    extra = 1


class FotografieCruceBisericaInline(admin.StackedInline):
    model = models.FotografieCruceBiserica
    verbose_name = 'Fotografie Cruce Biserica'
    verbose_name_plural = 'Cruce Biserica'
    extra = 1


class FotografieTurnInline(admin.StackedInline):
    model = models.FotografieTurn
    verbose_name = 'Fotografie Turn'
    verbose_name_plural = 'Turn'
    extra = 1


class FotografieDegradariExterioareInline(admin.StackedInline):
    model = models.FotografieDegradariExterioare
    verbose_name = 'Fotografie Degradări Exterioare'
    verbose_name_plural = 'Degradări Exterioare'
    extra = 1


class FotografieInteriorDesfasuratInline(admin.StackedInline):
    model = models.FotografieInteriorDesfasurat
    verbose_name = 'Fotografie Interior Desfașurat'
    verbose_name_plural = 'Interior Desfașurat'
    extra = 1


class FotografiePisanieInscriptieCtitorMesterInline(admin.StackedInline):
    model = models.FotografiePisanieInscriptieCtitorMester
    verbose_name = 'Fotografie Pisanie/Inscriptie/Ctitor/Mester'
    verbose_name_plural = 'Pisanie Inscriptie Ctitor Mester'
    extra = 1


class FotografiePortalPronaosInline(admin.StackedInline):
    model = models.FotografiePortalPronaos
    verbose_name = 'Fotografie Portal Pronaos/Naos'
    verbose_name_plural = 'Portal Pronaos'
    extra = 1


class FotografiePortalNaosInline(admin.StackedInline):
    model = models.FotografiePortalNaos
    verbose_name = 'Fotografie Portal Naos/Pronaos'
    verbose_name_plural = 'Portal Naos'
    extra = 1


class FotografieDetaliuBoltaInline(admin.StackedInline):
    model = models.FotografieDetaliuBolta
    verbose_name = 'Fotografie Detaliu Boltă'
    verbose_name_plural = 'Detaliu Boltă'
    extra = 1


class FotografieIconostasNaosInline(admin.StackedInline):
    model = models.FotografieIconostasNaos
    verbose_name = 'Fotografie Iconostas Naos'
    verbose_name_plural = 'Iconostas Naos'
    extra = 1


class FotografieIconostasAltarInline(admin.StackedInline):
    model = models.FotografieIconostasAltar
    verbose_name = 'Fotografie Iconostas Altar'
    verbose_name_plural = 'Iconostas Altar'
    extra = 1


class FotografieIcoanaInline(admin.StackedInline):
    model = models.FotografieIcoana
    verbose_name = 'Fotografie Icoană'
    verbose_name_plural = 'Icoane'
    extra = 1


class FotografieObiectCultInline(admin.StackedInline):
    model = models.FotografieObiectCult
    verbose_name = 'Fotografie Obiect Cult'
    verbose_name_plural = 'Obiecte Cult'
    extra = 1


class FotografieMobilierCandelabreInline(admin.StackedInline):
    model = models.FotografieMobilierCandelabre
    verbose_name = 'Fotografie Mobilier Candelabre'
    verbose_name_plural = 'Mobilier/Candelabre'
    extra = 1


class FotografieDegradariInteriorInline(admin.StackedInline):
    model = models.FotografieDegradariInterior
    verbose_name = 'Fotografie Degradări Interior'
    verbose_name_plural = 'Degradări Interior'
    extra = 1


class FotografieDegradariPodInline(admin.StackedInline):
    model = models.FotografieDegradariPod
    verbose_name = 'Fotografie Degradări Pod'
    verbose_name_plural = 'Degradări Pod'
    extra = 1


class FotografieDetaliuPodInline(admin.StackedInline):
    model = models.FotografieDetaliuPod
    verbose_name = 'Fotografie Detaliu Pod'
    verbose_name_plural = 'Detalii Pod'
    extra = 1



@admin.register(models.Fotografii)
class FotografiiAdmin(GuardedModelAdmin, HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['biserica']
    search_fields = ["biserica__nume"]
    exclude = ['biserica']
    inlines = [
        FotografieFatadaInline,
        FotografiePortalInline,
        FotografieFereastraInline,
        FotografieCheotoarInline,
        FotografieTalpaInline,
        FotografieStreasinaInline,
        FotografieInvelitoareInline,
        FotografieCruceBisericaInline,
        FotografieTurnInline,
        FotografieDegradariExterioareInline,
        FotografieInteriorDesfasuratInline,
        FotografiePisanieInscriptieCtitorMesterInline,
        FotografiePortalPronaosInline,
        FotografiePortalNaosInline,
        FotografieDetaliuBoltaInline,
        FotografieIconostasNaosInline,
        FotografieIconostasAltarInline,
        FotografieIcoanaInline,
        FotografieObiectCultInline,
        FotografieMobilierCandelabreInline,
        FotografieDegradariInteriorInline,
        FotografieDegradariPodInline,
        FotografieDetaliuPodInline,
    ]
