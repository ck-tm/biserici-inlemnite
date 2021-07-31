from django.contrib import admin
from django.contrib.auth.models import Permission
# Register your models here.
from nomenclatoare import models
from guardian.admin import GuardedModelAdmin

from simple_history.admin import SimpleHistoryAdmin

class HistoryChangedFields(object):
    history_list_display = ["changed_fields"]
    def changed_fields(self, obj):
        if obj.prev_record:
            delta = obj.diff_against(obj.prev_record)
            return delta.changed_fields
        return None

@admin.register(models.Localitate)
class LocalitateAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume', 'nr_biserici']
    search_fields = ["nume"]
    list_filter = ["judet"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.Judet)
class JudetAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume', 'cod', 'nr_biserici']
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
           return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.StatutBiserica)
class StatutBisericaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume', 'nr_biserici']
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
           return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.CultBiserica)
class CultBisericaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume', 'nr_biserici']
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
           return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.UtilizareBiserica)
class UtilizareBisericaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume', 'nr_biserici']
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
           return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.SingularitateBiserica)
class SingularitateBisericaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume', 'nr_biserici']
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
           return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.ProprietateBiserica)
class ProprietateBisericaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume', 'nr_biserici']
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
           return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.FunctiuneBiserica)
class FunctiuneBisericaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume', 'nr_biserici', 'nr_biserici_initiale']
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
           return obj.biserici.count()
        except:
            return 'N.A.'

    def nr_biserici_initiale(self, obj):
       return obj.biserici_initiale.count()


@admin.register(models.SursaDatare)
class SursaDatareAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume', 'nr_biserici']
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
           return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.Secol)
class SecolAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ['nume', 'nr_biserici']
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
           return obj.biserici.count()
        except:
            return 'N.A.'


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


@admin.register(models.AmplasamentBiserica)
class AmplasamentBisericaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.TopografieBiserica)
class TopografieBisericaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.RelatieCimitir)
class RelatieCimitirAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.PeisagisticaSit)
class PeisagisticaSitAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.ElementAnsambluConstruit)
class ElementAnsambluConstruitAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.ElementImportant)
class ElementImportantAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.Planimetrie)
class PlanimetrieAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.Material)
class MaterialAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.DimensiuneTurn)
class DimensiuneTurnAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.TipTurn)
class TipTurnAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.DecorTurn)
class DecorTurnAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.PlanTurn)
class PlanTurnAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.AmplasareTurn)
class AmplasareTurnAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.GalerieTurn)
class GalerieTurnAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.TipSarpanta)
class TipSarpantaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.FinisajExterior)
class FinisajExteriorAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.TipBatereSindrila)
class TipBatereSindrilaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.TipPrindereSindrila)
class TipPrindereSindrilaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.TipBotSindrila)
class TipBotSindrilaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.TipPrelucrareSindrila)
class TipPrelucrareSindrilaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.EsentaLemnoasa)
class EsentaLemnoasaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.ElementBiserica)
class ElementBisericaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.MaterialFinisajPardoseli)
class MaterialFinisajPardoseliAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.MaterialFinisajPeretiInteriori)
class MaterialFinisajPeretiInterioriAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.Finisaj)
class FinisajAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.TipFundatie)
class TipFundatieAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.TipStructuraCheotoare)
class TipStructuraCheotoareAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.TipStructuraCatei)
class TipStructuraCateiAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.LocalizarePictura)
class LocalizarePicturaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.TehnicaPictura)
class TehnicaPicturaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'

@admin.register(models.RegistruIconostas)
class RegistruIconostasAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'

@admin.register(models.TipUsiIconostas)
class TipUsiIconostasAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'

@admin.register(models.SuportPictura)
class SuportPicturaAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.FinisajIconostas)
class FinisajIconostasAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.TipIconostas)
class TipIconostasAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.DetaliuPodTurn)
class DetaliuPodTurnAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'




@admin.register(models.AsezareTalpaTurn)
class AsezareTalpaTurnAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'

@admin.register(models.RelatieTalpaTurn)
class RelatieTalpaTurnAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'



@admin.register(models.BoltaPesteAltar)
class BoltaPesteAltarAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.TipBoltaPesteAltar)
class TipBoltaPesteAltarAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.TipBoltaPronaos)
class TipBoltaPronaosAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'


@admin.register(models.Mobilier)
class MobilierAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'




@admin.register(models.ObiectCult)
class ObiectCultAdmin(HistoryChangedFields, SimpleHistoryAdmin):
    list_display = ["nume", "nr_biserici"]
    search_fields = ["nume"]

    def nr_biserici(self, obj):
        try:
            return obj.biserici.count()
        except:
            return 'N.A.'




