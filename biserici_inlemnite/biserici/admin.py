from django.contrib import admin
from django.contrib.auth.models import Permission
from django.utils.html import format_html
from django.conf import settings

from biserici import models
from nomenclatoare import admin as nadmin
from guardian.admin import GuardedModelAdmin
from adminsortable.admin import SortableAdmin
from adminsortable2.admin import SortableAdminMixin
from simple_history.admin import SimpleHistoryAdmin


# class MyAdminSite(admin.AdminSite):
#     def get_app_list(self, request):
#         """
#         Return a sorted list of all the installed apps that have been
#         registered in this site.
#         """
#         ordering = {
#             "Biserici": 1,
#             "Identificare Biserici": 2,
#         }
#         app_dict = self._build_app_dict(request)
#         # a.sort(key=lambda x: b.index(x[0]))
#         # Sort the apps alphabetically.
#         app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
#         print('new admin .....')
#         print('new admin .....')
#         print('new admin .....')
#         print('new admin .....')
#         # Sort the models alphabetically within each app.
#         for app in app_list:
#             app['models'].sort(key=lambda x: ordering[x['name']])

#         return app_list


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
    readonly_fields = ['completare', 'missing_fields']
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
    readonly_fields = ['completare', 'missing_fields']
    fieldsets = (
        ('Localizare/peisaj', {
           'fields': ("amplasament", "topografie", "toponim", "toponim_sursa", "relatia_cu_cimitirul", "peisagistica_sitului", "observatii"),

        }),
        ('Ansamblu construit', {
            'fields': ("elemente", "detalii_elemente", "elemente_importante", "detalii_elemente_importante"),
            'description': 'This is another description text'
        }),
        ('Arhitectura', {
            'fields': ("planimetria_bisericii", "gabarit_exterior_al_talpilor", "materiale", "detalii_materiale"),
            'description': 'This is another description text'
        }),
        ('Elemente arhitecturale', {
            'fields': ("turn_dimensiune", "turn_tip", "turn_numar", "turn_decor", "turn_plan", "turn_amplasare", "turn_galerie", "turn_numar_arcade", "turn_numar_arcade_detalii", "turn_asezare_talpi", "turn_relatie_talpi", "turn_numar_talpi", "turn_observatii", "clopote_an", "clopote_inscriptie", "sarpanta_tip", "sarpanta_veche_nefolosita", "sarpanta_numar_turnulete", "sarpanta_numar_cruci", "sarpanta_material_cruci", "sarpanta_detalii", "numar_accese_pridvor", "numar_accese_pridvor_detalii", "numar_accese_pronaos", "numar_accese_pronaos_detalii", "numar_accese_naos", "numar_accese_naos_detalii", "numar_accese_altar", "numar_accese_altar_detalii", "numar_geamuri_pridvor", "numar_geamuri_pridvor_detalii", "numar_geamuri_pronaos", "numar_geamuri_pronaos_detalii", "numar_geamuri_naos", "numar_geamuri_naos_detalii", "numar_geamuri_altar", "numar_geamuri_altar_detalii", "oachiesi_aerisitoare", "oachiesi_aerisitoare_detalii", "bolta_peste_pronaos", "bolta_peste_pronaos_material", "bolta_peste_pronaos_tipul_de_arc", "bolta_peste_pronaos_observatii", "bolta_peste_naos", "bolta_peste_naos_material", "bolta_peste_naos_tipul_de_arc", "bolta_peste_naos_observatii", "bolta_peste_altar", "bolta_peste_altar_tip", "bolta_peste_altar_material", "bolta_peste_altar_tipul_de_arc", "bolta_peste_altar_observatii", "cor", "cor_material", "cor_observatii", "solee", "solee_detalii", "masa_altar_material_picior", "masa_altar_material_blat", "masa_altar_observatii"),
            'description': 'This is another description text'
        }),
        ('Structura', {
            'fields': ("fundatia", "sistem_in_cheotoare", "sistem_in_catei", "sistem_mixt"),
            'description': 'This is another description text'
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
    readonly_fields = ['completare', 'missing_fields']


class ConservareInline(admin.StackedInline):
    model = models.Conservare
    verbose_name = "Stare Conservare"
    verbose_name_plural = "Stare Conservare"


@admin.register(models.Conservare)
class ConservareAdmin(GuardedModelAdmin, HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['biserica']
    search_fields = ["biserica__nume"]
    exclude = ['biserica']
    readonly_fields = ['completare', 'missing_fields']
    inlines = [
    ]
    fieldsets = (
        ('Sit', {
           'fields': ('stare_cimitir', 'stare_cimitir_detalii', 'stare_monumente_funerare_valoroase', 'stare_monumente_funerare_valoroase_detalii', 'vegetatie_invaziva', 'vegetatie_invaziva_detalii', 'stare_elemente_arhitecturale', 'stare_elemente_arhitecturale_detalii')
        }),
        ('Structura bisericii', {
           'fields': ("stare_teren", "stare_teren_detalii", "stare_fundatii", "stare_fundatii_detalii", "stare_corp_biserica", "stare_corp_biserica_detalii", "stare_bolti", "stare_bolti_detalii", "stare_sarpanta_peste_corp_biserica", "stare_sarpanta_peste_corp_biserica_detalii", "stare_structura_turn", "stare_structura_turn_detalii", "stare_talpi", "stare_talpi_detalii", "stare_cosoroabe", "stare_cosoroabe_detalii", "stare_sarpanta_turn", "stare_sarpanta_turn_detalii")
        }),
        ('Finisaje de arhitectură', {
           'fields': ("stare_invelitoare", "stare_invelitoare_detalii", "stare_finisaj_peste_corp", "stare_finisaj_peste_corp_detalii", "stare_finisaj_tambur_turn", "stare_finisaj_tambur_turn_detalii", "stare_pardoseli_interioare", "stare_pardoseli_interioare_detalii", "stare_usi_si_ferestre", "stare_usi_si_ferestre_detalii")
        }),
        ('Starea stratului pictural', {
           'fields': ("stare_picturi_exterioare", "stare_picturi_exterioare_detalii", "stare_picturi_interioare", "stare_picturi_interioare_detalii", "stare_iconostas", "stare_iconostas_detalii")
        }),
        ('Obiecte de cult', {
           'fields': ("stare_icoane_istorice", "stare_icoane_istorice_detalii", "starea_obiecte_de_cult", "starea_obiecte_de_cult_detalii", "starea_mobilier", "starea_mobilier_detalii")
        }),
        
    )


@admin.register(models.Biserica)
class BisericaAdmin(SortableAdminMixin, GuardedModelAdmin, HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume', 'identificare_completare', 'istoric_completare', 'descriere_completare', 'finisaje_completare', 'fotografii_completare', 'componenta_artistica_completare', 'patrimoniu_completare', 'conservare_completare']
    search_fields = ["nume"]
    readonly_fields = ('capitole',)
    list_filter = ["identificare__judet"]
    inlines = [
        # IdentificareInline,
        # IstoricInline,
        # DescriereInline,
        # PatrimoniuInline,
        # ConservareInline
        ]

    def get_queryset(self, request):
        qs = super().get_queryset(request).select_related("identificare","descriere","istoric","patrimoniu","conservare","fotografii","finisaj","componentaartistica")
        print('get')
        return qs

    def identificare_completare(self, obj):
        
        html = f"<a href='/{settings.ADMIN_URL}biserici/identificare/{obj.identificare.pk}/change/'>{obj.identificare.completare}</a> <br>"
        return format_html(html)

    def descriere_completare(self, obj):
        
        html = f"<a href='/{settings.ADMIN_URL}biserici/descriere/{obj.descriere.pk}/change/'>{obj.descriere.completare}</a> <br>"
        return format_html(html)

    def istoric_completare(self, obj):
        html = f"<a href='/{settings.ADMIN_URL}biserici/istoric/{obj.istoric.pk}/change/'>{obj.istoric.completare}</a> <br>"
        return format_html(html)

    def decriere_completare(self, obj):
        
        html = f"<a href='/{settings.ADMIN_URL}biserici/descriere/{obj.descriere.pk}/change/'>{obj.descriere.completare}</a> <br>"
        return format_html(html)


    def fotografii_completare(self, obj):
        
        html = f"<a href='/{settings.ADMIN_URL}biserici/fotografii/{obj.fotografii.pk}/change/'>{obj.fotografii.completare}</a> <br>"
        return format_html(html)


    def finisaje_completare(self, obj):
        
        html = f"<a href='/{settings.ADMIN_URL}biserici/finisaj/{obj.finisaj.pk}/change/'>{obj.finisaj.completare}</a> <br>"
        return format_html(html)

    def componenta_artistica_completare(self, obj):
        
        html = f"<a href='/{settings.ADMIN_URL}biserici/componentaartistica/{obj.componentaartistica.pk}/change/'>{obj.componentaartistica.completare}</a> <br>"
        return format_html(html)

    def patrimoniu_completare(self, obj):
        
        html = f"<a href='/{settings.ADMIN_URL}biserici/patrimoniu/{obj.patrimoniu.pk}/change/'>{obj.patrimoniu.completare}</a> <br>"
        return format_html(html)

    def conservare_completare(self, obj):
        
        html = f"<a href='/{settings.ADMIN_URL}biserici/conservare/{obj.conservare.pk}/change/'>{obj.conservare.completare}</a> <br>"
        return format_html(html)


    def capitole(self, obj):
        html = f"<a href='/{settings.ADMIN_URL}biserici/identificare/{obj.identificare.pk}/change/'>1. Identificare</a> <br>"
        html += f"<a href='/{settings.ADMIN_URL}biserici/istoric/{obj.istoric.pk}/change/'>2. Istoric</a> <br>"
        html += f"<a href='/{settings.ADMIN_URL}biserici/descriere/{obj.descriere.pk}/change/'>3. Descriere</a> <br>"
        html += f"<a href='/{settings.ADMIN_URL}biserici/fotografii/{obj.fotografii.pk}/change/'>3.1. Fotografii</a> <br>"
        html += f"<a href='/{settings.ADMIN_URL}biserici/finisaj/{obj.finisaj.pk}/change/'>3.2. Finisaje</a> <br>"
        html += f"<a href='/{settings.ADMIN_URL}biserici/componentaartistica/{obj.componentaartistica.pk}/change/'>3.3. Componenta Artistică</a> <br>"
        html += f"<a href='/{settings.ADMIN_URL}biserici/patrimoniu/{obj.patrimoniu.pk}/change/'>4. Valoare patrimoniu</a> <br>"
        html += f"<a href='/{settings.ADMIN_URL}biserici/conservare/{obj.conservare.pk}/change/'>5. Stare de conservare</a> <br>"

        return format_html(html)

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


class FotografieDetaliuSculpturaInline(admin.StackedInline):
    model = models.FotografieDetaliuSculptura
    verbose_name = 'Fotografie Detaliu Sculptură'
    verbose_name_plural = 'Sculptură'
    extra = 1



class FotografieDetaliuImaginePeretiInline(admin.StackedInline):
    model = models.FotografieDetaliuImaginePereti
    verbose_name = 'Fotografie Detaliu Imagine Pereți'
    verbose_name_plural = 'Pereți'
    extra = 1


class FotografieProgramIconograficInline(admin.StackedInline):
    model = models.FotografieProgramIconografic
    verbose_name = 'Fotografie Program Iconografic'
    verbose_name_plural = 'Program Iconografic'
    extra = 1


class FotografieUrmeSemneSimboluriInline(admin.StackedInline):
    model = models.FotografieUrmeSemneSimboluri
    verbose_name = 'Fotografie Urme/Semne/Simboluri'
    verbose_name_plural = 'Urme/Semne/Simboluri'
    extra = 1


@admin.register(models.Fotografii)
class FotografiiAdmin(GuardedModelAdmin, HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['biserica']
    search_fields = ["biserica__nume"]
    exclude = ['biserica']
    readonly_fields = ['completare', 'missing_fields']
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
        FotografieDetaliuImaginePeretiInline,
        FotografiePisanieInscriptieCtitorMesterInline,
        FotografiePortalPronaosInline,
        FotografiePortalNaosInline,
        FotografieDetaliuBoltaInline,
        FotografieDetaliuSculpturaInline,
        FotografieIconostasNaosInline,
        FotografieIconostasAltarInline,
        FotografieIcoanaInline,
        FotografieObiectCultInline,
        FotografieMobilierCandelabreInline,
        FotografieDegradariInteriorInline,
        FotografieDegradariPodInline,
        FotografieDetaliuPodInline,
        FotografieProgramIconograficInline,
        FotografieUrmeSemneSimboluriInline
    ]

class FinisajActualInline(admin.StackedInline):
    model = models.FinisajActualInvelitoare
    verbose_name = 'Finisaj actual al învelitorii peste corpul bisericii'
    verbose_name_plural = 'Finisajul actual al învelitorii peste corpul bisericii'
    max_num = 1

    class Media:
        js = ('js/admin/invelitoare.js',)

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


class FinisajPorticInline(admin.StackedInline):
    model = models.FinisajPortic
    verbose_name = 'Finisaj Portic'
    verbose_name_plural = 'Portic'
    extra = 1 

class FinisajPronaosInline(admin.StackedInline):
    model = models.FinisajPronaos
    verbose_name = 'Finisaj Pronaos'
    verbose_name_plural = 'Pronaos'
    extra = 1 

class FinisajNaosInline(admin.StackedInline):
    model = models.FinisajNaos
    verbose_name = 'Finisaj Naos'
    verbose_name_plural = 'Naos'
    extra = 1 

class FinisajAltarInline(admin.StackedInline):
    model = models.FinisajAltar
    verbose_name = 'Finisaj Altar'
    verbose_name_plural = 'Altar'
    extra = 1 


@admin.register(models.Finisaj)
class FinisajAdmin(GuardedModelAdmin, HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['biserica']
    search_fields = ["biserica__nume"]
    exclude = ['biserica']
    readonly_fields = ['completare', 'missing_fields']
    inlines = [
        FinisajActualInline,
        FinisajAnteriorInvelitoareInline,
        FinisajTamburTurnInline,
        FinisajInvelitoareTurnInline,
        FinisajPardoseaInline,
        FinisajPeretiInteriorInline,
        FinisajBoltiInline,
        FinisajTavanInline,
        FinisajPorticInline,
        FinisajPronaosInline,
        FinisajNaosInline,
        FinisajAltarInline,
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
    readonly_fields = ['completare', 'missing_fields']

    fieldsets = (
        ('General', {
           'fields': ("proscomidie", "suport_proscomidie","elemente_sculptate","elemente_detalii","alte_icoane_vechi","alte_icoane_vechi_detalii","obiecte_de_cult","obiecte_de_cult_detalii","mobiliere","mobiliere_detalii","obiecte_instrainate","obiecte_instrainate_detalii", "completare", "missing_fields")
        }),
        ('Iconostasul', {
           'fields': ("iconostas_naos_altar_tip", "iconostas_naos_altar_materiale", "iconostas_naos_altar_numar_intrari", "iconostas_naos_altar_tehnica", "iconostas_naos_altar_registre", "iconostas_naos_altar_tip_usi", "iconostas_naos_altar_detalii")
        }),
        ('Perete despărțitor (pronaos/naos)', {
           'fields': ("iconostas_pronaos_naos_tip","iconostas_pronaos_naos_numar_intrari","iconostas_pronaos_naos_tehnica","iconostas_pronaos_naos_detalii")
        }),
        ('Altar', {
           'fields': ("altar_placa_mesei", "altar_piciorul_mesei", "altar_decor", "altar_detalii")
        })
    )



@admin.register(models.Identificare)
class IdentificareAdmin(GuardedModelAdmin, HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['biserica']
    search_fields = ["biserica__nume"]