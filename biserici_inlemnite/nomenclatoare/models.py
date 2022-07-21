from django.db import models
from simple_history.models import HistoricalRecords

from wagtail.snippets.models import register_snippet
from wagtail.search import index

from wagtailmodelchooser import register_model_chooser, Chooser


class CustomChooser(Chooser):
    modal_template = "wagtailmodelchooser/modal.html"
    modal_results_template = "wagtailmodelchooser/results.html"


@register_snippet
@register_model_chooser
class Judet(index.Indexed, models.Model):
    """
    Description: Model Description
    """

    nume = models.CharField(max_length=50)
    cod = models.CharField(max_length=2)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Județe"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class Comuna(index.Indexed, models.Model):
    """
    Description: Model Description
    """

    nume = models.CharField(max_length=50)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Comune"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class Localitate(index.Indexed, models.Model):
    """
    Description: Model Description
    """

    nume = models.CharField(max_length=50)
    judet = models.ForeignKey("Judet", on_delete=models.CASCADE)
    comuna = models.ForeignKey("Comuna", on_delete=models.CASCADE, null=True, blank=True)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Localități"
        ordering = ["nume"]

    def __str__(self):
        if self.comuna:
            return f"{self.nume}, com. {self.comuna.nume}"
        return self.nume


@register_snippet
@register_model_chooser
class FunctiuneBiserica(index.Indexed, models.Model):
    """
    Description: Model Description
    """

    nume = models.CharField(max_length=150)
    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Funcțiuni Biserică"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class StatutBiserica(index.Indexed, models.Model):
    """
    Description: Model Description
    """

    nume = models.CharField(max_length=150)
    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Statuturi Biserică"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class CultBiserica(index.Indexed, models.Model):
    """
    Description: Model Description
    """

    nume = models.CharField(max_length=150)
    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Culte biserică"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class UtilizareBiserica(index.Indexed, models.Model):
    """
    Description: Model Description
    """

    nume = models.CharField(max_length=150)
    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Utilizări Biserică"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class SingularitateBiserica(index.Indexed, models.Model):
    """
    Description: Model Description
    """

    nume = models.CharField(max_length=150)
    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Singularități Biserică"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class RegimProprietate(index.Indexed, models.Model):
    """
    Description: Model Description
    """

    nume = models.CharField(max_length=150)
    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Regimul de proprietate"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class SursaDatare(index.Indexed, models.Model):
    """
    Description: Model Description
    """

    nume = models.CharField(max_length=150)
    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Surse Datări"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class StudiuDendocronologic(index.Indexed, models.Model):
    """
    Description: Model Description
    """

    nume = models.CharField(max_length=150)
    fisier = models.FileField()
    an = models.IntegerField(null=True, blank=True)
    autor = models.CharField(max_length=150, null=True, blank=True)
    detalii = models.TextField(null=True, blank=True)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Studii dendocronologice"
        ordering = ["nume"]

    def __str__(self):
        return f"{self.nume} - {self.autor} ({self.an})"


class Persoana(index.Indexed, models.Model):
    """
    Description: Model Description
    """

    nume = models.CharField(max_length=150)
    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Persoane"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class Studiu(index.Indexed, models.Model):
    """
    Description: Model Description
    """

    nume = models.CharField(max_length=150)
    fisier = models.FileField()
    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Studii"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class Secol(index.Indexed, models.Model):
    """
    Description: Model Description
    """

    nume = models.CharField(max_length=6)
    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Secole"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class AmplasamentBiserica(index.Indexed, models.Model):
    """
    Capitol: Amplasament Biserica
    """

    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Amplasamente Biserică"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TopografieBiserica(index.Indexed, models.Model):
    """
    Capitol: Topografie Biserica
    """

    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Topografii Biserică"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class RelatieCimitir(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Relația cu cimitirul"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class PeisagisticaSit(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Peisagistica sitului"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class ElementAnsambluConstruit(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Elemente Ansamblu Construit"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class ElementImportant(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Elemente Importante"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class Planimetrie(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Planimetrii"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class Material(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Materiale"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class MaterialMobilier(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Materiale mobilier"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class MaterialMasaAltar(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Materiale masă altar"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class MaterialIconostas(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Materiale Iconostas"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class MaterialCruci(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Materiale Cruci"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class MaterialBolta(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Materiale Boltă"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class MaterialCor(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Materiale Cor"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class MaterialeStructura(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Materiale Structura"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class MaterialeStructuraBolta(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Materiale Structură Boltă"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class DimensiuneTurn(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Dimensiuni Turn"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipTurn(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri Turn"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class DecorTurn(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Decoruri Turn"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class PlanTurn(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Planuri Turn"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class AmplasareTurn(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Amplasări Turn"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class GalerieTurn(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Galerii Turn"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipSarpanta(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri Sarpanta"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class FinisajExterior(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Finisaje Exterioare"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class FinisajInvelitoare(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Finisaj Învelitore"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipBatereSindrila(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri Batere Sindrila"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipPrindereSindrila(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri montaj șindrilă"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipBotSindrila(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri Bot Sindrila"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipPrelucrareSindrila(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri Prelucrare Sindrila"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class EsentaLemnoasa(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Esenta Lemnoasa"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class ElementInteriorBiserica(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Elemente interior Biserica"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class ElementBiserica(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Elemente Biserica"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class MaterialFinisajPardoseli(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Material Finisaj Pardoseli"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class MaterialFinisajPeretiInteriori(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Material Finisaj Pereti Interiori"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class Finisaj(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Finisaje biserică"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipFundatie(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri Fundatie"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipStructuraCheotoare(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri Structură Cheotoare"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipStructuraCatei(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri Structură Căței"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class LocalizarePictura(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Localizări Pictură"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TehnicaPictura(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tehnici Pictura"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class SuportPictura(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Suport Pictură"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TehnicaIconostas(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tehnici Iconostas"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class RegistruIconostas(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Registre Iconostas"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipIconostas(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri Iconostas"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipUsiIconostas(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri Uși Iconostas"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class DetaliuPodTurn(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Detalii podul turnului"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class AsezareTalpaTurn(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Așezări talpă turn"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class RelatieTalpaTurn(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Relații talpă turn"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class BoltaPesteAltar(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Boltă peste altar"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipBoltaPesteAltar(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri boltă peste altar"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipBoltaPronaos(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri boltă pronaos/naos"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class Mobilier(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Mobilier"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class ObiectCult(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Obiecte de Cult"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipArcBolta(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri arc boltă"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class PozitionareTurle(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Poziționare turle"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class StilTurle(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Stilul turlelor"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipTiranti(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tip tiranti"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class MaterialInvelitoareTurle(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Material învelitoare turle"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class Hram(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Hram Biserică"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipSistemStructural(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField("nume", partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri sisteme structurale"
        ordering = ["nume"]

    def __str__(self):
        return self.nume
