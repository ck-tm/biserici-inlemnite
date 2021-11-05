from app import blocks
from django.db import models
from django import forms
from django.utils.html import format_html
from django.contrib.postgres.fields import ArrayField, JSONField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel,
    PageChooserPanel,
    ObjectList,
    TabbedInterface,

    FieldRowPanel
)
from wagtail.search import index

from wagtail.core.models import Orderable, Page
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.models import ClusterableModel

from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from wagtailmodelchooser.edit_handlers import ModelChooserPanel

from wagtail.admin.edit_handlers import InlinePanel as BaseInlinePanel
from wagtail.admin.edit_handlers import EditHandler
from wagtail.api import APIField
from unidecode import unidecode

from .blocks import BaseStreamBlock


IDENTIFICARE_DOC_CADASTRALE = (
    (1, 'Da'),
    (2, 'Nu'),
    (3, 'În curs de'),
)


CLASE_EVALUARE = (
    (1, "A"),
    (2, "B"),
    (3, "C"),
)

NR15 = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

NR135 = (
    (1, 1),
    (3, 3),
    (5, 5),
)

ELEMENTE_BISERICA = (
    ('pardosea', 'pardosea'),
    ('pereți interiori', 'pereți interiori'),
    ('boltă', 'boltă'),
    ('tavan', 'tavan'),
)


class InlinePanel(BaseInlinePanel):
    def widget_overrides(self):
        widgets = {}
        child_edit_handler = self.get_child_edit_handler()
        for handler_class in child_edit_handler.children:
            widgets.update(handler_class.widget_overrides())
        widget_overrides = {self.relation_name: widgets}
        return widget_overrides


class ReadOnlyPanel(EditHandler):
    def __init__(self, attr, *args, **kwargs):
        self.attr = attr
        super().__init__(*args, **kwargs)

    def clone(self):
        return self.__class__(
            attr=self.attr,
            heading=self.heading,
            classname=self.classname,
            help_text=self.help_text,
        )

    def render(self):
        value = getattr(self.instance, self.attr)
        if callable(value):
            value = value()
        return format_html('<div style="padding-top: 1.2em;">{}</div>', value)

    def render_as_object(self):
        return format_html(
            '<fieldset><legend>{}</legend>'
            '<ul class="fields"><li><div class="field">{}</div></li></ul>'
            '</fieldset>',
            self.heading, self.render())

    def render_as_field(self):
        return format_html(
            '<div class="field">'
            '<label>{}{}</label>'
            '<div class="field-content">{}</div>'
            '</div>',
            self.heading, ':', self.render())


class HomePage(Page):
    """Home page model."""

    template = "home/home_page.html"
    subpage_types = [
        "BisericaPage"
    ]
    parent_page_type = [
        'wagtailcore.Page'
    ]

    class Meta:  # noqa

        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


class ParteneriProiect(Orderable):
    page = ParentalKey('AboutPage',
                       on_delete=models.CASCADE, related_name='parteneri')
    logo = models.ForeignKey('wagtailimages.Image', null=True,
                             blank=True, on_delete=models.SET_NULL, related_name='+')
    link = models.URLField(null=True, blank=True)

    panels = [
        ImageChooserPanel('logo'),
        FieldPanel('link'),
    ]


class AboutPage(Page):
    """Home page model."""
    body = StreamField(BaseStreamBlock(), verbose_name="Secțiuni", null=True, blank=True)

    subpage_types = []
    parent_page_type = [
        'wagtailcore.Page'
    ]

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        InlinePanel('parteneri', label="Partner")
    ]

    class Meta:  # noqa
        verbose_name_plural = "About Pages"




class PozeBiserica(Orderable):
    page = ParentalKey('BisericaPage',
                       on_delete=models.CASCADE, related_name='poze')
    poza = models.ForeignKey('wagtailimages.Image', null=True,
                             blank=True, on_delete=models.SET_NULL, related_name='+')
    rendition = models.JSONField(null=True, blank=True)
    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        ImageChooserPanel('poza'),
        FieldPanel('observatii'),
    ]


class BisericaPage(Page):
    """Home page model."""

    subpage_types = [
        "IdentificarePage",
        "DescrierePage",
        "ComponentaArtisticaPage",
        "ConservarePage",
        "ValoarePage",
        "IstoricPage",
    ]

    identificare_page = models.ForeignKey('IdentificarePage', null=True, blank=True,
                              on_delete=models.SET_NULL)
    descriere_page = models.ForeignKey('DescrierePage', null=True, blank=True,
                              on_delete=models.SET_NULL)
    componenta_artistica_page = models.ForeignKey('ComponentaArtisticaPage', null=True, blank=True,
                              on_delete=models.SET_NULL)
    istoric_page = models.ForeignKey('IstoricPage', null=True, blank=True,
                              on_delete=models.SET_NULL)
    valoare_page = models.ForeignKey('ValoarePage', null=True, blank=True,
                              on_delete=models.SET_NULL)
    conservare_page = models.ForeignKey('ConservarePage', null=True, blank=True,
                              on_delete=models.SET_NULL)

    judet = models.ForeignKey('nomenclatoare.Judet', null=True, blank=True,
                              on_delete=models.SET_NULL, related_name='pp_biserici', verbose_name="Județ")
    localitate = models.ForeignKey('nomenclatoare.Localitate', null=True,
                                   blank=True, on_delete=models.SET_NULL, related_name='pp_biserici', verbose_name="Localitate")
    utitle = models.CharField(max_length=250, null=True, blank=True, verbose_name="UTitle")
    adresa = models.CharField(max_length=250, null=True, blank=True, verbose_name="Adresă")
    latitudine = models.FloatField(null=True, blank=True, verbose_name="Latitudine")
    longitudine = models.FloatField(null=True, blank=True, verbose_name="Longitudine")

    valoare = models.FloatField(max_length=5, null=True, blank=True)
    conservare = models.FloatField(null=True, blank=True)
    prioritizare = models.FloatField(null=True, blank=True)

    datare_an = models.IntegerField(null=True, blank=True)
    datare_prin_interval_timp = models.CharField(
        max_length=50, null=True, blank=True)
    datare_secol = models.ForeignKey('nomenclatoare.Secol', null=True,
                                     blank=True, on_delete=models.SET_NULL, related_name='pp_biserici')
    promote_panels = []

    content_panels = Page.content_panels + [
        # ModelChooserPanel("judet", disabled=True),
        MultiFieldPanel([
            InlinePanel("poze", label="Poză")
        ],
            heading='Poze',
            classname='collapsible'
        ),
        MultiFieldPanel([
            ReadOnlyPanel("utitle", heading="U Title"),
            ReadOnlyPanel("judet", heading="Judet"),
            ReadOnlyPanel("localitate", heading="localitate"),
            ReadOnlyPanel("adresa", heading="adresa"),
            ReadOnlyPanel("latitudine", heading="latitudine"),
            ReadOnlyPanel("longitudine", heading="longitudine"),
            ReadOnlyPanel("datare_an", heading="Datare An"),
            ReadOnlyPanel("datare_prin_interval_timp", heading="Interval Datare"),
            ReadOnlyPanel("datare_secol", heading="Secol Datare"),
            ReadOnlyPanel("valoare", heading="Clasa valoare"),
            ReadOnlyPanel("conservare", heading="Nota conservare"),
            ReadOnlyPanel("prioritizare", heading="Nota Prioritizare"),

            ReadOnlyPanel("identificare_page", heading="identificare page"),
            ReadOnlyPanel("descriere_page", heading="descriere page"),
            ReadOnlyPanel("componenta_artistica_page", heading="componenta_artistica page"),
            ReadOnlyPanel("istoric_page", heading="istoric page"),
            ReadOnlyPanel("valoare_page", heading="valoare page"),
            ReadOnlyPanel("conservare_page", heading="conservare page"),
        ],
            heading='Hidden',
            classname='collapsible'
        ),
    ]

    class Meta:  # noqa

        verbose_name = "Biserică"
        verbose_name_plural = "Biserici"

    def save(self, *args, **kwargs):
        self.utitle = unidecode(self.title)
        return super().save(*args, **kwargs)



class IdentificarePage(Page):
    """Home page model."""

    judet = models.ForeignKey('nomenclatoare.Judet', null=True, blank=True,
                              on_delete=models.SET_NULL, related_name='ppp_biserici', verbose_name="Județ")
    localitate = models.ForeignKey('nomenclatoare.Localitate', null=True,
                                   blank=True, on_delete=models.SET_NULL, related_name='p_biserici', verbose_name="Localitate")
    adresa = models.CharField(max_length=250, null=True, blank=True, verbose_name="Adresă")
    latitudine = models.FloatField(null=True, blank=True, verbose_name="Latitudine")
    longitudine = models.FloatField(null=True, blank=True, verbose_name="Longitudine")
    statut = models.ForeignKey('nomenclatoare.StatutBiserica', null=True,
                               blank=True, on_delete=models.SET_NULL, related_name='p_biserici')
    hram = models.ForeignKey('nomenclatoare.Hram', null=True,
                               blank=True, on_delete=models.SET_NULL, related_name='p_biserici')
    denumire_actuala = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Actuală")
    denumire_precedenta = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Precendentă")
    denumire_locala = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Locală")
    denumire_oberservatii = RichTextField(
        features=[], null=True, blank=True, verbose_name="Observații")
    cult = models.ForeignKey('nomenclatoare.CultBiserica', null=True,
                             blank=True, on_delete=models.SET_NULL, related_name='p_biserici')
    utilizare = models.ForeignKey('nomenclatoare.UtilizareBiserica', null=True,
                                  blank=True, on_delete=models.SET_NULL, related_name='p_biserici')
    utilizare_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name="Observații")
    singularitate = models.ForeignKey('nomenclatoare.SingularitateBiserica',
                                      null=True, blank=True, on_delete=models.SET_NULL, related_name='p_biserici')
    singularitate_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name="Observații")
    functiune = models.ForeignKey('nomenclatoare.FunctiuneBiserica', null=True,
                                  blank=True, on_delete=models.SET_NULL, related_name='p_biserici')
    functiune_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')
    functiune_initiala = models.ForeignKey('nomenclatoare.FunctiuneBiserica', null=True,
                                           blank=True, on_delete=models.SET_NULL, related_name='p_biserici_initiale')
    functiune_initiala_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')
    proprietate_actuala = models.ForeignKey('nomenclatoare.RegimProprietate', null=True,
                                            blank=True, on_delete=models.SET_NULL, related_name='p_biserici_initiale')
    proprietate_observatii = RichTextField(features=[], null=True, blank=True)
    proprietar_actual = RichTextField(features=[], null=True, blank=True)
    inscriere_documente_cadastrale = models.IntegerField(
        choices=IDENTIFICARE_DOC_CADASTRALE, null=True, blank=True)

    subpage_types = []

    content_panels = [
        MultiFieldPanel(
            [
                ModelChooserPanel("judet"),
                ModelChooserPanel("localitate"),
                FieldPanel("adresa"),
                FieldPanel("latitudine"),
                FieldPanel("longitudine")],
            heading="Localizare",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel("statut")],
            heading="Statut",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel("hram")],
            heading="Hram",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel("denumire_actuala"),
                FieldPanel("denumire_precedenta"),
                FieldPanel("denumire_locala"),
                FieldPanel("denumire_oberservatii")
            ],
            heading="Denumire",
            classname="collapsible collapsed ",
        ), MultiFieldPanel(
            [
                FieldPanel("cult"),
            ],
            heading="Cult",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel("utilizare"),
                FieldPanel("utilizare_observatii"),
            ],
            heading="Utilizare",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel("singularitate"),
                FieldPanel("singularitate_observatii"),
            ],
            heading="Singularitate",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel("functiune"),
                FieldPanel("functiune_observatii"),
                FieldPanel("functiune_initiala"),
                FieldPanel("functiune_initiala_observatii"),
            ],
            heading="Funcțiune",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel("proprietate_actuala"),
                FieldPanel("proprietate_observatii"),
                FieldPanel("proprietar_actual"),
            ],
            heading="Proprietate",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel("inscriere_documente_cadastrale")
            ],
            heading="Înscriere documente cadastrale",
            classname="collapsible collapsed ",
        ),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading='Identificare'),
        ]
    )

    class Meta:  # noqa

        verbose_name = "Identificare"
        verbose_name_plural = "Identificare"

    def save(self, *args, **kwargs):
        biserica = self.get_parent().specific
        biserica.judet = self.judet
        biserica.localitate = self.localitate
        biserica.adresa = self.adresa
        biserica.latitudine = self.latitudine
        biserica.longitudine = self.longitudine
        biserica.save_revision()
        return super().save(*args, **kwargs)


class PozeElementAnsambluConstruit(Orderable):
    page = ParentalKey('ElementeAnsambluConstruit',
                       on_delete=models.CASCADE, related_name='poze')
    poza = models.ForeignKey('wagtailimages.Image', null=True,
                             blank=True, on_delete=models.SET_NULL, related_name='+')
    rendition = models.JSONField(null=True, blank=True)
    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        ImageChooserPanel('poza'),
        FieldPanel('observatii'),
    ]


class ElementAnsambluConstruit(ClusterableModel):
    element = models.ForeignKey(
        'nomenclatoare.ElementAnsambluConstruit', on_delete=models.CASCADE)
    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')
    element_important  = models.BooleanField(default=False)
    element_disonant  = models.BooleanField(default=False)

    panels = [
        FieldPanel('element'),
        FieldPanel('element_important'),
        FieldPanel('element_disonant'),
        FieldPanel('observatii'),
        InlinePanel('poze', label='Poză'),
    ]

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.element)

class ElementeAnsambluConstruit(Orderable, ElementAnsambluConstruit):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='elemente_ansamblu_construit')


class PozeElementImportantAnsambluConstruit(Orderable):
    page = ParentalKey('ElementeImportanteAnsambluConstruit',
                       on_delete=models.CASCADE, related_name='poze')
    poza = models.ForeignKey('wagtailimages.Image', null=True,
                             blank=True, on_delete=models.SET_NULL, related_name='+')
    rendition = models.JSONField(null=True, blank=True)
    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        ImageChooserPanel('poza'),
        FieldPanel('observatii'),
    ]


class ElementImportantAnsambluConstruit(ClusterableModel):
    element = models.ForeignKey(
        'nomenclatoare.ElementImportant', on_delete=models.CASCADE)
    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')
    element_important  = models.BooleanField(default=False)
    element_disonant  = models.BooleanField(default=False)

    panels = [
        FieldPanel('element'),
        FieldPanel('element_important'),
        FieldPanel('element_disonant'),
        FieldPanel('observatii'),
        InlinePanel('poze', label='Poză'),
    ]

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.element)

class ElementeImportanteAnsambluConstruit(Orderable, ElementImportantAnsambluConstruit):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='elemente_importante_ansamblu_construit')


class PozeClopot(Orderable):
    page = ParentalKey('ClopoteBiserica',
                       on_delete=models.CASCADE, related_name='poze_clopot')
    poza = models.ForeignKey('wagtailimages.Image', null=True,
                             blank=True, on_delete=models.SET_NULL, related_name='+')
    rendition = models.JSONField(null=True, blank=True)

    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        ImageChooserPanel('poza'),
        FieldPanel('observatii'),
    ]


class ClopotBiserica(ClusterableModel):
    an = models.IntegerField(null=True, blank=True, verbose_name='An')
    inscriptie = RichTextField(
        features=[], null=True, blank=True, verbose_name='Inscripție')
    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        FieldPanel('an'),
        FieldPanel('inscriptie'),
        InlinePanel('poze_clopot', label='Poze')
    ]

    class Meta:
        abstract = True


    def __str__(self):
        return str(self.an) if self.an else 'Fără datare'

class ClopoteBiserica(Orderable, ClopotBiserica):
    page = ParentalKey(
        'DescrierePage', on_delete=models.CASCADE, related_name='clopote')


class PozeFinisajPortic(Orderable):
    page_portic = ParentalKey(
        'FinisajePortic', on_delete=models.CASCADE, related_name='poze_finisaj')
    poza = models.ForeignKey('wagtailimages.Image', null=True,
                             blank=True, on_delete=models.SET_NULL, related_name='+')
    rendition = models.JSONField(null=True, blank=True)

    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        ImageChooserPanel('poza'),
        FieldPanel('observatii'),
    ]


class FinisajePortic(ClusterableModel, Orderable):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='finisaje_portic')
    element = models.ForeignKey(
        'nomenclatoare.ElementInteriorBiserica', on_delete=models.SET_NULL, null=True, blank=True)
    material = models.ForeignKey(
        'nomenclatoare.Finisaj', null=True, blank=True, on_delete=models.CASCADE)
    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        FieldPanel('element'),
        FieldPanel('material'),
        FieldPanel('observatii'),
        InlinePanel('poze_finisaj', label='Poze')
    ]

    def __str__(self):
        return str(self.element)

class PozeFinisajPronaos(Orderable):
    page_pronaos = ParentalKey(
        'FinisajePronaos', on_delete=models.CASCADE, related_name='poze_finisaj')
    poza = models.ForeignKey('wagtailimages.Image', null=True,
                             blank=True, on_delete=models.SET_NULL, related_name='+')
    rendition = models.JSONField(null=True, blank=True)

    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        ImageChooserPanel('poza'),
        FieldPanel('observatii'),
    ]


class FinisajePronaos(ClusterableModel, Orderable):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='finisaje_pronaos')
    element = models.ForeignKey(
        'nomenclatoare.ElementInteriorBiserica', on_delete=models.SET_NULL, null=True, blank=True)
    material = models.ForeignKey(
        'nomenclatoare.Finisaj', null=True, blank=True, on_delete=models.CASCADE)
    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        FieldPanel('element'),
        FieldPanel('material'),
        FieldPanel('observatii'),
        InlinePanel('poze_finisaj', label='Poze')
    ]

    def __str__(self):
        return str(self.element)

class PozeFinisajNaos(Orderable):
    page_naos = ParentalKey(
        'FinisajeNaos', on_delete=models.CASCADE, related_name='poze_finisaj')
    poza = models.ForeignKey('wagtailimages.Image', null=True,
                             blank=True, on_delete=models.SET_NULL, related_name='+')
    rendition = models.JSONField(null=True, blank=True)

    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        ImageChooserPanel('poza'),
        FieldPanel('observatii'),
    ]


class FinisajeNaos(ClusterableModel, Orderable):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='finisaje_naos')
    element = models.ForeignKey(
        'nomenclatoare.ElementInteriorBiserica', on_delete=models.SET_NULL, null=True, blank=True)
    material = models.ForeignKey(
        'nomenclatoare.Finisaj', null=True, blank=True, on_delete=models.CASCADE)
    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        FieldPanel('element'),
        FieldPanel('material'),
        FieldPanel('observatii'),
        InlinePanel('poze_finisaj', label='Poze')
    ]

    def __str__(self):
        return str(self.element)

class PozeFinisajAltar(Orderable):
    page_altar = ParentalKey(
        'FinisajeAltar', on_delete=models.CASCADE, related_name='poze_finisaj')
    poza = models.ForeignKey('wagtailimages.Image', null=True,
                             blank=True, on_delete=models.SET_NULL, related_name='+')
    rendition = models.JSONField(null=True, blank=True)
    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        ImageChooserPanel('poza'),
        FieldPanel('observatii'),
    ]


class FinisajeAltar(ClusterableModel, Orderable):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='finisaje_altar')
    element = models.ForeignKey(
        'nomenclatoare.ElementInteriorBiserica', on_delete=models.SET_NULL, null=True, blank=True)
    material = models.ForeignKey(
        'nomenclatoare.Finisaj', null=True, blank=True, on_delete=models.CASCADE)
    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        FieldPanel('element'),
        FieldPanel('material'),
        FieldPanel('observatii'),
        InlinePanel('poze_finisaj', label='Poze')
    ]

    def __str__(self):
        return str(self.element)


class Poza(models.Model):
    poza = models.ForeignKey('wagtailimages.Image', null=True,
                             blank=True, on_delete=models.SET_NULL, related_name='+')
    rendition = models.JSONField(null=True, blank=True)

    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        ImageChooserPanel('poza'),
        FieldPanel('observatii')
    ]

    api_fields = [
        APIField('poza'),
        APIField('observatii'),
    ]

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.poza)


class PozeAccese(Orderable, Poza):
    page = ParentalKey(
        'DescrierePage', on_delete=models.CASCADE, related_name='poze_accese')


class PozeFerestre(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='poze_ferestre')


class PozeOchiesi(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='poze_ochiesi')


class PozeSolee(Orderable, Poza):
    page = ParentalKey(
        'DescrierePage', on_delete=models.CASCADE, related_name='poze_solee')


class PozeMasaAtlar(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='poze_masa_atlar')


class PozeDescriereBolti(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='poze_bolti')


class PozeCor(Orderable, Poza):
    page = ParentalKey(
        'DescrierePage', on_delete=models.CASCADE, related_name='poze_cor')


class PozeSarpanta(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='poze_sarpanta')


class PozeTurn(Orderable, Poza):
    page = ParentalKey(
        'DescrierePage', on_delete=models.CASCADE, related_name='poze_turn')


class PozeClopote(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='poze_clopote')


class PozeTurle(Orderable, Poza):
    page = ParentalKey(
        'DescrierePage', on_delete=models.CASCADE, related_name='poze_turle')


class PozeGeneraleExterior(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='poze_generale_exterior')


class PozeGeneraleInterior(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='poze_generale_interior')


class PozeAmplasament(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='poze_amplasament')


class PozePeisagisticaSitului(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='poze_peisagistica_sitului')


class PozeFundatie(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='poze_fundatie')


class PozeStructuraCheotoare(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='poze_structura_cheotoare')


class PozeStructuraCatei(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='poze_structura_catei')


class PozeStructuraMixt(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='poze_structura_mixt')


class PozeTiranti(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='poze_tiranti')

class PozeEtapeAnterioareInvelitoare(Orderable, Poza):
        page = ParentalKey(
            'DescrierePage', on_delete=models.CASCADE, related_name='poze_interventii_invelitoare')


class PozeFinisajeInvelitoare(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='poze_invelitoare')

class PozeFinisajeInvelitoareTurle(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='poze_invelitoare_turle')


class PozeFinisajeInchidereTambur(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='poze_inchidere_tambur')

class PozeFinisajeInvelitoareTurn(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='poze_invelitoare_turn')

class PozeFinisajeExteriorCorp(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='poze_exterior_corp')



class PozeEtapeIstoriceVizibile(Orderable):
    page = ParentalKey('EtapeIstoriceVizibile',
                       on_delete=models.CASCADE, related_name='poze')
    poza = models.ForeignKey('wagtailimages.Image', null=True,
                             blank=True, on_delete=models.SET_NULL, related_name='+')
    rendition = models.JSONField(null=True, blank=True)
    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        ImageChooserPanel('poza'),
        FieldPanel('observatii'),
    ]

class EtapeIstoriceVizibile(ClusterableModel, Orderable):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE,
                       related_name='etape_istorice_vizibile')

    element = models.ForeignKey(
        'nomenclatoare.ElementBiserica', on_delete=models.SET_NULL, null=True, blank=True)
    datat = models.BooleanField(default=False)
    an = models.IntegerField(null=True, blank=True)
    interventie_neconforma = models.BooleanField(default=False)
    sursa = RichTextField(features=[], null=True, blank=True)
    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        FieldPanel('element'),
        FieldPanel('datat'),
        FieldPanel('an'),
        FieldPanel('interventie_neconforma'),
        FieldPanel('sursa'),
        FieldPanel('observatii'),
        InlinePanel('poze', label='Poză'),
    ]

    def __str__(self):
        return str(self.element)

class DescrierePage(Page):
    """
    Capitol: Descriere Biserica
    """

    # Localizare/peisaj
    amplasament = models.ForeignKey(
        'nomenclatoare.AmplasamentBiserica', null=True, blank=True, on_delete=models.SET_NULL)
    topografie = models.ForeignKey(
        'nomenclatoare.TopografieBiserica', null=True, blank=True, on_delete=models.SET_NULL)
    toponim = models.CharField(
        max_length=150, null=True, blank=True, help_text="denumirea locului")
    toponim_sursa = RichTextField(
        features=[], null=True, blank=True, verbose_name='Sursă informații')
    relatia_cu_cimitirul = models.ForeignKey(
        'nomenclatoare.RelatieCimitir', null=True, blank=True, on_delete=models.SET_NULL)
    peisagistica_sitului = ParentalManyToManyField(
        'nomenclatoare.PeisagisticaSit', blank=True)
    observatii = RichTextField(features=[], null=True, blank=True)

    # Ansamblu construit
    elemente = ParentalManyToManyField(
        'nomenclatoare.ElementInteriorBiserica', help_text="Elemente ansamblu construit", blank=True)
    detalii_elemente = RichTextField(features=[], null=True, blank=True)

    elemente_importante = ParentalManyToManyField(
        'nomenclatoare.ElementImportant', help_text="Elemente ansamblu construit", blank=True)
    detalii_elemente_importante = RichTextField(
        features=[], null=True, blank=True)

    # Arhitectura bisericii
    planimetria_bisericii = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    materiale = models.ForeignKey(
        'nomenclatoare.MaterialeStructura', help_text="Materiale folosite in construcția bisericii", null=True, blank=True,
        on_delete=models.SET_NULL)
    detalii_materiale = RichTextField(features=[], null=True, blank=True,
                                      help_text="Materialele care compun structura de rezistentă a bisericii")

    # Elemente arhitecturale

    turn_dimensiune = models.ForeignKey(
        'nomenclatoare.DimensiuneTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Dimensiune')
    turn_tip = models.ForeignKey('nomenclatoare.TipTurn', null=True,
                                 blank=True, on_delete=models.SET_NULL, verbose_name='Tip')
    turn_numar = models.IntegerField(
        null=True, blank=True, verbose_name='Număr de turnuri')
    turn_numar_stalpi = models.IntegerField(
        null=True, blank=True, verbose_name='Număr stâlpi')
    turn_plan = models.ForeignKey('nomenclatoare.PlanTurn', null=True,
                                  blank=True, on_delete=models.SET_NULL, verbose_name='Plan')
    turn_amplasare = models.ForeignKey(
        'nomenclatoare.AmplasareTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Amplasare')
    turn_galerie = models.ForeignKey('nomenclatoare.GalerieTurn', null=True,
                                     blank=True, on_delete=models.SET_NULL, verbose_name='Galerie')
    turn_numar_arcade = models.IntegerField(
        null=True, blank=True, verbose_name='Număr arcade Turn deschis')
    turn_numar_arcade_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Detalii arcade Turn deschis')
    turn_asezare_talpi = models.ForeignKey('nomenclatoare.AsezareTalpaTurn', null=True, blank=True,
                                           on_delete=models.SET_NULL, verbose_name='Așezarea tălpilor turnului în legătură cu corpul bisericii')
    turn_relatie_talpi = models.ForeignKey('nomenclatoare.RelatieTalpaTurn', null=True,
                                           blank=True, on_delete=models.SET_NULL, verbose_name='Relația dintre tălpile turnului')
    turn_numar_talpi = models.IntegerField(
        null=True, blank=True, verbose_name='Număr de tălpi')
    turn_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name="Observații")

    sarpanta_tip = ParentalManyToManyField(
        'nomenclatoare.TipSarpanta', blank=True, verbose_name='Tip')
    sarpanta_veche_nefolosita = models.BooleanField(
        default=False, verbose_name='Veche nefolosită sub șarpanta actuală')
    sarpanta_numar_turnulete = models.IntegerField(
        null=True, blank=True, verbose_name='Număr turnulețe decorative')
    sarpanta_numar_cruci = models.IntegerField(
        null=True, blank=True, verbose_name='Număr cruci')
    sarpanta_material_cruci = models.ForeignKey('nomenclatoare.MaterialCruci', null=True, blank=True,
                                                on_delete=models.SET_NULL, verbose_name='Material cruci', related_name="p_material_cruci")
    sarpanta_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    numar_accese_pridvor = models.IntegerField(
        null=True, blank=True, verbose_name='Număr accese pridvor')
    numar_accese_pridvor_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații Pridvor')
    numar_accese_pronaos = models.IntegerField(
        null=True, blank=True, verbose_name='Număr accese pronaos')
    numar_accese_pronaos_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații Pronaos')
    numar_accese_naos = models.IntegerField(
        null=True, blank=True, verbose_name='Număr accese naos')
    numar_accese_naos_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații Naos')
    numar_accese_altar = models.IntegerField(
        null=True, blank=True, verbose_name='Număr accese altar')
    numar_accese_altar_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații Altar')

    numar_ferestre_pridvor = models.IntegerField(
        null=True, blank=True, verbose_name='Număr ferestre pridvor')
    numar_ferestre_pridvor_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații Pridvor')
    numar_ferestre_pronaos = models.IntegerField(
        null=True, blank=True, verbose_name='Număr ferestre pronaos')
    numar_ferestre_pronaos_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații Pronaos')
    numar_ferestre_naos = models.IntegerField(
        null=True, blank=True, verbose_name='Număr ferestre naos')
    numar_ferestre_naos_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații Naos')
    numar_ferestre_altar = models.IntegerField(
        null=True, blank=True, verbose_name='Număr ferestre altar')
    numar_ferestre_altar_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații Altar')

    ochiesi_aerisitoare = models.BooleanField(
        default=False, verbose_name='Ochieși / Aerisitoare ')
    numar_ochiesi = models.IntegerField(default=0)
    ochiesi_aerisitoare_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    bolta_peste_pronaos = models.ForeignKey('nomenclatoare.TipBoltaPronaos', null=True, blank=True, on_delete=models.SET_NULL,
                                            verbose_name='Boltă peste pronaos', related_name='p_biserici_bolta_peste_pronaos')
    bolta_peste_pronaos_tipul_de_arc = ParentalManyToManyField(
        'nomenclatoare.TipArcBolta', blank=True, related_name='p_biserici_bolta_peste_pronaos')
    bolta_peste_pronaos_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')
    bolta_peste_pronaos_structura = ParentalManyToManyField(
        'nomenclatoare.MaterialeStructuraBolta', blank=True, verbose_name="Structură boltă pronaos", related_name='p_pronaos')

    bolta_peste_naos = models.ForeignKey('nomenclatoare.TipBoltaPronaos', null=True, blank=True,
                                         on_delete=models.SET_NULL, verbose_name='Boltă peste naos', related_name='p_biserici_bolta_peste_naos')
    bolta_peste_naos_tipul_de_arc = ParentalManyToManyField(
        'nomenclatoare.TipArcBolta', blank=True, related_name='p_biserici_bolta_peste_naos')
    bolta_peste_naos_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')
    bolta_peste_naos_structura = ParentalManyToManyField(
        'nomenclatoare.MaterialeStructuraBolta', blank=True, verbose_name="Structură boltă naos", related_name='p_naos')

    bolta_peste_altar = models.ForeignKey('nomenclatoare.BoltaPesteAltar', null=True, blank=True,
                                          on_delete=models.SET_NULL, verbose_name='Boltă peste altar', related_name='p_biserici_bolta_peste_altar')
    bolta_peste_altar_tip = models.ForeignKey('nomenclatoare.TipBoltaPesteAltar', null=True,
                                              blank=True, on_delete=models.SET_NULL, verbose_name='Tip', related_name='p_biserici')
    bolta_peste_altar_material = ParentalManyToManyField(
        'nomenclatoare.MaterialBolta', blank=True, related_name='p_biserici_bolta_peste_altar', verbose_name='Material')
    bolta_peste_altar_tipul_de_arc = ParentalManyToManyField(
        'nomenclatoare.TipArcBolta', blank=True, related_name='p_biserici_bolta_peste_altar', verbose_name='Tipul de arc')
    bolta_peste_altar_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')
    bolta_peste_altar_structura = ParentalManyToManyField(
        'nomenclatoare.MaterialeStructuraBolta', blank=True, verbose_name="Structură boltă altar", related_name='p_altar')
    cor = models.BooleanField(default=False)
    cor_material = ParentalManyToManyField(
        'nomenclatoare.MaterialCor', blank=True, related_name='p_biserici_cor')
    cor_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    solee = models.BooleanField(default=False)
    solee_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    masa_altar_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    turle_exista = models.BooleanField(default=False, verbose_name='Există')
    turle_numar = models.IntegerField(
        null=True, blank=True, verbose_name='Număr')
    turle_pozitionare = ParentalManyToManyField(
        'nomenclatoare.PozitionareTurle', blank=True, related_name='biserici', verbose_name='Poziționare')
    turle_numar_goluri = models.IntegerField(
        null=True, blank=True, verbose_name='Număr goluri')
    turle_stil = models.ForeignKey('nomenclatoare.StilTurle', null=True, blank=True,
                                             on_delete=models.SET_NULL, related_name='biserici', verbose_name='Stilul turlelor')
    turle_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    # Structura
    fundatia = models.ForeignKey('nomenclatoare.TipFundatie', null=True, blank=True,
                                 on_delete=models.SET_NULL, verbose_name='Structura fundației', related_name='p_biserici')
    fundatia_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    sistem_structural = models.ForeignKey('nomenclatoare.TipSistemStructural', null=True,
                                            blank=True, on_delete=models.SET_NULL, verbose_name='Tip', related_name='p_biserici')

    sistem_in_cheotoare = models.ForeignKey('nomenclatoare.TipStructuraCheotoare', null=True,
                                            blank=True, on_delete=models.SET_NULL, verbose_name='Tip', related_name='p_biserici')
    sistem_in_cheotoare_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')
    sistem_in_catei = models.ForeignKey('nomenclatoare.TipStructuraCatei', null=True,
                                        blank=True, on_delete=models.SET_NULL, verbose_name='Tip', related_name='p_biserici')
    sistem_in_catei_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')
    sistem_mixt = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    tiranti_numar = models.IntegerField(
        null=True, blank=True, verbose_name='Număr')
    tiranti_tip = models.ForeignKey('nomenclatoare.TipTiranti', null=True, blank=True,
                                    on_delete=models.SET_NULL, verbose_name='Tip Tiranți', related_name='p_biserici')
    tiranti_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    # Finisaje
    finisaj_exterior_tip = ParentalManyToManyField(
        'nomenclatoare.FinisajExterior', blank=True, verbose_name='Finisaj exterior corp')
    finisaj_exterior_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    # Finisaje - Învelitoare corp biserică

    invelitoare_corp_material = models.ForeignKey(
        'nomenclatoare.FinisajInvelitoare', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Material', related_name='invelitoare_corp')
    invelitoare_corp_sindrila_lungime = models.FloatField(
        null=True, blank=True, verbose_name='Șindrila (lungime)')
    invelitoare_corp_sindrila_latime_medie = models.FloatField(
        null=True, blank=True, verbose_name='Șindrila (lățime medie)')
    invelitoare_corp_sindrila_grosime_medie = models.FloatField(
        null=True, blank=True, verbose_name='Șindrila (grosime medie)')
    invelitoare_corp_sindrila_pasul_latuirii = models.FloatField(
        null=True, blank=True, verbose_name='Șindrila (pasul lățuirii)')
    invelitoare_corp_sindrila_pasul_baterii = models.FloatField(
        null=True, blank=True, verbose_name='Șindrila (pasul baterii)')
    invelitoare_corp_sindrila_numar_straturi = models.IntegerField(
        null=True, blank=True, verbose_name='Șindrila (număr straturi)')
    invelitoare_corp_sindrila_cu_horj = models.BooleanField(
        default=False, verbose_name='Șindrila cu horj')
    invelitoare_corp_sindrlia_tipul_de_batere = models.ForeignKey(
        'nomenclatoare.TipBatereSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (tipul de batere)', related_name='invelitoare_corp')
    invelitoare_corp_sindrlia_tipul_prindere = models.ForeignKey(
        'nomenclatoare.TipPrindereSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (tipul de prindere)', related_name='invelitoare_corp')
    invelitoare_corp_sindrlia_forma_botului = models.ForeignKey(
        'nomenclatoare.TipBotSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (forma botului)', related_name='invelitoare_corp')
    invelitoare_corp_sindrila_cu_tesitura = models.BooleanField(
        default=False, verbose_name='Șindrila cu teșitură')
    invelitoare_corp_sindrlia_prelucrare = models.ForeignKey(
        'nomenclatoare.TipPrelucrareSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (prelucrare)', related_name='invelitoare_corp')
    invelitoare_corp_sindrlia_esenta_lemnoasa = models.ForeignKey(
        'nomenclatoare.EsentaLemnoasa', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (esență lemnoasă)', related_name='invelitoare_corp_sindrlia_esenta')
    invelitoare_corp_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    # Finisaje -  Învelitoare turn

    invelitoare_turn_material = models.ForeignKey(
        'nomenclatoare.FinisajInvelitoare', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Material', related_name='invelitoare_turn')
    invelitoare_turn_sindrila_lungime = models.FloatField(
        null=True, blank=True, verbose_name='Șindrila (lungime)')
    invelitoare_turn_sindrila_latime_medie = models.FloatField(
        null=True, blank=True, verbose_name='Șindrila (lățime medie)')
    invelitoare_turn_sindrila_grosime_medie = models.FloatField(
        null=True, blank=True, verbose_name='Șindrila (grosime medie)')
    invelitoare_turn_sindrila_pasul_latuirii = models.FloatField(
        null=True, blank=True, verbose_name='Șindrila (pasul lățuirii)')
    invelitoare_turn_sindrila_pasul_baterii = models.FloatField(
        null=True, blank=True, verbose_name='Șindrila (pasul baterii)')
    invelitoare_turn_sindrila_numar_straturi = models.IntegerField(
        null=True, blank=True, verbose_name='Șindrila (număr straturi)')
    invelitoare_turn_sindrila_cu_horj = models.BooleanField(
        default=False, verbose_name='Șindrila cu horj')
    invelitoare_turn_sindrlia_tipul_de_batere = models.ForeignKey(
        'nomenclatoare.TipBatereSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (tipul de batere)', related_name='invelitoare_turn')
    invelitoare_turn_sindrlia_tipul_prindere = models.ForeignKey(
        'nomenclatoare.TipPrindereSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (tipul de prindere)', related_name='invelitoare_turn')
    invelitoare_turn_sindrlia_forma_botului = models.ForeignKey(
        'nomenclatoare.TipBotSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (forma botului)', related_name='invelitoare_turn')
    invelitoare_turn_sindrila_cu_tesitura = models.BooleanField(
        default=False, verbose_name='Șindrila cu teșitură')
    invelitoare_turn_sindrlia_prelucrare = models.ForeignKey(
        'nomenclatoare.TipPrelucrareSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (prelucrare)', related_name='invelitoare_turn')
    invelitoare_turn_sindrlia_esenta_lemnoasa = models.ForeignKey(
        'nomenclatoare.EsentaLemnoasa', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (esență lemnoasă)', related_name='invelitoare_turn_sindrlia_esenta')
    invelitoare_turn_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    # Finisaje -  Închidere tambur turn

    inchidere_tambur_turn_material = models.ForeignKey(
        'nomenclatoare.FinisajInvelitoare', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Material', related_name='inchidere_tambur')
    inchidere_tambur_turn_sindrila_lungime = models.FloatField(
        null=True, blank=True, verbose_name='Șindrila (lungime)')
    inchidere_tambur_turn_sindrila_latime_medie = models.FloatField(
        null=True, blank=True, verbose_name='Șindrila (lățime medie)')
    inchidere_tambur_turn_sindrila_grosime_medie = models.FloatField(
        null=True, blank=True, verbose_name='Șindrila (grosime medie)')
    inchidere_tambur_turn_sindrila_pasul_latuirii = models.FloatField(
        null=True, blank=True, verbose_name='Șindrila (pasul lățuirii)')
    inchidere_tambur_turn_sindrila_pasul_baterii = models.FloatField(
        null=True, blank=True, verbose_name='Șindrila (pasul baterii)')
    inchidere_tambur_turn_sindrila_numar_straturi = models.IntegerField(
        null=True, blank=True, verbose_name='Șindrila (număr straturi)')
    inchidere_tambur_turn_sindrila_cu_horj = models.BooleanField(
        default=False, verbose_name='Șindrila cu horj')
    inchidere_tambur_turn_sindrlia_tipul_de_batere = models.ForeignKey(
        'nomenclatoare.TipBatereSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (tipul de batere)', related_name='inchidere_tambur_turn')
    inchidere_tambur_turn_sindrlia_tipul_prindere = models.ForeignKey(
        'nomenclatoare.TipPrindereSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (tipul de prindere)', related_name='inchidere_tambur_turn')
    inchidere_tambur_turn_sindrlia_forma_botului = models.ForeignKey(
        'nomenclatoare.TipBotSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (forma botului)', related_name='inchidere_tambur_turn')
    inchidere_tambur_turn_sindrila_cu_tesitura = models.BooleanField(
        default=False, verbose_name='Șindrila cu teșitură')
    inchidere_tambur_turn_sindrlia_prelucrare = models.ForeignKey(
        'nomenclatoare.TipPrelucrareSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (prelucrare)', related_name='inchidere_tambur_turn')
    inchidere_tambur_turn_sindrlia_esenta_lemnoasa = models.ForeignKey(
        'nomenclatoare.EsentaLemnoasa', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (esență lemnoasă)', related_name='inchidere_tambur_turn_sindrlia_esenta')
    inchidere_tambur_turn_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    # Finisaje -  Învelitoare turle
    invelitoare_turle_material = ParentalManyToManyField(
        'nomenclatoare.FinisajInvelitoare', blank=True, verbose_name='Material')
    invelitoare_turle_sindrila_lungime = models.FloatField(
        null=True, blank=True, verbose_name='Șindrila (lungime)')
    invelitoare_turle_sindrila_latime_medie = models.FloatField(
        null=True, blank=True, verbose_name='Șindrila (lățime medie)')
    invelitoare_turle_sindrila_grosime_medie = models.FloatField(
        null=True, blank=True, verbose_name='Șindrila (grosime medie)')
    invelitoare_turle_sindrila_pasul_latuirii = models.FloatField(
        null=True, blank=True, verbose_name='Șindrila (pasul lățuirii)')
    invelitoare_turle_sindrila_pasul_baterii = models.FloatField(
        null=True, blank=True, verbose_name='Șindrila (pasul baterii)')
    invelitoare_turle_sindrila_numar_straturi = models.IntegerField(
        null=True, blank=True, verbose_name='Șindrila (număr straturi)')
    invelitoare_turle_sindrila_cu_horj = models.BooleanField(
        default=False, verbose_name='Șindrila cu horj')
    invelitoare_turle_sindrlia_tipul_de_batere = models.ForeignKey(
        'nomenclatoare.TipBatereSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (tipul de batere)', related_name='invelitoare_turle')
    invelitoare_turle_sindrlia_tipul_prindere = models.ForeignKey(
        'nomenclatoare.TipPrindereSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (tipul de prindere)', related_name='invelitoare_turle')
    invelitoare_turle_sindrlia_forma_botului = models.ForeignKey(
        'nomenclatoare.TipBotSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (forma botului)', related_name='invelitoare_turle')
    invelitoare_turle_sindrila_cu_tesitura = models.BooleanField(
        default=False, verbose_name='Șindrila cu teșitură')
    invelitoare_turle_sindrlia_prelucrare = models.ForeignKey(
        'nomenclatoare.TipPrelucrareSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (prelucrare)', related_name='invelitoare_turle')
    invelitoare_turle_sindrlia_esenta_lemnoasa = models.ForeignKey(
        'nomenclatoare.EsentaLemnoasa', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (esență lemnoasă)', related_name='invelitoare_turle_sindrlia_esenta')
    invelitoare_turle_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    # Interventii arhitecturale vizibile in timp

    invelitoare_actuala_an = models.IntegerField(
        null=True, blank=True, verbose_name='An montaj')
    invelitoare_actuala_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    interventii_invelitoare_etape_anterioare_vizibile = models.BooleanField(
        default=False, verbose_name='Vizibile')
    interventii_invelitoare_sindrila_pasul_latuirii = models.IntegerField(
        null=True, blank=True, verbose_name='Pasul lățuirii')
    interventii_invelitoare_sindrila_numar_straturi = models.IntegerField(
        null=True, blank=True, verbose_name='Număr straturi')
    interventii_invelitoare_sindrila_cu_horj = models.BooleanField(
        default=False, verbose_name='Cu horj')
    interventii_invelitoare_sindrlia_tipul_de_batere = models.ForeignKey(
        'nomenclatoare.TipBatereSindrila', null=True, blank=True, on_delete=models.SET_NULL,
        related_name='interventii_invelitoare', verbose_name='Tipul de batere')
    interventii_invelitoare_sindrlia_forma_botului = models.ForeignKey(
        'nomenclatoare.TipBotSindrila', null=True, blank=True, on_delete=models.SET_NULL,
        related_name='interventii_invelitoare', verbose_name='Forma botului')
    interventii_invelitoare_sindrila_cu_tesitura = models.BooleanField(
        default=False, verbose_name='Cu teșitură')
    interventii_invelitoare_sindrlia_esenta_lemnoasa = models.ForeignKey(
        'nomenclatoare.EsentaLemnoasa', null=True, blank=True, on_delete=models.SET_NULL,
        related_name='interventii_invelitoare', verbose_name='Esența lemnoasă')
    interventii_invelitoare_alte_tipuri_invelitoare = RichTextField(
        features=[], null=True, blank=True, verbose_name='Alte tipuri')
    interventii_invelitoare_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    # Modele 3d
    model_nori_de_puncte = models.TextField(null=True, blank=True)
    model_fotogrametrie = models.TextField(null=True, blank=True)


    # Invisible fields
    are_scanare_laser = models.BooleanField(default=False)
    are_model_fotogrametric = models.BooleanField(default=False)
    ansamblu_construit = ArrayField(
            models.CharField(max_length=100, blank=True),
            size=20,
            null=True,
            blank=True
        )
    numar_clopote = models.IntegerField(default=0)

    api_fields = [
        APIField('amplasament'),
        APIField('poze_amplasament'),
    ]
    localizare_panels = [
        MultiFieldPanel([
            FieldPanel("amplasament"),
            InlinePanel("poze_amplasament", label="Poză")
        ],
            heading='amplasament',
            classname='collapsible collapsed'
        ),
        MultiFieldPanel([
            FieldPanel("topografie"), ],
            heading='topografie',
            classname='collapsible collapsed'
        ),
        MultiFieldPanel([
            FieldPanel("toponim"),
            FieldPanel("toponim_sursa"), 
            ],
            heading='toponim',
            classname='collapsible collapsed'
        ),
        
        MultiFieldPanel([
            FieldPanel("relatia_cu_cimitirul"), ],
            heading='relatia cu cimitirul',
            classname='collapsible collapsed'
        ),
        MultiFieldPanel([
            FieldPanel("peisagistica_sitului",
                       widget=forms.CheckboxSelectMultiple),
            InlinePanel("poze_peisagistica_sitului", label="Poză")
        ],
            heading='peisagistica sitului',
            classname='collapsible collapsed'
        ),
        MultiFieldPanel([
            FieldPanel("observatii"), ],
            heading='observatii',
            classname='collapsible collapsed'
        ),
    ]

    ansamblu_panels = [
        InlinePanel('elemente_ansamblu_construit',
                    label="element arhitectural", classname="collapsible collapsed "),
        InlinePanel('elemente_importante_ansamblu_construit',
                    label="Alte componente importante ale sitului "),
    ]

    arhitectura_panels = [
        MultiFieldPanel([
            FieldPanel('materiale'),
            FieldPanel('detalii_materiale'),
        ],
            heading="Materiale",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel([
            ImageChooserPanel('planimetria_bisericii', ['planimetrii']),
        ],
            heading="Planimetria bisericii",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('numar_accese_pridvor'),
                FieldPanel('numar_accese_pridvor_observatii'),
                FieldPanel('numar_accese_pronaos'),
                FieldPanel('numar_accese_pronaos_observatii'),
                FieldPanel('numar_accese_naos'),
                FieldPanel('numar_accese_naos_observatii'),
                FieldPanel('numar_accese_altar'),
                FieldPanel('numar_accese_altar_observatii'),
                MultiFieldPanel(
                    [
                        InlinePanel('poze_accese', label='Poza')
                    ]
                )
            ],
            heading="Număr accese",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('numar_ferestre_pridvor'),
                FieldPanel('numar_ferestre_pridvor_observatii'),
                FieldPanel('numar_ferestre_pronaos'),
                FieldPanel('numar_ferestre_pronaos_observatii'),
                FieldPanel('numar_ferestre_naos'),
                FieldPanel('numar_ferestre_naos_observatii'),
                FieldPanel('numar_ferestre_altar'),
                FieldPanel('numar_ferestre_altar_observatii'),
                MultiFieldPanel(
                    [
                        InlinePanel('poze_ferestre', label='Poza')
                    ]
                )
            ],
            heading="Număr ferestre",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('ochiesi_aerisitoare'),
                FieldPanel('numar_ochiesi'),
                FieldPanel('ochiesi_aerisitoare_observatii'),
                MultiFieldPanel(
                    [
                        InlinePanel('poze_ochiesi', label='Poza')
                    ]
                )
            ],
            heading="Ochieși / Aerisitoare",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('solee'),
                FieldPanel('solee_observatii'),
                MultiFieldPanel(
                    [
                        InlinePanel('poze_solee', label='Poza')
                    ]
                )
            ],
            heading="Solee",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('masa_altar_observatii'),
                MultiFieldPanel(
                    [
                        InlinePanel('poze_masa_atlar', label='Poza')
                    ]
                )
            ],
            heading="Masă altar",
            classname="collapsible collapsed ",
        ),

        MultiFieldPanel(
            [
                FieldPanel('bolta_peste_pronaos'),
                FieldPanel('bolta_peste_pronaos_structura',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('bolta_peste_pronaos_tipul_de_arc',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('bolta_peste_pronaos_observatii'),
                FieldPanel('bolta_peste_naos'),
                FieldPanel('bolta_peste_naos_structura',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('bolta_peste_naos_tipul_de_arc',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('bolta_peste_naos_observatii'),
                FieldPanel('bolta_peste_altar'),
                FieldPanel('bolta_peste_altar_tip'),
                FieldPanel('bolta_peste_altar_material',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('bolta_peste_altar_structura',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('bolta_peste_altar_tipul_de_arc',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('bolta_peste_altar_observatii'),
                InlinePanel('poze_bolti', label='Poza')
            ],
            heading="Bolți",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('cor'),
                FieldPanel('cor_material',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('cor_observatii'),
                MultiFieldPanel(
                    [
                        InlinePanel('poze_cor', label='Poza')
                    ]
                )
            ],
            heading="Cor",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('sarpanta_tip',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('sarpanta_veche_nefolosita'),
                FieldPanel('sarpanta_numar_turnulete'),
                FieldPanel('sarpanta_numar_cruci'),
                FieldPanel('sarpanta_material_cruci'),
                FieldPanel('sarpanta_observatii'),
                MultiFieldPanel(
                    [
                        InlinePanel('poze_sarpanta', label='Poza')
                    ]
                )
            ],
            heading="Șarpanta corp",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('turn_dimensiune'),
                FieldPanel('turn_tip'),
                FieldPanel('turn_numar'),
                FieldPanel('turn_numar_stalpi'),
                FieldPanel('turn_plan'),
                FieldPanel('turn_amplasare'),
                FieldPanel('turn_galerie'),
                FieldPanel('turn_numar_arcade'),
                FieldPanel('turn_numar_arcade_observatii'),
                FieldPanel('turn_asezare_talpi'),
                FieldPanel('turn_relatie_talpi'),
                FieldPanel('turn_numar_talpi'),
                FieldPanel('turn_observatii'),
                MultiFieldPanel(
                    [
                        InlinePanel('poze_turn', label='Poza')
                    ]
                )
            ],
            heading="Turn",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                InlinePanel('clopote', label='Clopote'),
                MultiFieldPanel(
                    [
                        InlinePanel('poze_clopote', label='Poza')
                    ]
                )
            ],
            heading="Clopote",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('turle_exista'),
                FieldPanel('turle_numar'),
                FieldPanel('turle_pozitionare',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('turle_numar_goluri'),
                FieldPanel('turle_stil'),
                FieldPanel('turle_observatii'),


                MultiFieldPanel(
                    [
                        InlinePanel('poze_turle', label='Poza')
                    ]
                )
            ],
            heading="Turle",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                InlinePanel('poze_generale_exterior', label='Poza')
            ],
            heading="Poze Generale Exterior",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                InlinePanel('poze_generale_interior', label='Poza')
            ],
            heading="Poze Generale Interior",
            classname="collapsible collapsed ",
        ),
    ]

    structura_panels = [
        MultiFieldPanel(
            [
                FieldPanel('fundatia'),
                FieldPanel('fundatia_observatii'),
                InlinePanel("poze_fundatie", label="Poză")
            ],
            heading="FUNDAȚIA",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('sistem_structural'),
            ],
            heading="SISTEM STRUCTURAL AL CORPULUI BISERICII",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('sistem_in_cheotoare'),
                FieldPanel('sistem_in_cheotoare_observatii'),
                InlinePanel("poze_structura_cheotoare", label="Poză")
            ],
            heading="SISTEM STRUCTURAL AL CORPULUI BISERICII ÎN CHEOTOARE",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('sistem_in_catei'),
                FieldPanel('sistem_in_catei_observatii'),
                InlinePanel("poze_structura_catei", label="Poză")
            ],
            heading="SISTEM STRUCTURAL AL CORPULUI BISERICII ÎN CĂȚEI",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('sistem_mixt'),
                InlinePanel("poze_structura_mixt", label="Poză")
            ],
            heading="SISTEM STRUCTURAL AL CORPULUI BISERICII MIXT",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('tiranti_numar'),
                FieldPanel('tiranti_tip'),
                FieldPanel('tiranti_observatii'),
                InlinePanel("poze_tiranti", label="Poză")
            ],
            heading="Tiranți",
            classname="collapsible collapsed ",
        ),
    ]

    finisaje_panels = [
        MultiFieldPanel(
            [
                FieldPanel('finisaj_exterior_tip',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('finisaj_exterior_observatii'),
                InlinePanel('poze_exterior_corp', label='Poză'),
            ],
            heading="Exterior corp biserică",
            classname="collapsible collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('invelitoare_corp_material'),
                FieldPanel('invelitoare_corp_sindrila_lungime'),
                FieldPanel('invelitoare_corp_sindrila_latime_medie'),
                FieldPanel('invelitoare_corp_sindrila_grosime_medie'),
                FieldPanel('invelitoare_corp_sindrila_pasul_latuirii'),
                FieldPanel('invelitoare_corp_sindrila_pasul_baterii'),
                FieldPanel('invelitoare_corp_sindrila_numar_straturi'),
                FieldPanel('invelitoare_corp_sindrila_cu_horj'),
                FieldPanel('invelitoare_corp_sindrlia_tipul_de_batere'),
                FieldPanel('invelitoare_corp_sindrlia_tipul_prindere'),
                FieldPanel('invelitoare_corp_sindrlia_forma_botului'),
                FieldPanel('invelitoare_corp_sindrila_cu_tesitura'),
                FieldPanel('invelitoare_corp_sindrlia_prelucrare'),
                FieldPanel('invelitoare_corp_sindrlia_esenta_lemnoasa'),
                FieldPanel('invelitoare_corp_observatii'),
                InlinePanel('poze_invelitoare', label='Poză'),
            ],
            heading="Învelitoare corp biserică",
            classname="collapsible  collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('invelitoare_turn_material'),
                FieldPanel('invelitoare_turn_sindrila_lungime'),
                FieldPanel('invelitoare_turn_sindrila_latime_medie'),
                FieldPanel('invelitoare_turn_sindrila_grosime_medie'),
                FieldPanel('invelitoare_turn_sindrila_pasul_latuirii'),
                FieldPanel('invelitoare_turn_sindrila_pasul_baterii'),
                FieldPanel('invelitoare_turn_sindrila_numar_straturi'),
                FieldPanel('invelitoare_turn_sindrila_cu_horj'),
                FieldPanel('invelitoare_turn_sindrlia_tipul_de_batere'),
                FieldPanel('invelitoare_turn_sindrlia_tipul_prindere'),
                FieldPanel('invelitoare_turn_sindrlia_forma_botului'),
                FieldPanel('invelitoare_turn_sindrila_cu_tesitura'),
                FieldPanel('invelitoare_turn_sindrlia_prelucrare'),
                FieldPanel('invelitoare_turn_sindrlia_esenta_lemnoasa'),
                FieldPanel('invelitoare_turn_observatii'),
                InlinePanel('poze_invelitoare_turn', label='Poză'),
            ],
            heading="Învelitoare turn",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('inchidere_tambur_turn_material'),
                FieldPanel('inchidere_tambur_turn_sindrila_lungime'),
                FieldPanel('inchidere_tambur_turn_sindrila_latime_medie'),
                FieldPanel('inchidere_tambur_turn_sindrila_grosime_medie'),
                FieldPanel('inchidere_tambur_turn_sindrila_pasul_latuirii'),
                FieldPanel('inchidere_tambur_turn_sindrila_pasul_baterii'),
                FieldPanel('inchidere_tambur_turn_sindrila_numar_straturi'),
                FieldPanel('inchidere_tambur_turn_sindrila_cu_horj'),
                FieldPanel('inchidere_tambur_turn_sindrlia_tipul_de_batere'),
                FieldPanel('inchidere_tambur_turn_sindrlia_tipul_prindere'),
                FieldPanel('inchidere_tambur_turn_sindrlia_forma_botului'),
                FieldPanel('inchidere_tambur_turn_sindrila_cu_tesitura'),
                FieldPanel('inchidere_tambur_turn_sindrlia_prelucrare'),
                FieldPanel('inchidere_tambur_turn_sindrlia_esenta_lemnoasa'),
                FieldPanel('inchidere_tambur_turn_observatii'),
                InlinePanel('poze_inchidere_tambur', label='Poză'),
            ],
            heading="Închidere tambur turn",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('invelitoare_turle_material',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('invelitoare_turle_sindrila_lungime'),
                FieldPanel('invelitoare_turle_sindrila_latime_medie'),
                FieldPanel('invelitoare_turle_sindrila_grosime_medie'),
                FieldPanel('invelitoare_turle_sindrila_pasul_latuirii'),
                FieldPanel('invelitoare_turle_sindrila_pasul_baterii'),
                FieldPanel('invelitoare_turle_sindrila_numar_straturi'),
                FieldPanel('invelitoare_turle_sindrila_cu_horj'),
                FieldPanel('invelitoare_turle_sindrlia_tipul_de_batere'),
                FieldPanel('invelitoare_turle_sindrlia_tipul_prindere'),
                FieldPanel('invelitoare_turle_sindrlia_forma_botului'),
                FieldPanel('invelitoare_turle_sindrila_cu_tesitura'),
                FieldPanel('invelitoare_turle_sindrlia_prelucrare'),
                FieldPanel('invelitoare_turle_sindrlia_esenta_lemnoasa'),
                FieldPanel('invelitoare_turle_observatii'),
                InlinePanel('poze_invelitoare_turle', label='Poză'),
            ],
            heading="Învelitoare turle",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                InlinePanel('finisaje_portic')
            ],
            heading="Finisaje Portic",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                InlinePanel('finisaje_pronaos')
            ],
            heading="Finisaje pronaos",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                InlinePanel('finisaje_naos')
            ],
            heading="Finisaje naos",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                InlinePanel('finisaje_altar', label="Element altar")
            ],
            heading="Finisaje altar",
            classname="collapsible collapsed ",
        ),


    ]

    interventii_panels = [
        MultiFieldPanel(
            [
                FieldPanel('invelitoare_actuala_an'),
                FieldPanel('invelitoare_actuala_observatii'),
            ],
            heading="Învelitoare actuală de lemn",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel(
                    'interventii_invelitoare_etape_anterioare_vizibile'),
                FieldPanel('interventii_invelitoare_sindrila_pasul_latuirii'),
                FieldPanel('interventii_invelitoare_sindrila_numar_straturi'),
                FieldPanel('interventii_invelitoare_sindrila_cu_horj'),
                FieldPanel('interventii_invelitoare_sindrlia_tipul_de_batere'),
                FieldPanel('interventii_invelitoare_sindrlia_forma_botului'),
                FieldPanel('interventii_invelitoare_sindrila_cu_tesitura'),
                FieldPanel('interventii_invelitoare_sindrlia_esenta_lemnoasa'),
                FieldPanel('interventii_invelitoare_alte_tipuri_invelitoare'),
                FieldPanel('interventii_invelitoare_observatii'),
                InlinePanel('poze_interventii_invelitoare', label="Poză")
            ],
            heading="Etape anterioare vizibile ale învelitorii",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                InlinePanel('etape_istorice_vizibile', label="Etapă")
            ],
            heading="Alte etape istorice vizibile",
            classname="collapsible collapsed ",
        ),

    ]

    modele_3d_panels = [
        FieldPanel('model_nori_de_puncte'),
        FieldPanel('model_fotogrametrie')

    ]
    edit_handler = TabbedInterface(
        [
            ObjectList(localizare_panels, heading='Localizare/peisaj'),
            ObjectList(ansamblu_panels, heading='Ansamblu construit'),
            ObjectList(arhitectura_panels, heading='Arhitectura bisericii'),
            ObjectList(structura_panels, heading='Structura'),
            ObjectList(finisaje_panels, heading='Finisaje'),
            ObjectList(interventii_panels,
                       heading='Intervenții arhitecturale vizibile în timp'),
            ObjectList(modele_3d_panels, heading='Modele 3d')
        ]
    )

    class Meta:  # noqa

        verbose_name = "Capitol Descriere"
        verbose_name_plural = "Capitole Descriere"

    @classmethod
    def get_image_collection(cls):
        print(cls)
        # any logic here to determine what collection to filter by
        return 2



    def save(self, *args, **kwargs):

        self.are_scanare_laser = False
        self.are_model_fotogrametric = False

        self.ansamblu_construit = [x.element.nume for x in self.elemente_ansamblu_construit.all()]
        self.numar_clopote = len(self.clopote.all())

        return super().save(*args, **kwargs)




class Persoana(models.Model):
    nume = models.CharField(max_length=250)
    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')
    sursa = RichTextField(features=[], null=True,
                          blank=True, verbose_name='Sursa')

    panels = [
        FieldPanel('nume'),
        FieldPanel('observatii'),
        FieldPanel('sursa'),
    ]

    class Meta:
        abstract = True

    def __str__(self):
        return self.nume


class PozeCtitori(Orderable):
    page = ParentalKey('Ctitori',
                       on_delete=models.CASCADE, related_name='poze')
    poza = models.ForeignKey('wagtailimages.Image', null=True,
                             blank=True, on_delete=models.SET_NULL, related_name='+')
    rendition = models.JSONField(null=True, blank=True)
    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        ImageChooserPanel('poza'),
        FieldPanel('observatii'),
    ]

class Ctitori(ClusterableModel, Orderable, Persoana):
    page = ParentalKey(
        'IstoricPage', on_delete=models.PROTECT, related_name='ctitori')

    panels = Persoana.panels + [
        InlinePanel('poze', label='Poză')
    ]

class PozeMesteri(Orderable):
    page = ParentalKey('Mesteri',
                       on_delete=models.CASCADE, related_name='poze')
    poza = models.ForeignKey('wagtailimages.Image', null=True,
                             blank=True, on_delete=models.SET_NULL, related_name='+')
    rendition = models.JSONField(null=True, blank=True)
    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        ImageChooserPanel('poza'),
        FieldPanel('observatii'),
    ]

class Mesteri(ClusterableModel, Orderable, Persoana):
    page = ParentalKey(
        'IstoricPage', on_delete=models.PROTECT, related_name='mesteri')

    panels = Persoana.panels + [
        InlinePanel('poze', label='Poză')
    ]

class PozeZugravi(Orderable):
    page = ParentalKey('Zugravi',
                       on_delete=models.CASCADE, related_name='poze')
    poza = models.ForeignKey('wagtailimages.Image', null=True,
                             blank=True, on_delete=models.SET_NULL, related_name='+')
    rendition = models.JSONField(null=True, blank=True)
    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        ImageChooserPanel('poza'),
        FieldPanel('observatii'),
    ]

class Zugravi(ClusterableModel, Orderable, Persoana):
    page = ParentalKey(
        'IstoricPage', on_delete=models.PROTECT, related_name='zugravi')

    panels = Persoana.panels + [
        InlinePanel('poze', label='Poză')
    ]

class PozePersonalitati(Orderable):
    page = ParentalKey('Personalitati',
                       on_delete=models.CASCADE, related_name='poze')
    poza = models.ForeignKey('wagtailimages.Image', null=True,
                             blank=True, on_delete=models.SET_NULL, related_name='+')
    rendition = models.JSONField(null=True, blank=True)
    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        ImageChooserPanel('poza'),
        FieldPanel('observatii'),
    ]

class Personalitati(ClusterableModel, Orderable, Persoana):
    page = ParentalKey('IstoricPage', on_delete=models.PROTECT,
                       related_name='personalitati')

    panels = Persoana.panels + [
        InlinePanel('poze', label='Poză')
    ]

class Eveniment(models.Model):
    nume = models.CharField(max_length=250)
    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        FieldPanel('nume'),
        FieldPanel('observatii'),
    ]

    class Meta:
        abstract = True

    def __str__(self):
        return self.nume


class Evenimente(Orderable, Eveniment):
    page = ParentalKey('IstoricPage', on_delete=models.CASCADE,
                       related_name='evenimente')


class MutareBiserica(models.Model):
    localitate = models.ForeignKey('nomenclatoare.Localitate', null=True,
                                   blank=True, on_delete=models.SET_NULL, related_name='p_biserici_mutari')
    adresa = models.CharField(max_length=250, null=True, blank=True)
    latitudine = models.FloatField(null=True, blank=True)
    longitudine = models.FloatField(null=True, blank=True)

    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')
    sursa = RichTextField(features=[], null=True,
                          blank=True, verbose_name='Sursa')

    panels = [
        SnippetChooserPanel('localitate'),
        FieldPanel('adresa'),
        FieldPanel('latitudine'),
        FieldPanel('longitudine'),
        FieldPanel('observatii'),
        FieldPanel('sursa'),
    ]

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.localitate)


class MutariBiserica(Orderable, MutareBiserica):
    page = ParentalKey(
        'IstoricPage', on_delete=models.CASCADE, related_name='mutari')


class PovesteBiserica(models.Model):
    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')
    sursa = RichTextField(features=[], null=True,
                          blank=True, verbose_name='Sursa')

    panels = [
        FieldPanel('observatii'),
        FieldPanel('sursa'),
    ]

    class Meta:
        abstract = True

    def __str__(self):
        return self.sursa

class PovestiBiserica(Orderable, PovesteBiserica):
    page = ParentalKey(
        'IstoricPage', on_delete=models.CASCADE, related_name='povesti')



class PozePisanie(Orderable, Poza):
        page = ParentalKey(
            'IstoricPage', on_delete=models.CASCADE, related_name='poze_pisanie')



class IstoricPage(Page):
    sursa_datare = ParentalManyToManyField(
        'nomenclatoare.SursaDatare', related_name='p_biserici', blank=True)
    an_constructie = models.IntegerField(null=True, blank=True)
    datare_prin_interval_timp = models.CharField(
        max_length=50, null=True, blank=True)
    datare_secol = models.ForeignKey('nomenclatoare.Secol', null=True,
                                     blank=True, on_delete=models.SET_NULL, related_name='p_biserici')
    datare_secol_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')
    datare_secol_sursa = RichTextField(
        features=[], null=True, blank=True, verbose_name='Sursa')

    studiu_dendocronologic_fisier = models.ForeignKey(
        'wagtaildocs.Document', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Fișier')
    studiu_dendocronologic_autor = models.CharField(
        max_length=150, null=True, blank=True, verbose_name='Autor')
    studiu_dendocronologic_an = models.IntegerField(
        null=True, blank=True, verbose_name='An')
    studiu_dendocronologic_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    pisanie_traducere = RichTextField(
        features=[], null=True, blank=True, verbose_name='Traducere')
    pisanie_secol_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')
    pisanie_secol_sursa = RichTextField(
        features=[], null=True, blank=True, verbose_name='Sursa')

    are_pisanie = models.BooleanField(default=False, verbose_name='Pisanie')
    are_studiu_dendro = models.BooleanField(default=False, verbose_name='Studiu Dendrocronologic')
    are_mutari = models.BooleanField(default=False, verbose_name='Mutări')
    lista_ctitori = ArrayField(
            models.CharField(max_length=100, blank=True),
            size=20,
            null=True,
            blank=True,
            verbose_name='Ctitori'
        )
    lista_mesteri = ArrayField(
            models.CharField(max_length=100, blank=True),
            size=20,
            null=True,
            blank=True,
            verbose_name='Meșteri'
        )
    lista_zugravi = ArrayField(
            models.CharField(max_length=100, blank=True),
            size=20,
            null=True,
            blank=True,
            verbose_name='Zugravi'
        )
    lista_personalitati = ArrayField(
            models.CharField(max_length=100, blank=True),
            size=20,
            null=True,
            blank=True,
            verbose_name='Personalități'
        )
    istoric_panels = [
        MultiFieldPanel([
            FieldPanel('sursa_datare', widget=forms.CheckboxSelectMultiple),
            FieldPanel('an_constructie'),
            FieldPanel('datare_prin_interval_timp'),
            FieldPanel('datare_secol'),
            FieldPanel('datare_secol_observatii'),
            FieldPanel('datare_secol_sursa'),
        ],
            heading="Datare",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel([
            DocumentChooserPanel('studiu_dendocronologic_fisier'),
            FieldPanel('studiu_dendocronologic_autor'),
            FieldPanel('studiu_dendocronologic_an'),
            FieldPanel('studiu_dendocronologic_observatii')
        ],
            heading="Studiu dendrocronologic",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel([
            FieldPanel('pisanie_traducere'),
            FieldPanel('pisanie_secol_observatii'),
            FieldPanel('pisanie_secol_sursa'),
            InlinePanel("poze_pisanie", label="Poză")
        ],
            heading="Pisanie",
            classname="collapsible collapsed ",
        ),
    ]

    ctitori_panels = [
        InlinePanel('ctitori', label='ctitori')
    ]

    mesteri_panels = [
        InlinePanel('mesteri', label='mesteri')
    ]

    zugravi_panels = [
        InlinePanel('zugravi', label='zugravi')
    ]

    personalitati_panels = [
        InlinePanel('personalitati', label='personalitati')
    ]

    evenimente_panels = [
        InlinePanel('evenimente', label='evenimente')
    ]

    mutari_panels = [
        InlinePanel('mutari', label='mutari')
    ]

    povesti_panels = [
        InlinePanel('povesti', label='povesti')
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(istoric_panels, heading='Istoric'),
            ObjectList(ctitori_panels, heading='Ctitori'),
            ObjectList(mesteri_panels, heading='Mesteri'),
            ObjectList(zugravi_panels, heading='Zugravi'),
            ObjectList(personalitati_panels, heading='Personalitati'),
            ObjectList(evenimente_panels, heading='Evenimente'),
            ObjectList(mutari_panels, heading='Mutari'),
            ObjectList(povesti_panels, heading='Povesti'),
        ])

    class Meta:  # noqa

        verbose_name = "Istoric"
        verbose_name_plural = "Istoric"


    def save(self, *args, **kwargs):

        biserica = self.get_parent().specific
        biserica.datare_secol = self.datare_secol
        biserica.datare_prin_interval_timp = self.datare_prin_interval_timp
        biserica.datare_an = self.an_constructie
        biserica.save_revision()




        self.are_pisanie = True if self.pisanie_traducere else False
        self.are_studiu_dendro = True if self.studiu_dendocronologic_fisier else False
        self.are_mutari = True if self.mutari.all() else False
        self.lista_ctitori = [x.nume for x in self.ctitori.all()]
        self.lista_mesteri = [x.nume for x in self.mesteri.all()]
        self.lista_zugravi = [x.nume for x in self.zugravi.all()]
        self.lista_personalitati = [x.nume for x in self.personalitati.all()]
        return super().save(*args, **kwargs)



class ValoarePage(Page):
    vechime = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True,
                                  help_text="Printr-un algorim definit se va da automat o notă de la 1-5 în funcție de vechimea monumentului si a picturii descrise conform OMCC2682/2003 ETC", verbose_name='Clasa')
    vechime_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    integritate = models.IntegerField(choices=CLASE_EVALUARE, null=True,
                                      blank=True, help_text="Integritate / Autenticitate", verbose_name='Clasa')
    integritate_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    unicitate = models.IntegerField(choices=CLASE_EVALUARE, null=True,
                                    blank=True, help_text="Unicitate / raritate", verbose_name='Clasa')
    unicitate_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    valoare_memoriala = models.IntegerField(
        choices=CLASE_EVALUARE, null=True, blank=True, help_text="evenimente, personalități", verbose_name='Clasa')
    valoare_memoriala_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    peisaj_cultural = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True,
                                          help_text="Parte definitorie a peisajului cultural al zonei", verbose_name='Clasa')
    peisaj_cultural_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    valoare_sit = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True,
                                      help_text="Valoarea sitului împreună cu toate componentele ansamblului din care face parte, ținând cont de integritate, autenticitate, estetică peisageră, biodiversitate, etc. SUBIECTIV", verbose_name='Clasa')
    valoare_sit_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    estetica = models.IntegerField(choices=CLASE_EVALUARE, null=True,
                                   blank=True, help_text="Estetică / Arhitectură", verbose_name='Clasa')
    estetica_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    mestesug = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True,
                                   help_text="Meșteșug (calitatea muncii -  a se vedea golurile dintre lemne (dintre bârne în general dar în special la așezarea elementelor orizontale peste cele verticale))", verbose_name='Clasa')
    mestesug_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    pictura = models.IntegerField(
        choices=CLASE_EVALUARE, null=True, blank=True, verbose_name='Clasa')
    pictura_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    folosinta_actuala = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True,
                                            help_text="Folosință actuală / singura biserică din sat / loc al patrimoniului imaterial", verbose_name='Clasa')
    folosinta_actuala_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    relevanta_actuala = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True,
                                            help_text="Relevanța actuală pentru comunitatea locală (prin reprezentanții săi: preot, crâsnic, învățător, familii de bază)", verbose_name='Clasa')
    relevanta_actuala_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    potential = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True,
                                    help_text="Potențialul de beneficii aduse comunității locale", verbose_name='Clasa')
    potential_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    valoare_panels = [
        MultiFieldPanel(
            [
                FieldPanel('vechime'),
                FieldPanel('vechime_observatii'),
            ],
            heading="Vechime",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('integritate'),
                FieldPanel('integritate_observatii'),
            ],
            heading="Integritate / Autenticitate",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('unicitate'),
                FieldPanel('unicitate_observatii'),
            ],
            heading="Unicitate",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('valoare_memoriala'),
                FieldPanel('valoare_memoriala_observatii'),
            ],
            heading="Valoare memorială",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('peisaj_cultural'),
                FieldPanel('peisaj_cultural_observatii'),
            ],
            heading="Valoarea peisajului cultural",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('valoare_sit'),
                FieldPanel('valoare_sit_observatii'),
            ],
            heading="Valoarea sitului",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('estetica'),
                FieldPanel('estetica_observatii'),
            ],
            heading="Valoarea estetică",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('mestesug'),
                FieldPanel('mestesug_observatii'),
            ],
            heading="Valoarea meșteșugului",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('pictura'),
                FieldPanel('pictura_observatii'),
            ],
            heading="Valoarea componentei artistice",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('folosinta_actuala'),
                FieldPanel('folosinta_actuala_observatii'),
            ],
            heading="Folosința actuală",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('relevanta_actuala'),
                FieldPanel('relevanta_actuala_observatii'),
            ],
            heading="Relevanța actuală pentru comunitate",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('potential'),
                FieldPanel('potential_observatii'),
            ],
            heading="Potențial",
            classname="collapsible collapsed ",
        ),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(valoare_panels, heading='General'),
        ])

    class Meta:  # noqa

        verbose_name = "Valoare"
        verbose_name_plural = "Valoare"



    def save(self, *args, **kwargs):
        nota_valoare = 0
        active_fields = 0

        fields = [
            "vechime",
            "integritate",
            "unicitate",
            "valoare_memoriala",
            "peisaj_cultural",
            "valoare_sit",
            "estetica",
            "mestesug",
            "pictura",
            "folosinta_actuala",
            "relevanta_actuala",
            "potential",
        ]

        important_fields = [
            "vechime",
            "integritate",
            "unicitate",
            "folosinta_actuala",
            "relevanta_actuala",
            "potential",
        ]

        for field in fields:
            field_value = getattr(self, field)
            if field_value:
                if field in important_fields:
                    nota_valoare += 2 * field_value
                    active_fields += 2
                else:
                    nota_valoare += field_value
                    active_fields += 1

        if active_fields:
            nota_valoare = nota_valoare / active_fields
        
        biserica = self.get_parent().specific
        biserica.valoare = nota_valoare

        if biserica.conservare:
            biserica.prioritizare = biserica.valoare * biserica.conservare
        biserica.save_revision()

        return super().save(*args, **kwargs)



    class PozeSit(Orderable, Poza):
        page = ParentalKey(
            'ConservarePage', on_delete=models.CASCADE, related_name='poze_sit')

    class PozeElementeArhitecturale(Orderable, Poza):
        page = ParentalKey('ConservarePage', on_delete=models.CASCADE,
                           related_name='poze_elemente_arhitecturale')

    class PozeAlteElementeImportante(Orderable, Poza):
        page = ParentalKey('ConservarePage', on_delete=models.CASCADE,
                           related_name='poze_alte_elemente_importante')

    class PozeVegetatie(Orderable, Poza):
        page = ParentalKey(
            'ConservarePage', on_delete=models.CASCADE, related_name='poze_vegetatie')

    class PozeTeren(Orderable, Poza):
        page = ParentalKey(
            'ConservarePage', on_delete=models.CASCADE, related_name='poze_teren')

    class PozeFundatii(Orderable, Poza):
        page = ParentalKey(
            'ConservarePage', on_delete=models.CASCADE, related_name='poze_fundatii')

    class PozeTalpi(Orderable, Poza):
        page = ParentalKey(
            'ConservarePage', on_delete=models.CASCADE, related_name='poze_talpi')

    class PozeCorpBiserica(Orderable, Poza):
        page = ParentalKey(
            'ConservarePage', on_delete=models.CASCADE, related_name='poze_corp_biserica')

    class PozeBolti(Orderable, Poza):
        page = ParentalKey(
            'ConservarePage', on_delete=models.CASCADE, related_name='poze_bolti')

    class PozeCosoroabe(Orderable, Poza):
        page = ParentalKey(
            'ConservarePage', on_delete=models.CASCADE, related_name='poze_cosoroabe')

    class PozeSarpantaCorpBiserica(Orderable, Poza):
        page = ParentalKey('ConservarePage', on_delete=models.CASCADE,
                           related_name='poze_sarpanta_corp_biserica')

    class PozeTurnConservare(Orderable, Poza):
        page = ParentalKey(
            'ConservarePage', on_delete=models.CASCADE, related_name='poze_turn')

    class PozeZonaDinJurulBiserici(Orderable, Poza):
        page = ParentalKey('ConservarePage', on_delete=models.CASCADE,
                           related_name='poze_zona_din_jurul_biserici')

    class PozePardoseliInterioare(Orderable, Poza):
        page = ParentalKey('ConservarePage', on_delete=models.CASCADE,
                           related_name='poze_pardoseli_interioare')

    class PozeFinisajExterior(Orderable, Poza):
        page = ParentalKey('ConservarePage', on_delete=models.CASCADE,
                           related_name='poze_finisaj_exterior')

    class PozeFinisajPeretiInteriori(Orderable, Poza):
        page = ParentalKey('ConservarePage', on_delete=models.CASCADE,
                           related_name='poze_finisaj_pereti_interiori')

    class PozeFinisajTavaneSiBolti(Orderable, Poza):
        page = ParentalKey('ConservarePage', on_delete=models.CASCADE,
                           related_name='poze_finisaj_tavane_si_bolti')

    class PozeTamplarii(Orderable, Poza):
        page = ParentalKey(
            'ConservarePage', on_delete=models.CASCADE, related_name='poze_tamplarii')

    class PozeInvelitoareSarpantaSiTurn(Orderable, Poza):
        page = ParentalKey('ConservarePage', on_delete=models.CASCADE,
                           related_name='poze_invelitoare_sarpanta_si_turn')

    class PozeInstalatieElectrica(Orderable, Poza):
        page = ParentalKey('ConservarePage', on_delete=models.CASCADE,
                           related_name='poze_instalatie_electrica')

    class PozeInstalatieTermica(Orderable, Poza):
        page = ParentalKey('ConservarePage', on_delete=models.CASCADE,
                           related_name='poze_instalatie_termica')

    class PozeParatraznet(Orderable, Poza):
        page = ParentalKey(
            'ConservarePage', on_delete=models.CASCADE, related_name='poze_paratraznet')

    class PozeStratPictural(Orderable, Poza):
        page = ParentalKey(
            'ConservarePage', on_delete=models.CASCADE, related_name='poze_strat_pictural')

    class PozeObiecteDeCultConservare(Orderable, Poza):
        page = ParentalKey('ConservarePage', on_delete=models.CASCADE,
                           related_name='poze_obiecte_de_cult')

    class PozeMobilier(Orderable, Poza):
        page = ParentalKey(
            'ConservarePage', on_delete=models.CASCADE, related_name='poze_mobilier')


class ConservarePage(Page):
    # Sit
    sit = models.IntegerField(choices=NR15, null=True,
                              blank=True, verbose_name='Stare')
    sit_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')
    sit_pericol = models.BooleanField(
        default=False, verbose_name='Pericol')

    elemente_arhitecturale = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    elemente_arhitecturale_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')
    elemente_arhitecturale_pericol = models.BooleanField(
        default=False, verbose_name='Pericol')

    alte_elemente_importante = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    alte_elemente_importante_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')
    alte_elemente_importante_pericol = models.BooleanField(
        default=False, verbose_name='Pericol')

    vegetatie = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    vegetatie_pericol = models.BooleanField(
        default=False, verbose_name='Pericol')
    vegetatie_observatii = RichTextField(
        features=[], null=True, blank=True, help_text="Vegetație invazivă ce poate pune monumentul în pericol", verbose_name='Observații')

    # Structura bisericii
    teren = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    teren_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    teren_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    fundatii = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    fundatii_pericol = models.BooleanField(
        default=False, verbose_name='Pericol')
    fundatii_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    talpi = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    talpi_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    talpi_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    corp_biserica = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    corp_biserica_pericol = models.BooleanField(
        default=False, verbose_name='Pericol')
    corp_biserica_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    bolti = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    bolti_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    bolti_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    cosoroabe = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    cosoroabe_pericol = models.BooleanField(
        default=False, verbose_name='Pericol')
    cosoroabe_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    sarpanta_peste_corp_biserica = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    sarpanta_peste_corp_biserica_pericol = models.BooleanField(
        default=False, verbose_name='Pericol')
    sarpanta_peste_corp_biserica_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    turn = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    turn_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    turn_observatii = RichTextField(features=[], null=True, blank=True,
                                    help_text="Starea structurii turnului, inclusiv a tălpilor și a coifului", verbose_name='Observații')

    # Finisaje biserică
    zona_din_jurul_biserici = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    zona_din_jurul_biserici_pericol = models.BooleanField(
        default=False, verbose_name='Pericol')
    zona_din_jurul_biserici_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    pardoseli_interioare = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    pardoseli_interioare_pericol = models.BooleanField(
        default=False, verbose_name='Pericol')
    pardoseli_interioare_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    finisaj_exterior = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    finisaj_exterior_pericol = models.BooleanField(
        default=False, verbose_name='Pericol')
    finisaj_exterior_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    finisaj_pereti_interiori = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    finisaj_pereti_interiori_pericol = models.BooleanField(
        default=False, verbose_name='Pericol')
    finisaj_pereti_interiori_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    finisaj_tavane_si_bolti = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    finisaj_tavane_si_bolti_pericol = models.BooleanField(
        default=False, verbose_name='Pericol')
    finisaj_tavane_si_bolti_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    tamplarii = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    tamplarii_pericol = models.BooleanField(
        default=False, verbose_name='Pericol')
    tamplarii_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    invelitoare_sarpanta_si_turn = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    invelitoare_sarpanta_si_turn_pericol = models.BooleanField(
        default=False, verbose_name='Pericol')
    invelitoare_sarpanta_si_turn_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    instalatie_electrica = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    instalatie_electrica_pericol = models.BooleanField(
        default=False, verbose_name='Pericol')
    instalatie_electrica_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    instalatie_termica = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    instalatie_termica_pericol = models.BooleanField(
        default=False, verbose_name='Pericol')
    instalatie_termica_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    paratraznet = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    paratraznet_pericol = models.BooleanField(
        default=False, verbose_name='Pericol')
    paratraznet_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    # Starea componenta artistică
    strat_pictural = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    strat_pictural_pericol = models.BooleanField(
        default=False, verbose_name='Pericol')
    strat_pictural_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    obiecte_de_cult = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    obiecte_de_cult_pericol = models.BooleanField(
        default=False, verbose_name='Pericol')
    obiecte_de_cult_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    mobilier = models.IntegerField(
        choices=NR15, null=True, blank=True, verbose_name='Stare')
    mobilier_pericol = models.BooleanField(
        default=False, verbose_name='Pericol')
    mobilier_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    subpage_types = []

    sit_panels = [
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('sit'),
                    FieldPanel('sit_pericol'),
                ]),
                FieldPanel('sit_observatii'),
                InlinePanel('poze_sit', label="Poză")
            ],
            heading="Sit",
            classname="collapsible collapsed ",
        ),

        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('elemente_arhitecturale'),
                    FieldPanel('elemente_arhitecturale_pericol'),
                ]),

                FieldPanel('elemente_arhitecturale_observatii'),
                InlinePanel('poze_elemente_arhitecturale', label="Poză")
            ],
            heading="Elemente arhitecturale",
            classname="collapsible collapsed ",
        ),

        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('alte_elemente_importante'),
                    FieldPanel('alte_elemente_importante_pericol'),
                ]),
                FieldPanel('alte_elemente_importante_observatii'),
                InlinePanel('poze_alte_elemente_importante', label="Poză")
            ],
            heading="Alte elemente importante",
            classname="collapsible collapsed ",
        ),

        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('vegetatie'),
                    FieldPanel('vegetatie_pericol'),
                ]),
                FieldPanel('vegetatie_observatii'),
                InlinePanel('poze_vegetatie', label="Poză")
            ],
            heading="Vegetație",
            classname="collapsible collapsed ",
        ),
    ]

    structura_panels = [
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('teren'),
                    FieldPanel('teren_pericol'),
                ]),
                FieldPanel('teren_observatii'),
                InlinePanel('poze_teren', label="Poză")
            ],
            heading="Teren",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('fundatii'),
                    FieldPanel('fundatii_pericol'),
                ]),
                FieldPanel('fundatii_observatii'),
                InlinePanel('poze_fundatii', label="Poză")
            ],
            heading="Fundații",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('talpi'),
                    FieldPanel('talpi_pericol'),
                ]),
                FieldPanel('talpi_observatii'),
                InlinePanel('poze_talpi', label="Poză")
            ],
            heading="Tălpi",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('corp_biserica'),
                    FieldPanel('corp_biserica_pericol'),
                ]),
                FieldPanel('corp_biserica_observatii'),
                InlinePanel('poze_corp_biserica', label="Poză")
            ],
            heading="Corp biserică",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('bolti'),
                    FieldPanel('bolti_pericol'),
                ]),
                FieldPanel('bolti_observatii'),
                InlinePanel('poze_bolti', label="Poză")
            ],
            heading="Bolți",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('cosoroabe'),
                    FieldPanel('cosoroabe_pericol'),
                ]),
                FieldPanel('cosoroabe_observatii'),
                InlinePanel('poze_cosoroabe', label="Poză")
            ],
            heading="Cosoroabe",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('sarpanta_peste_corp_biserica'),
                    FieldPanel('sarpanta_peste_corp_biserica_pericol'),
                ]),
                FieldPanel('sarpanta_peste_corp_biserica_observatii'),
                InlinePanel('poze_sarpanta_corp_biserica', label="Poză")
            ],
            heading="Șarpantă corp biserică",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('turn'),
                    FieldPanel('turn_pericol'),
                ]),
                FieldPanel('turn_observatii'),
                InlinePanel('poze_turn', label="Poză")
            ],
            heading="Turn",
            classname="collapsible collapsed ",
        ),

    ]

    finisaje_panels = [
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('zona_din_jurul_biserici'),
                    FieldPanel('zona_din_jurul_biserici_pericol'),
                ]),
                FieldPanel('zona_din_jurul_biserici_observatii'),
                InlinePanel('poze_zona_din_jurul_biserici', label="Poză")
            ],
            heading="Zona din jurul biserici",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('pardoseli_interioare'),
                    FieldPanel('pardoseli_interioare_pericol'),
                ]),
                FieldPanel('pardoseli_interioare_observatii'),
                InlinePanel('poze_pardoseli_interioare', label="Poză")
            ],
            heading="Pardoseli interioare",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('finisaj_exterior'),
                    FieldPanel('finisaj_exterior_pericol'),
                ]),
                FieldPanel('finisaj_exterior_observatii'),
                InlinePanel('poze_finisaj_exterior', label="Poză")
            ],
            heading="Finisaj pereți exteriori",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('finisaj_pereti_interiori'),
                    FieldPanel('finisaj_pereti_interiori_pericol'),
                ]),
                FieldPanel('finisaj_pereti_interiori_observatii'),
                InlinePanel('poze_finisaj_pereti_interiori', label="Poză")
            ],
            heading="Finisaj pereți interiori",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('finisaj_tavane_si_bolti'),
                    FieldPanel('finisaj_tavane_si_bolti_pericol'),
                ]),
                FieldPanel('finisaj_tavane_si_bolti_observatii'),
                InlinePanel('poze_finisaj_tavane_si_bolti', label="Poză")
            ],
            heading="Finisaj tavane și bolți",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('tamplarii'),
                    FieldPanel('tamplarii_pericol'),
                ]),
                FieldPanel('tamplarii_observatii'),
                InlinePanel('poze_tamplarii', label="Poză")
            ],
            heading="Tâmplării",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('invelitoare_sarpanta_si_turn'),
                    FieldPanel('invelitoare_sarpanta_si_turn_pericol'),
                ]),
                FieldPanel('invelitoare_sarpanta_si_turn_observatii'),
                InlinePanel('poze_invelitoare_sarpanta_si_turn', label="Poză")
            ],
            heading="Învelitoare șarpantă și turn",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('instalatie_electrica'),
                    FieldPanel('instalatie_electrica_pericol'),
                ]),
                FieldPanel('instalatie_electrica_observatii'),
                InlinePanel('poze_instalatie_electrica', label="Poză")
            ],
            heading="Instalație electrică",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('instalatie_termica'),
                    FieldPanel('instalatie_termica_pericol'),
                ]),
                FieldPanel('instalatie_termica_observatii'),
                InlinePanel('poze_instalatie_termica', label="Poză")
            ],
            heading="Instalație termică",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('paratraznet'),
                    FieldPanel('paratraznet_pericol'),
                ]),
                FieldPanel('paratraznet_observatii'),
                InlinePanel('poze_paratraznet', label="Poză")
            ],
            heading="Paratrăznet",
            classname="collapsible collapsed ",
        ),
    ]

    componenta_artistica_panels = [
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('strat_pictural'),
                    FieldPanel('strat_pictural_pericol'),
                ]),
                FieldPanel('strat_pictural_observatii'),
                InlinePanel('poze_strat_pictural', label="Poză")
            ],
            heading="Strat pictural",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('obiecte_de_cult'),
                    FieldPanel('obiecte_de_cult_pericol'),
                ]),
                FieldPanel('obiecte_de_cult_observatii'),
                InlinePanel('poze_obiecte_de_cult', label="Poză")
            ],
            heading="Obiecte de cult",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('mobilier'),
                    FieldPanel('mobilier_pericol'),
                ]),
                FieldPanel('mobilier_observatii'),
                InlinePanel('poze_mobilier', label="Poză")
            ],
            heading="Mobilier",
            classname="collapsible collapsed ",
        ),

    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(sit_panels, heading='Sit'),
            ObjectList(structura_panels, heading='Structura bisericii'),
            ObjectList(finisaje_panels, heading='Finisaje biserică'),
            ObjectList(componenta_artistica_panels,
                       heading='Componenta Artistică'),
        ])

    class Meta:  # noqa

        verbose_name = "Conservare"
        verbose_name_plural = "Conservare"

    def save(self, *args, **kwargs):

        nota_conservare = 0
        active_fields = 0
        has_pericol = False
        min_pericol = 15

        fields = [
            "sit",
            "elemente_arhitecturale",
            "alte_elemente_importante",
            "vegetatie",
            "teren",
            "fundatii",
            "talpi",
            "corp_biserica",
            "bolti",
            "cosoroabe",
            "sarpanta_peste_corp_biserica",
            "turn",
            "zona_din_jurul_biserici",
            "pardoseli_interioare",
            "finisaj_exterior",
            "finisaj_pereti_interiori",
            "finisaj_tavane_si_bolti",
            "tamplarii",
            "invelitoare_sarpanta_si_turn",
            "instalatie_electrica",
            "instalatie_termica",
            "paratraznet",
            "strat_pictural",
            "obiecte_de_cult",
            "mobilier",
        ]

        for field in fields:
            field_value = getattr(self, field)
            if field_value:
                try:
                    pericol_field = getattr(self, field + '_pericol')
                    if pericol_field:
                        has_pericol = True
                        if min_pericol > field_value:
                            min_pericol = field_value
                except:
                    pass

                nota_conservare += field_value
                active_fields += 1


        if has_pericol:
            nota_conservare = min_pericol
        else:
            if active_fields:
                nota_conservare = nota_conservare / active_fields

        biserica = self.get_parent().specific
        biserica.conservare = nota_conservare

        if biserica.valoare:
            biserica.prioritizare = biserica.valoare * biserica.conservare
        biserica.save_revision()

        return super().save(*args, **kwargs)


class PozeArtisticEtapeIstoriceVizibile(Orderable):
    page = ParentalKey('ArtisticEtapeIstoriceVizibile',
                       on_delete=models.CASCADE, related_name='poze')
    poza = models.ForeignKey('wagtailimages.Image', null=True,
                             blank=True, on_delete=models.SET_NULL, related_name='+')
    rendition = models.JSONField(null=True, blank=True)
    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        ImageChooserPanel('poza'),
        FieldPanel('observatii'),
    ]


class ArtisticEtapeIstoriceVizibile(ClusterableModel, Orderable):
    page = ParentalKey('ComponentaArtisticaPage', on_delete=models.CASCADE,
                       related_name='etape_istorice_vizibile')

    element = models.ForeignKey(
        'nomenclatoare.ElementInteriorBiserica', on_delete=models.SET_NULL, null=True, blank=True)
    datat = models.BooleanField(default=False)
    an = models.IntegerField(null=True, blank=True)
    interventie_neconforma = models.BooleanField(default=False)
    sursa = RichTextField(features=[], null=True, blank=True)
    observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        FieldPanel('element'),
        FieldPanel('datat'),
        FieldPanel('an'),
        FieldPanel('interventie_neconforma'),
        FieldPanel('sursa'),
        FieldPanel('observatii'),
        InlinePanel('poze', label='Poză'),
    ]

    def __str__(self):
        return str(self.element)

class PozeProscomidie(Orderable, Poza):
    page = ParentalKey('ComponentaArtisticaPage',
                       on_delete=models.CASCADE, related_name='poze_proscomidie')


class PozeElementeSculptate(Orderable, Poza):
    page = ParentalKey('ComponentaArtisticaPage', on_delete=models.CASCADE,
                       related_name='poze_elemente_sculptate')


class PozeIcoaneVechi(Orderable, Poza):
    page = ParentalKey('ComponentaArtisticaPage',
                       on_delete=models.CASCADE, related_name='poze_icoane_vechi')


class PozeObiecteDeCult(Orderable, Poza):
    page = ParentalKey('ComponentaArtisticaPage',
                       on_delete=models.CASCADE, related_name='poze_obiecte_de_cult')


class PozeMobiliere(Orderable, Poza):
    page = ParentalKey('ComponentaArtisticaPage',
                       on_delete=models.CASCADE, related_name='poze_mobiliere')


class PozeObiecteInstrainate(Orderable, Poza):
    page = ParentalKey('ComponentaArtisticaPage', on_delete=models.CASCADE,
                       related_name='poze_obiecte_instrainate')


class PozeIconostas(Orderable, Poza):
    page = ParentalKey('ComponentaArtisticaPage',
                       on_delete=models.CASCADE, related_name='poze_iconostas')


class PozePereteDespartitor(Orderable, Poza):
    page = ParentalKey('ComponentaArtisticaPage', on_delete=models.CASCADE,
                       related_name='poze_perete_despartitor')


class PozeAltar(Orderable, Poza):
    page = ParentalKey('ComponentaArtisticaPage',
                       on_delete=models.CASCADE, related_name='poze_altar')


class PozePicturaExterioara(Orderable, Poza):
    page = ParentalKey('ComponentaArtisticaPage', on_delete=models.CASCADE,
                       related_name='poze_pictura_exterioara')


class PozePicturaInterioara(Orderable, Poza):
    page = ParentalKey('ComponentaArtisticaPage', on_delete=models.CASCADE,
                       related_name='poze_pictura_interioara')


class ComponentaArtisticaPage(Page):
    proscomidie = models.BooleanField(
        default=False, verbose_name="Proscomidie în exteriorul altarului")
    suport_proscomidie = ParentalManyToManyField(
        'nomenclatoare.SuportPictura', blank=True)

    elemente_sculptate = models.BooleanField(
        default=False, verbose_name="Elemente sculptate / decoruri în biserică")
    elemente_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name="Observații")

    alte_icoane_vechi = models.BooleanField(
        default=False, verbose_name="Alte icoane vechi")
    alte_icoane_vechi_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name="Observații")

    obiecte_de_cult = ParentalManyToManyField(
        'nomenclatoare.ObiectCult', verbose_name="Obiecte de cult", blank=True)
    obiecte_de_cult_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name="Observații")

    mobiliere = ParentalManyToManyField(
        'nomenclatoare.MaterialMobilier', verbose_name="Mobilier", blank=True)
    mobiliere_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name="Observații")

    obiecte_instrainate = models.BooleanField(
        default=False, verbose_name="Obiecte de cult înstrăinate")
    obiecte_instrainate_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name="Observații")

    # Pictură exterioară aplicată
    # Pictură interioară aplicată

    # Iconostasul  (dintre naos și altar)
    iconostas_naos_altar_tip = models.ForeignKey('nomenclatoare.TipIconostas', verbose_name='Tip',
                                                 null=True, blank=True, on_delete=models.SET_NULL, related_name='p_iconostasuri_naos_altar')
    iconostas_naos_altar_numar_intrari = models.IntegerField(
        verbose_name='Număr intrări', null=True, blank=True)
    iconostas_naos_altar_tehnica = ParentalManyToManyField(
        'nomenclatoare.TehnicaIconostas', verbose_name='Tehnică', related_name='p_iconostasuri_naos_altar', blank=True)
    iconostas_naos_altar_registre = ParentalManyToManyField(
        'nomenclatoare.RegistruIconostas', verbose_name='Registru', related_name='p_iconostasuri_naos_altar', blank=True)
    iconostas_naos_altar_tip_usi = ParentalManyToManyField(
        'nomenclatoare.TipUsiIconostas', verbose_name='Tip uși', related_name='p_iconostasuri_naos_altar', blank=True)
    iconostas_naos_altar_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name="Observații")
    iconostas_naos_altar_materiale = ParentalManyToManyField(
        'nomenclatoare.MaterialIconostas', verbose_name='Material', blank=True, related_name='p_iconostasuri_naos_altar')

    # Iconostasul  (dintre pronaos și naos)
    iconostas_pronaos_naos_tip = models.ForeignKey('nomenclatoare.TipIconostas', verbose_name='Tip',
                                                   null=True, blank=True, on_delete=models.SET_NULL, related_name='p_iconostasuri_pronaos_naos')
    iconostas_pronaos_naos_materiale = models.ForeignKey(
        'nomenclatoare.MaterialIconostas', verbose_name='Material', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_iconostasuri_pronaos_naos')
    iconostas_pronaos_naos_numar_intrari = models.IntegerField(
        verbose_name='Număr intrări', null=True, blank=True)
    iconostas_pronaos_naos_tehnica = ParentalManyToManyField(
        'nomenclatoare.TehnicaIconostas', verbose_name='Tehnica', related_name='p_iconostasuri_pronaos_naos', blank=True)
    iconostas_pronaos_naos_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name="Observații")

    # Altar
    altar_placa_mesei = ParentalManyToManyField(
        'nomenclatoare.MaterialMasaAltar', verbose_name='Placa mesei', blank=True, related_name='p_placa_mesei')
    altar_piciorul_mesei = ParentalManyToManyField(
        'nomenclatoare.MaterialMasaAltar', verbose_name='Piciorul mesei', blank=True, related_name='p_piciorul_mesei')
    altar_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name="Observații")

    # Pictura Exterioara
    pictura_exterioara_localizare = models.ForeignKey('nomenclatoare.LocalizarePictura', on_delete=models.SET_NULL,
                                                      null=True, blank=True, related_name='p_localizari_exterioare', verbose_name='Proporția de suprafață acoperită')
    pictura_exterioara_localizare_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name="Observații")
    pictura_exterioara_tehnica = models.ForeignKey('nomenclatoare.TehnicaPictura', on_delete=models.SET_NULL,
                                                   null=True, blank=True, related_name='p_localizari_exterioare', verbose_name='Tehnică')
    pictura_exterioara_suport = ParentalManyToManyField(
        'nomenclatoare.SuportPictura', blank=True, related_name='p_localizari_exterioare', verbose_name='Suport')
    pictura_exterioara_numar_straturi_pictura = models.IntegerField(
        null=True, blank=True, verbose_name='Număr straturi')

    pictura_exterioara_sursa_datare = ParentalManyToManyField(
        'nomenclatoare.SursaDatare', related_name='p_componente_artistice_exterioare', blank=True, verbose_name='Sursa datare')
    pictura_exterioara_anul_picturii = models.IntegerField(
        null=True, blank=True, verbose_name='Anul picturii')
    pictura_exterioara_datare_prin_interval_timp = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='Datare prin interval de timp')
    pictura_exterioara_datare_secol = models.ForeignKey(
        'nomenclatoare.Secol', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_localizari_exterioare', verbose_name='Datare secol')
    pictura_exterioara_datare_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name="Observații")

    # Pictura Interioara
    pictura_interioara_localizare = models.ForeignKey('nomenclatoare.LocalizarePictura', verbose_name="Proporția de suprafață acoperită",
                                                      on_delete=models.SET_NULL, null=True, blank=True, related_name='p_localizari_interioare')
    pictura_interioara_localizare_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name="Observatii")
    pictura_interioara_tehnica_pictura = models.ForeignKey(
        'nomenclatoare.TehnicaPictura', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Tehnică')
    pictura_interioara_suport = ParentalManyToManyField(
        'nomenclatoare.SuportPictura', blank=True, related_name='p_localizari_interioare', verbose_name='Suport')
    pictura_interioara_numar_straturi_pictura = models.IntegerField(
        null=True, blank=True, verbose_name='Număr straturi')

    pictura_interioara_sursa_datare = ParentalManyToManyField(
        'nomenclatoare.SursaDatare', related_name='p_componente_artistice_interioare', blank=True, verbose_name='Sursa datare')
    pictura_interioara_anul_picturii = models.IntegerField(
        null=True, blank=True, verbose_name='Anul picturii')
    pictura_interioara_datare_prin_interval_timp = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='Datare prin interval de timp')
    pictura_interioara_datare_secol = models.ForeignKey(
        'nomenclatoare.Secol', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_localizari_interioare', verbose_name='Datare secol')
    pictura_interioara_datare_observatii = RichTextField(
        features=[], null=True, blank=True, verbose_name="Observații")


    # Invisible fields
    elemente_interventii = ArrayField(
            models.CharField(max_length=100, blank=True),
            size=20,
            null=True,
            blank=True,
            verbose_name='Element'
        )

    general_panels = [
        MultiFieldPanel(
            [
                FieldPanel('proscomidie'),
                FieldPanel('suport_proscomidie',
                           widget=forms.CheckboxSelectMultiple),
                InlinePanel('poze_proscomidie', label="Poză")
            ],
            heading="Proscomidie",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('elemente_sculptate'),
                FieldPanel('elemente_observatii'),
                InlinePanel('poze_elemente_sculptate', label="Poză")
            ],
            heading="Elemente Sculptate",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('alte_icoane_vechi'),
                FieldPanel('alte_icoane_vechi_observatii'),
                InlinePanel('poze_icoane_vechi', label="Poză")
            ],
            heading="Alte icoane vechi",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('obiecte_de_cult',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('obiecte_de_cult_observatii'),
                InlinePanel('poze_obiecte_de_cult', label="Poză")
            ],
            heading="Obiecte de cult",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel(
                    'mobiliere', widget=forms.CheckboxSelectMultiple),
                FieldPanel('mobiliere_observatii'),
                InlinePanel('poze_mobiliere', label="Poză")
            ],
            heading="Mobiliere",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('obiecte_instrainate'),
                FieldPanel('obiecte_instrainate_observatii'),
                InlinePanel('poze_obiecte_instrainate', label="Poză")
            ],
            heading="Obiecte de cult înstrăinate",
            classname="collapsible collapsed ",
        ),
    ]

    iconostas_panels = [
        MultiFieldPanel(
            [
                FieldPanel('iconostas_naos_altar_tip'),
                FieldPanel('iconostas_naos_altar_numar_intrari'),
                FieldPanel('iconostas_naos_altar_materiale',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('iconostas_naos_altar_tehnica',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('iconostas_naos_altar_registre',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('iconostas_naos_altar_tip_usi',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('iconostas_naos_altar_observatii'),
                InlinePanel('poze_iconostas', label="Poză")
            ],
            heading="",
            classname="collapsible ",
        ),
    ]

    perete_despartitor_panels = [
        MultiFieldPanel(
            [
                FieldPanel('iconostas_pronaos_naos_tip'),
                FieldPanel('iconostas_pronaos_naos_materiale'),
                FieldPanel('iconostas_pronaos_naos_numar_intrari'),
                FieldPanel('iconostas_pronaos_naos_tehnica',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('iconostas_pronaos_naos_observatii'),
                InlinePanel('poze_perete_despartitor', label="Poză")
            ],
            heading="",
            classname="collapsible ",
        ),
    ]

    altar_panels = [
        MultiFieldPanel(
            [
                FieldPanel('altar_placa_mesei',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('altar_piciorul_mesei',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('altar_observatii'),
                InlinePanel('poze_altar', label="Poză")
            ],
            heading="",
            classname="collapsible ",
        ),
    ]

    exterior_panels = [

        MultiFieldPanel(
            [
                FieldPanel('pictura_exterioara_localizare'),
                FieldPanel('pictura_exterioara_localizare_observatii'),
                FieldPanel('pictura_exterioara_tehnica'),
                FieldPanel('pictura_exterioara_suport',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('pictura_exterioara_numar_straturi_pictura'),
                InlinePanel('poze_pictura_exterioara', label="Poză")
            ],
            heading="",
            classname="collapsible ",
        ),

        MultiFieldPanel(
            [
                FieldPanel('pictura_exterioara_sursa_datare',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('pictura_exterioara_anul_picturii'),
                FieldPanel('pictura_exterioara_datare_prin_interval_timp'),
                FieldPanel('pictura_exterioara_datare_secol'),
                FieldPanel('pictura_exterioara_datare_observatii'),
            ],
            heading="Datare",
            classname="collapsible ",
        ),
    ]

    interior_panels = [
        MultiFieldPanel(
            [
                FieldPanel('pictura_interioara_localizare'),
                FieldPanel('pictura_interioara_localizare_observatii'),
                FieldPanel('pictura_interioara_tehnica_pictura'),
                FieldPanel('pictura_interioara_suport',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('pictura_interioara_numar_straturi_pictura'),
                InlinePanel('poze_pictura_interioara', label="Poză")
            ],
            heading="",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('pictura_interioara_sursa_datare',
                           widget=forms.CheckboxSelectMultiple),
                FieldPanel('pictura_interioara_anul_picturii'),
                FieldPanel('pictura_interioara_datare_prin_interval_timp'),
                FieldPanel('pictura_interioara_datare_secol'),
                FieldPanel('pictura_interioara_datare_observatii'),
            ],
            heading="Datare",
            classname="collapsible ",
        ),
    ]

    interventii_panels = [
        MultiFieldPanel(
            [
                InlinePanel('etape_istorice_vizibile', label="Etapă")
            ],
            heading="Etape istorice vizibile",
            classname="collapsible ",
        ),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(general_panels, heading='General'),
            ObjectList(iconostas_panels, heading='Iconostasul'),
            ObjectList(perete_despartitor_panels,
                       heading='Perete despărțitor (pronaos/naos)'),
            ObjectList(altar_panels, heading='Altar'),
            ObjectList(exterior_panels, heading='Pictură exterioară'),
            ObjectList(interior_panels, heading='Pictură interioară'),
            ObjectList(interventii_panels, heading='Intervenții'),
        ])

    class Meta:  # noqa

        verbose_name = "Componenta Artistică"
        verbose_name_plural = "Componenta Artistică"

    def save(self, *args, **kwargs):
        elemente_interventii = []
        for x in self.etape_istorice_vizibile.all():
            if x.element:
                elemente_interventii.append(x.element.nume)
        self.elemente_interventii = elemente_interventii

        return super().save(*args, **kwargs)

