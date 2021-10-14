from django.db import models
from simple_history.models import HistoricalRecords

from wagtail.snippets.models import register_snippet
from wagtail.search import index

from wagtailmodelchooser import register_model_chooser, Chooser


class CustomChooser(Chooser):
    modal_template = 'wagtailmodelchooser/modal.html'
    modal_results_template = \
        'wagtailmodelchooser/results.html'


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
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Județe"
        ordering = ['nume']

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
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Comune"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class Localitate(index.Indexed, models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=50)
    judet = models.ForeignKey('Judet', on_delete=models.CASCADE)
    comuna = models.ForeignKey(
        'Comuna', on_delete=models.CASCADE, null=True, blank=True)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Localități"
        ordering = ['nume']

    def __str__(self):
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
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Funcțiuni Biserică"
        ordering = ['nume']

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
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Statuturi Biserică"
        ordering = ['nume']

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
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Culturi Biserică"
        ordering = ['nume']

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
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Utilizări Biserică"
        ordering = ['nume']

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
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Singularități Biserică"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class ProprietateBiserica(index.Indexed, models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Proprietăți Biserică"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class MutareBiserica(index.Indexed, models.Model):
    """
    Description: Model Description
    """
    istoric = models.ForeignKey('biserici.Istoric', on_delete=models.CASCADE)
    localitate = models.ForeignKey(
        'Localitate', null=True, blank=True, on_delete=models.SET_NULL)
    latitudine = models.FloatField(null=True, blank=True)
    longitudine = models.FloatField(null=True, blank=True)
    history = HistoricalRecords()
    # search_fields = [
    # index.SearchField('nume', partial_match=True, boost=10),
    # ]

    class Meta:
        verbose_name_plural = 'Mutări Biserică'


@register_snippet
@register_model_chooser
class SursaDatare(index.Indexed, models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = 'Surse Datări'
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
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
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = 'Studii dendocronologice'
        ordering = ['nume']

    def __str__(self):
        return f"{self.nume} - {self.autor} ({self.an})"


@register_snippet
@register_model_chooser
class Persoana(index.Indexed, models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = 'Persoane'
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class Eveniment(index.Indexed, models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = 'Evenimente'
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class CtitorBiserica(models.Model):
    """
    Description: Model Description
    """
    persoana = models.ForeignKey('Persoana', on_delete=models.CASCADE)
    istoric = models.ForeignKey(
        'biserici.Istoric', on_delete=models.SET_NULL, null=True, blank=True)
    detalii = models.TextField()
    sursa = models.TextField()
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = 'Ctitori'

    def __str__(self):
        return self.persoana


@register_snippet
@register_model_chooser
class ZugravBiserica(models.Model):
    """
    Description: Model Description
    """
    persoana = models.ForeignKey('Persoana', on_delete=models.CASCADE)
    istoric = models.ForeignKey(
        'biserici.Istoric', on_delete=models.SET_NULL, null=True, blank=True)
    detalii = models.TextField()
    sursa = models.TextField()
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = 'Zugravi'

    def __str__(self):
        return self.persoana


@register_snippet
@register_model_chooser
class MesterBiserica(models.Model):
    """
    Description: Model Description
    """
    persoana = models.ForeignKey('Persoana', on_delete=models.CASCADE)
    istoric = models.ForeignKey(
        'biserici.Istoric', on_delete=models.SET_NULL, null=True, blank=True)
    detalii = models.TextField()
    sursa = models.TextField()
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = 'Meșteri'

    def __str__(self):
        return self.persoana


@register_snippet
@register_model_chooser
class PersonalitateBiserica(models.Model):
    """
    Description: Model Description
    """
    persoana = models.ForeignKey('Persoana', on_delete=models.CASCADE)
    istoric = models.ForeignKey(
        'biserici.Istoric', on_delete=models.SET_NULL, null=True, blank=True)
    detalii = models.TextField()
    sursa = models.TextField()
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = 'Personalități Biserică'

    def __str__(self):
        return self.persoana


@register_snippet
@register_model_chooser
class EvenimentBiserica(models.Model):
    """
    Description: Model Description
    """
    eveniment = models.ForeignKey('Eveniment', on_delete=models.CASCADE)
    istoric = models.ForeignKey(
        'biserici.Istoric', null=True, blank=True, on_delete=models.SET_NULL)
    detalii = models.TextField()
    sursa = models.TextField()
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = 'Evenimente Istorice'

    def __str__(self):
        return self.eveniment.nume


@register_snippet
@register_model_chooser
class Studiu(index.Indexed, models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)
    fisier = models.FileField()
    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = 'Studii'
        ordering = ['nume']

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
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = 'Secole'
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class StudiuIstoric(index.Indexed, models.Model):
    """
    Description: Model Description
    """
    istoric = models.ForeignKey('biserici.Istoric', on_delete=models.CASCADE)
    nume = models.CharField(max_length=150)
    fisier = models.FileField()
    drepturi_de_autor = models.TextField()
    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = 'tudii Istorice'
        ordering = ['nume']

    def __str__(self):
        return self.studiu.nume


@register_snippet
@register_model_chooser
class AmplasamentBiserica(index.Indexed, models.Model):
    """
    Capitol: Amplasament Biserica
    """

    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Amplasamente Biserică"
        ordering = ['nume']

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
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Topografii Biserică"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class RelatieCimitir(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Relație Cimitir"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class PeisagisticaSit(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Peisagistică Sit"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class ElementAnsambluConstruit(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Elemente Ansamblu Construit"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class ElementImportant(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Elemente Importante"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class Planimetrie(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Planimetrii"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class Material(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Materiale"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class MaterialeStructura(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Materiale Structura"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class MaterialeStructuraBolta(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Materiale Structură Boltă"
        ordering = ['nume']

    def __str__(self):
        return self.nume

@register_snippet
@register_model_chooser
class DimensiuneTurn(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Dimensiuni Turn"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipTurn(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri Turn"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class DecorTurn(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Decoruri Turn"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class PlanTurn(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Planuri Turn"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class AmplasareTurn(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Amplasări Turn"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class GalerieTurn(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Galerii Turn"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipSarpanta(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri Sarpanta"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class FinisajExterior(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Finisaj Exterior"
        ordering = ['nume']
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipBatereSindrila(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri Batere Sindrila"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipPrindereSindrila(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri Prindere Sindrila"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipBotSindrila(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri Bot Sindrila"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipPrelucrareSindrila(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri Prelucrare Sindrila"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class EsentaLemnoasa(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Esenta Lemnoasa"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class ElementBiserica(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Elemente Biserica"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class MaterialFinisajPardoseli(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Material Finisaj Pardoseli"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class MaterialFinisajPeretiInteriori(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Material Finisaj Pereti Interiori"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class Finisaj(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Finisaj"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipFundatie(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri Fundatie"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipStructuraCheotoare(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri Structură Cheotoare"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipStructuraCatei(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri Structură Căței"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class LocalizarePictura(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Localizări Pictură"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TehnicaPictura(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tehnici Pictura"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class SuportPictura(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Suport Pictură"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class FinisajIconostas(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Finisaje Iconostas"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class RegistruIconostas(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Registre Iconostas"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipIconostas(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri Iconostas"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipUsiIconostas(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri Uși Iconostas"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class DetaliuPodTurn(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Detalii podul turnului"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class AsezareTalpaTurn(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Așezări talpă turn"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class RelatieTalpaTurn(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Relații talpă turn"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class BoltaPesteAltar(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Bolți peste altar"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipBoltaPesteAltar(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri boltă peste altar"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipBoltaPronaos(index.Indexed, models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri boltă pronaos/naos"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class Mobilier(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Mobilier"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class ObiectCult(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Obiecte Cult"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipArcBolta(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tipuri arc boltă"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class PozitionareTurle(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Poziționare turle"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class FormaSarpanteTurle(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Forme șarpante turle"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class TipTiranti(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Tip tiranti"
        ordering = ['nume']

    def __str__(self):
        return self.nume


@register_snippet
@register_model_chooser
class MaterialInvelitoareTurle(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Material învelitoare turle"
        ordering = ['nume']

    def __str__(self):
        return self.nume

@register_snippet
@register_model_chooser
class Hram(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()
    search_fields = [
        index.SearchField('nume', partial_match=True, boost=10),
    ]

    class Meta:
        verbose_name_plural = "Hramuri"
        ordering = ['nume']

    def __str__(self):
        return self.nume
