from django.contrib import admin
from django.contrib.auth.models import Permission
# Register your models here.
from biserici import models
from nomenclatoare import admin as nadmin
from guardian.admin import GuardedModelAdmin
from adminsortable.admin import SortableAdmin
from adminsortable2.admin import SortableAdminMixin
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

    fieldsets = (
        ('Localizare/peisaj', {
           'fields': ("amplasament", "topografie", "toponim", "toponim_sursa", "relatia_cu_cimitirul", "peisagistica_sitului")
        }),
        ('Ansamblu construit', {
            'fields': ("elemente", "detalii_elemente", "elemente_importante", "detalii_elemente_importante")
        }),
        ('Arhitectura', {
            'fields': ("planimetria_bisericii", "gabarit_exterior_al_talpilor", "materiale", "detalii_materiale")
        }),
        ('Elemente arhitecturale', {
            'fields': ("turn_dimensiune", "turn_tip", "turn_numar", "turn_decor", "turn_plan", "turn_amplasare", "turn_galerie", "turn_numar_arcade", "turn_numar_arcade_detalii", "turn_asezare_talpi", "turn_relatie_talpi", "turn_numar_talpi", "clopote_an", "clopote_inscriptie", "sarpanta_tip", "sarpanta_veche_nefolosita", "sarpanta_numar_turnulete", "sarpanta_numar_cruci", "sarpanta_material_cruci", "sarpanta_detalii", "numar_accese", "numar_geamuri", "oachiesi_aerisitoare", "oachiesi_aerisitoare_detalii", "bolta_peste_pronaos", "bolta_peste_naos", "bolta_peste_altar", "bolta_peste_altar_tip", "solee", "masa_altar_material_picior", "masa_altar_material_blat")
        }),
        ('Structura', {
            'fields': ("fundatia", "sistem_in_cheotoare", "sistem_in_catei", "sistem_mixt")
        })
    )



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
class BisericaAdmin(SortableAdminMixin, GuardedModelAdmin, HistoryChangedFields, SimpleHistoryAdmin):
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

class FinisajActualInline(admin.StackedInline):
    model = models.FinisajActualInvelitoare
    verbose_name = 'Finisaj actual al învelitorii peste corpul bisericii'
    verbose_name_plural = 'Finisajul actual al învelitorii peste corpul bisericii'
    max_num = 1


class FinisajAnteriorInvelitoareInline(admin.StackedInline):
    model = models.FinisajAnteriorInvelitoare
    verbose_name = 'Etapă anterioară vizibilă a învelitorii '
    verbose_name_plural = 'Etape anterioare vizibile ale învelitorii '
    max_num = 1 


class FinisajTamburTurnInline(admin.StackedInline):
    model = models.FinisajTamburTurn
    verbose_name = 'Finisaj exterior al tamburului turnului bisericii (dacă are turn)'
    verbose_name_plural = 'Finisajul exterior al tamburului turnului bisericii (dacă are turn)'
    max_num = 1 

class FinisajInvelitoareTurnInline(admin.StackedInline):
    model = models.FinisajInvelitoareTurn
    verbose_name = 'Finisaj învelitore peste turnul bisercii (dacă are turn)'
    verbose_name_plural = 'Finisajul învelitorii peste turnul bisercii (dacă are turn)'
    max_num = 1 

class FinisajPardoseaInline(admin.StackedInline):
    model = models.FinisajPardosea
    verbose_name = 'Finisaj pardoseli interioare'
    verbose_name_plural = 'Finisajul pardoselilor interioare'
    extra = 1 

class FinisajPeretiInteriorInline(admin.StackedInline):
    model = models.FinisajPeretiInterior
    verbose_name = 'Finisaj perete interior'
    verbose_name_plural = 'Pereți interiori'
    extra = 1 

class FinisajBoltiInline(admin.StackedInline):
    model = models.FinisajBolti
    verbose_name = 'Finisaj boltă'
    verbose_name_plural = 'Bolți'
    extra = 1 

class FinisajTavanInline(admin.StackedInline):
    model = models.FinisajTavan
    verbose_name = 'Finisaj tavan'
    verbose_name_plural = 'Tavane'
    extra = 1 


@admin.register(models.Finisaj)
class FinisajAdmin(GuardedModelAdmin, HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['biserica']
    search_fields = ["biserica__nume"]
    exclude = ['biserica']
    inlines = [
        FinisajActualInline,
        FinisajAnteriorInvelitoareInline,
        FinisajPardoseaInline,
        FinisajPeretiInteriorInline,
        FinisajBoltiInline,
        FinisajTavanInline,
    ]


class PicturaExterioaraInline(admin.StackedInline):
    model = models.PicturaExterioara
    verbose_name = 'Pictură exterioară'
    verbose_name_plural = 'Pictură exterioară'
    max_num = 1

class PicturaInterioaraInline(admin.StackedInline):
    model = models.PicturaInterioara
    verbose_name = 'Pictură interioară'
    verbose_name_plural = 'Pictură interioară'
    max_num = 1

@admin.register(models.ComponentaArtistica)
class ComponentaArtisticaAdmin(GuardedModelAdmin, HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['biserica']
    search_fields = ["biserica__nume"]
    exclude = ['biserica']
    inlines = [
        PicturaExterioaraInline,
        PicturaInterioaraInline
    ]

    fieldsets = (
        ('General', {
           'fields': ("proscomidie","elemente_sculptate","elemente_detalii","alte_icoane_vechi","alte_icoane_vechi_detalii","obiecte_de_cult","obiecte_de_cult_detalii","mobiliere","mobiliere_detalii","obiecte_instrainate","obiecte_instrainate_detalii")
        }),
        ('Iconostasul', {
           'fields': ("iconostas_naos_altar_tip", "iconostas_naos_altar_numar_intrari", "iconostas_naos_altar_finisaj", "iconostas_naos_altar_registre", "iconostas_naos_altar_tip_usi", "iconostas_naos_altar_detalii")
        }),
        ('Perete despărțitor (pronaos/naos)', {
           'fields': ("iconostas_pronaos_naos_tip","iconostas_pronaos_naos_numar_intrari","iconostas_pronaos_naos_finisaj","iconostas_pronaos_naos_detalii")
        }),
        ('Altar', {
           'fields': ("altar_decor", "altar_decor_detalii")
        })
    )

