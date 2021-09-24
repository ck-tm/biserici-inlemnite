from django.db import models
from django import forms
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
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from wagtailmodelchooser.edit_handlers import ModelChooserPanel

from wagtail.admin.edit_handlers import InlinePanel as BaseInlinePanel

class InlinePanel(BaseInlinePanel):
    def widget_overrides(self):
        widgets = {}
        child_edit_handler = self.get_child_edit_handler()
        for handler_class in child_edit_handler.children:
            widgets.update(handler_class.widget_overrides())
        widget_overrides = {self.relation_name: widgets}
        return widget_overrides


from app import blocks

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

class HomePage(Page):
    """Home page model."""

    template = "home/home_page.html"
    subpage_types = [
        "BisericaPage"
    ]
    parent_page_type = [
        'wagtailcore.Page'
    ]

    # banner_title = models.CharField(max_length=100, blank=False, null=True)
    # banner_subtitle = RichTextField(features=["bold", "italic"])
    # banner_image = models.ForeignKey(
    #     "wagtailimages.Image",
    #     null=True,
    #     blank=False,
    #     on_delete=models.SET_NULL,
    #     related_name="+",
    # )
    # banner_cta = models.ForeignKey(
    #     "wagtailcore.Page",
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name="+",
    # )

    # streamfields = StreamField([
    #     ("cta", blocks.CTABlock()),
    # ], null=True, blank=True)

    # content_panels = Page.content_panels + [
    #     StreamFieldPanel("streamfields"),
    # ]

    # # Custom list of panels. We'll put this in an ObjectList later.
    # banner_panels = [
    #     MultiFieldPanel(
    #         [
    #             FieldPanel("banner_title"),
    #             FieldPanel("banner_subtitle"),
    #             ImageChooserPanel("banner_image"),
    #             PageChooserPanel("banner_cta"),
    #         ],
    #         heading="Banner Options",
    #     ),
    # ]

    # # This is where all the tabs are created
    # edit_handler = TabbedInterface(
    #     [
    #         ObjectList(content_panels, heading='Content'),
    #         # This is our custom banner_panels. It's just a list, how easy!
    #         ObjectList(banner_panels, heading="Banner Settings"),
    #         ObjectList(Page.promote_panels, heading='Promotional Stuff'),
    #         ObjectList(Page.settings_panels, heading='Settings Stuff'),
    #     ]
    # )

    class Meta:  # noqa

        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


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

    judet = models.ForeignKey('nomenclatoare.Judet', null=True, blank=True, on_delete=models.SET_NULL, related_name='pp_biserici')

    promote_panels = []

    content_panels = Page.content_panels + [
        ModelChooserPanel("judet"),
    ]

    # def get_children(self):
    #     print('get  children')
    #     qs = super().get_children()
    #     print(qs)
    #     qs = qs.order_by('title')
    #     print(qs.order_by('title'))
    #     return qs.order_by('title')

    class Meta:  # noqa

        verbose_name = "Biserică"
        verbose_name_plural = "Biserici"

class IdentificarePage(Page):
    """Home page model."""

    # judet = models.ForeignKey('nomenclatoare.Judet', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_biserici')
    localitate = models.ForeignKey('nomenclatoare.Localitate', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_biserici')
    adresa = models.CharField(max_length=250, null=True, blank=True)
    latitudine = models.FloatField(null=True, blank=True)
    longitudine = models.FloatField(null=True, blank=True)
    statut = models.ForeignKey('nomenclatoare.StatutBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_biserici')
    denumire_actuala = models.CharField(max_length=150, null=True, blank=True, verbose_name="Actuală")
    denumire_precedenta = models.CharField(max_length=150, null=True, blank=True, verbose_name="Precendentă")
    denumire_locala = models.CharField(max_length=150, null=True, blank=True, verbose_name="Locală")
    denumire_oberservatii =  RichTextField(features=[], null=True, blank=True, verbose_name="Observații")
    cult = models.ForeignKey('nomenclatoare.CultBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_biserici')
    utilizare = models.ForeignKey('nomenclatoare.UtilizareBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_biserici')
    utilizare_observatii =  RichTextField(features=[], null=True, blank=True, verbose_name="Observații")
    singularitate = models.ForeignKey('nomenclatoare.SingularitateBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_biserici')
    singularitate_observatii =  RichTextField(features=[], null=True, blank=True, verbose_name="Observații")
    functiune = models.ForeignKey('nomenclatoare.FunctiuneBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_biserici')
    functiune_observatii =  RichTextField(features=[], null=True, blank=True, verbose_name='Observații')
    functiune_initiala = models.ForeignKey('nomenclatoare.FunctiuneBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_biserici_initiale')
    functiune_initiala_observatii =  RichTextField(features=[], null=True, blank=True, verbose_name='Observații')
    proprietate_actuala = models.ForeignKey('nomenclatoare.ProprietateBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_biserici_initiale')
    proprietate_observatii =  RichTextField(features=[], null=True, blank=True)
    proprietar_actual =  RichTextField(features=[], null=True, blank=True)
    inscriere_documente_cadastrale = models.IntegerField(choices=IDENTIFICARE_DOC_CADASTRALE, null=True, blank=True)


    subpage_types = []

    promote_panels = []

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
            ModelChooserPanel("localitate"),
            FieldPanel("adresa"),
            FieldPanel("latitudine"),
            FieldPanel("longitudine")],
            heading="Localizare",
            classname="collapsible collapsed ",
        ),
        FieldPanel("statut"),
        MultiFieldPanel(
            [ 
                FieldPanel("denumire_actuala"),
                FieldPanel("denumire_precedenta"),
                FieldPanel("denumire_locala"),
                FieldPanel("denumire_oberservatii")
            ],
            heading="Denumire",
            classname="collapsible collapsed ",
        ),
        FieldPanel("cult"),
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
        FieldPanel("inscriere_documente_cadastrale")
    ]
    class Meta:  # noqa

        verbose_name = "Identificare"
        verbose_name_plural = "Identificare"



class ElementAnsambluConstruit(models.Model):
    element = models.ForeignKey('nomenclatoare.ElementAnsambluConstruit', on_delete=models.CASCADE)
    observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        FieldPanel('element'),
        FieldPanel('observatii'),
    ]

    class Meta:
        abstract = True


class ElementeAnsambluConstruit(Orderable, ElementAnsambluConstruit):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE, related_name='elemente_ansamblu_construit')


class ElementImportantAnsambluConstruit(models.Model):
    element = models.ForeignKey('nomenclatoare.ElementImportant', on_delete=models.CASCADE)
    observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        FieldPanel('element'),
        FieldPanel('observatii'),
    ]

    class Meta:
        abstract = True


class ElementeImportanteAnsambluConstruit(Orderable, ElementImportantAnsambluConstruit):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE, related_name='elemente_importante_ansamblu_construit')



class PozeClopot(Orderable):
    page = ParentalKey('ClopoteBiserica', on_delete=models.CASCADE, related_name='poze_clopot')
    poza = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [
        ImageChooserPanel('poza')
    ]

class ClopotBiserica(ClusterableModel):
    an = models.IntegerField(null=True, blank=True, verbose_name='An')
    inscriptie = RichTextField(features=[], null=True, blank=True, verbose_name='Inscripție')
    observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        FieldPanel('an'),
        FieldPanel('inscriptie'),
        InlinePanel('poze_clopot', label='Poze')
    ]

    class Meta:
        abstract = True


class ClopoteBiserica(Orderable, ClopotBiserica):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE, related_name='clopote')


class PozeFinisajPortic(Orderable):
    page_portic = ParentalKey('FinisajePortic', on_delete=models.CASCADE, related_name='poze_finisaj')
    poza = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [
        ImageChooserPanel('poza')
    ]


class FinisajePortic(ClusterableModel, Orderable):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE, related_name='finisaje_portic')
    element = models.ForeignKey('nomenclatoare.ElementBiserica', on_delete=models.SET_NULL, null=True, blank=True)
    material = models.ForeignKey('nomenclatoare.Finisaj', null=True, blank=True, on_delete=models.CASCADE)
    observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        FieldPanel('element'),
        FieldPanel('material'),
        FieldPanel('observatii'),
        InlinePanel('poze_finisaj', label='Poze')
    ]


class PozeFinisajPronaos(Orderable):
    page_pronaos = ParentalKey('FinisajePronaos', on_delete=models.CASCADE, related_name='poze_finisaj')
    poza = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [
        ImageChooserPanel('poza')
    ]

class FinisajePronaos(ClusterableModel, Orderable):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE, related_name='finisaje_pronaos')
    element = models.ForeignKey('nomenclatoare.ElementBiserica', on_delete=models.SET_NULL, null=True, blank=True)
    material = models.ForeignKey('nomenclatoare.Finisaj', null=True, blank=True, on_delete=models.CASCADE)
    observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        FieldPanel('element'),
        FieldPanel('material'),
        FieldPanel('observatii'),
        InlinePanel('poze_finisaj', label='Poze')
    ]



class PozeFinisajNaos(Orderable):
    page_naos = ParentalKey('FinisajeNaos', on_delete=models.CASCADE, related_name='poze_finisaj')
    poza = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [
        ImageChooserPanel('poza')
    ]

class FinisajeNaos(ClusterableModel, Orderable):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE, related_name='finisaje_naos')
    element = models.ForeignKey('nomenclatoare.ElementBiserica', on_delete=models.SET_NULL, null=True, blank=True)
    material = models.ForeignKey('nomenclatoare.Finisaj', null=True, blank=True, on_delete=models.CASCADE)
    observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        FieldPanel('element'),
        FieldPanel('material'),
        FieldPanel('observatii'),
        InlinePanel('poze_finisaj', label='Poze')
    ]


class PozeFinisajAltar(Orderable):
    page_altar = ParentalKey('FinisajeAltar', on_delete=models.CASCADE, related_name='poze_finisaj')
    poza = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [
        ImageChooserPanel('poza')
    ]


class FinisajeAltar(ClusterableModel, Orderable):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE, related_name='finisaje_altar')
    element = models.ForeignKey('nomenclatoare.ElementBiserica', on_delete=models.SET_NULL, null=True, blank=True)
    material = models.ForeignKey('nomenclatoare.Finisaj', null=True, blank=True, on_delete=models.CASCADE)
    observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        FieldPanel('element'),
        FieldPanel('material'),
        FieldPanel('observatii'),
        InlinePanel('poze_finisaj', label='Poze')
    ]


class Poza(models.Model):
    poza = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        ImageChooserPanel('poza')
    ]

    class Meta:
        abstract = True


class PozeTurle(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE, related_name='poze_turle')

class PozeAccese(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE, related_name='poze_accese')

class PozeFerestre(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE, related_name='poze_ferestre')

class PozeOchiesi(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE, related_name='poze_ochiesi')

class PozeSolee(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE, related_name='poze_solee')

class PozeMasaAtlar(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE, related_name='poze_masa_atlar')

class PozeCor(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE, related_name='poze_cor')

class PozeSarpanta(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE, related_name='poze_sarpanta')

class PozeTurn(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE, related_name='poze_turn')

class PozeClopote(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE, related_name='poze_clopote')


class PozeTurle(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE, related_name='poze_turle')


class PozeGeneraleExterior(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE, related_name='poze_generale_exterior')

class PozeGeneraleInterior(Orderable, Poza):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE, related_name='poze_generale_interior')


class EtapeIstoriceVizibile(ClusterableModel, Orderable):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE, related_name='etape_istorice_vizibile')

    element = models.ForeignKey('nomenclatoare.ElementBiserica', on_delete=models.SET_NULL, null=True, blank=True)
    datat = models.BooleanField(default=False)
    an = models.IntegerField(null=True, blank=True)
    interventie_neconforma = models.BooleanField(default=False)
    sursa = RichTextField(features=[], null=True, blank=True)
    observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        FieldPanel('element'),
        FieldPanel('datat'),
        FieldPanel('an'),
        FieldPanel('interventie_neconforma'),
        FieldPanel('sursa'),
        FieldPanel('observatii'),
    ]


class DescrierePage(Page):
    """
    Capitol: Descriere Biserica
    """

    # Localizare/peisaj
    amplasament = models.ForeignKey('nomenclatoare.AmplasamentBiserica', null=True, blank=True, on_delete=models.SET_NULL)
    topografie = models.ForeignKey('nomenclatoare.TopografieBiserica', null=True, blank=True, on_delete=models.SET_NULL)
    toponim = models.CharField(max_length=150, null=True, blank=True, help_text="denumirea locului")
    toponim_sursa  = RichTextField(features=[], null=True, blank=True, verbose_name='Sursă informații')
    relatia_cu_cimitirul = models.ForeignKey('nomenclatoare.RelatieCimitir', null=True, blank=True, on_delete=models.SET_NULL)
    peisagistica_sitului = models.ManyToManyField('nomenclatoare.PeisagisticaSit', blank=True)
    observatii = RichTextField(features=[], null=True, blank=True)

    # Ansamblu construit
    elemente = models.ManyToManyField('nomenclatoare.ElementBiserica', help_text="Elemente ansamblu construit", blank=True)
    detalii_elemente = RichTextField(features=[], null=True, blank=True)

    elemente_importante = models.ManyToManyField('nomenclatoare.ElementImportant', help_text="Elemente ansamblu construit", blank=True)
    detalii_elemente_importante = RichTextField(features=[], null=True, blank=True)

    
    # Arhitectura bisericii
    planimetria_bisericii = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    materiale = models.ManyToManyField('nomenclatoare.Material', help_text="Materiale folosite in construcția bisericii", blank=True)
    detalii_materiale = RichTextField(features=[], null=True, blank=True, help_text="Materialele care compun structura de rezistentă a bisericii")

    # Elemente arhitecturale

    turn_dimensiune = models.ForeignKey('nomenclatoare.DimensiuneTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Dimensiune')
    turn_tip = models.ForeignKey('nomenclatoare.TipTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Tip')
    turn_numar = models.IntegerField(null=True, blank=True, verbose_name='Număr de turnuri')
    turn_numar_stalpi = models.IntegerField(null=True, blank=True, verbose_name='Număr stâlpi')
    turn_plan = models.ForeignKey('nomenclatoare.PlanTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Plan')
    turn_amplasare = models.ForeignKey('nomenclatoare.AmplasareTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Amplasare')
    turn_galerie = models.ForeignKey('nomenclatoare.GalerieTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Galerie')
    turn_numar_arcade = models.IntegerField(null=True, blank=True, verbose_name='Număr arcade Turn deschis')
    turn_numar_arcade_observatii =RichTextField(features=[], null=True, blank=True, verbose_name='Detalii arcade Turn deschis')
    turn_asezare_talpi  = models.ForeignKey('nomenclatoare.AsezareTalpaTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Așezarea tălpilor turnului în legătură cu corpul bisericii')
    turn_relatie_talpi  = models.ForeignKey('nomenclatoare.RelatieTalpaTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Relația dintre tălpile turnului')
    turn_numar_talpi = models.IntegerField(null=True, blank=True, verbose_name='Număr de tălpi')
    turn_observatii = RichTextField(features=[], null=True, blank=True, verbose_name="Observații")

    sarpanta_tip  = models.ManyToManyField('nomenclatoare.TipSarpanta', blank=True, verbose_name='Tip')
    sarpanta_veche_nefolosita = models.BooleanField(default=False, verbose_name='Veche nefolosită sub șarpanta actuală')
    sarpanta_numar_turnulete  = models.IntegerField(null=True, blank=True, verbose_name='Număr turnulețe decorative')
    sarpanta_numar_cruci  = models.IntegerField(null=True, blank=True, verbose_name='Număr cruci')
    sarpanta_material_cruci  = models.ForeignKey('nomenclatoare.Material', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Material cruci', related_name="p_material_cruci")
    sarpanta_observatii =RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    numar_accese_pridvor  = models.IntegerField(null=True, blank=True, verbose_name='Număr accese pridvor')
    numar_accese_pridvor_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații Pridvor')
    numar_accese_pronaos  = models.IntegerField(null=True, blank=True, verbose_name='Număr accese pronaos')
    numar_accese_pronaos_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații Pronaos')
    numar_accese_naos  = models.IntegerField(null=True, blank=True, verbose_name='Număr accese naos')
    numar_accese_naos_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații Naos')
    numar_accese_altar  = models.IntegerField(null=True, blank=True, verbose_name='Număr accese altar')
    numar_accese_altar_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații Altar')


    numar_ferestre_pridvor  = models.IntegerField(null=True, blank=True, verbose_name='Număr ferestre pridvor')
    numar_ferestre_pridvor_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații Pridvor')
    numar_ferestre_pronaos  = models.IntegerField(null=True, blank=True, verbose_name='Număr ferestre pronaos')
    numar_ferestre_pronaos_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații Pronaos')
    numar_ferestre_naos  = models.IntegerField(null=True, blank=True, verbose_name='Număr ferestre naos')
    numar_ferestre_naos_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații Naos')
    numar_ferestre_altar  = models.IntegerField(null=True, blank=True, verbose_name='Număr ferestre altar')
    numar_ferestre_altar_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații Altar')


    ochiesi_aerisitoare = models.BooleanField(default=False, verbose_name='Ochieși / Aerisitoare ')
    ochiesi_aerisitoare_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')


    
    bolta_peste_pronaos  = models.ForeignKey('nomenclatoare.TipBoltaPronaos', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Boltă peste pronaos', related_name='p_biserici_bolta_peste_pronaos')
    bolta_peste_pronaos_material = models.ManyToManyField('nomenclatoare.Material', blank=True, related_name='p_biserici_bolta_peste_pronaos')
    bolta_peste_pronaos_tipul_de_arc = models.ManyToManyField('nomenclatoare.TipArcBolta', blank=True, related_name='p_biserici_bolta_peste_pronaos')
    bolta_peste_pronaos_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    bolta_peste_naos  = models.ForeignKey('nomenclatoare.TipBoltaPronaos', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Boltă peste naos', related_name='p_biserici_bolta_peste_naos')
    bolta_peste_naos_material = models.ManyToManyField('nomenclatoare.Material', blank=True, related_name='p_biserici_bolta_peste_naos')
    bolta_peste_naos_tipul_de_arc = models.ManyToManyField('nomenclatoare.TipArcBolta', blank=True, related_name='p_biserici_bolta_peste_naos')
    bolta_peste_naos_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    bolta_peste_altar  = models.ForeignKey('nomenclatoare.BoltaPesteAltar', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Boltă peste altar', related_name='p_biserici_bolta_peste_altar')
    bolta_peste_altar_tip  = models.ForeignKey('nomenclatoare.TipBoltaPesteAltar', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Tip', related_name='p_biserici')
    bolta_peste_altar_material = models.ManyToManyField('nomenclatoare.Material', blank=True, related_name='p_biserici_bolta_peste_altar', verbose_name='Material')
    bolta_peste_altar_tipul_de_arc = models.ManyToManyField('nomenclatoare.TipArcBolta', blank=True, related_name='p_biserici_bolta_peste_altar', verbose_name='Tipul de arc')
    bolta_peste_altar_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    cor = models.BooleanField(default=False)
    cor_material = models.ManyToManyField('nomenclatoare.Material', blank=True, related_name='p_biserici_cor')
    cor_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    solee = models.BooleanField(default=False)
    solee_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    masa_altar_material_picior  = models.ForeignKey('nomenclatoare.Material', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Materialul piciorului', related_name='p_masa_altar_picior')
    masa_altar_material_blat  = models.ForeignKey('nomenclatoare.Material', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Materialul blatului', related_name='p_masa_altar_blat')
    masa_altar_observatii =  RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    turle_exista = models.BooleanField(default=False, verbose_name='Există')
    turle_numar = models.IntegerField(null=True, blank=True, verbose_name='Număr')
    turle_pozitionare = models.ManyToManyField('nomenclatoare.PozitionareTurle', blank=True, related_name='biserici', verbose_name='Poziționare')
    turle_numar_goluri  = models.IntegerField(null=True, blank=True, verbose_name='Număr goluri')
    turle_forma_sarpanta = models.ForeignKey('nomenclatoare.FormaSarpanteTurle', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici', verbose_name='Formă șarpantă')
    turle_observatii =  RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    # Structura
    fundatia  = models.ForeignKey('nomenclatoare.TipFundatie', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Tip', related_name='p_biserici')
    fundatia_observatii  = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')
    sistem_in_cheotoare = models.ForeignKey('nomenclatoare.TipStructuraCheotoare', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Tip', related_name='p_biserici')
    sistem_in_cheotoare_observatii  = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')
    sistem_in_catei  = models.ForeignKey('nomenclatoare.TipStructuraCatei', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Tip', related_name='p_biserici')
    sistem_in_catei_observatii  = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')
    sistem_mixt = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    tiranti_numar = models.IntegerField(null=True, blank=True, verbose_name='Număr')
    tiranti_tip = models.ForeignKey('nomenclatoare.TipTiranti', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Tip', related_name='p_biserici')
    tiranti_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')


    # Finisaje
    finisaj_exterior_tip = models.ManyToManyField('nomenclatoare.FinisajExterior', blank=True, verbose_name='Tip')
    finisaj_exterior_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    # Finisaje - Învelitoare corp biserică

    invelitoare_corp_material = models.ForeignKey('nomenclatoare.FinisajExterior', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Material', related_name='invelitoare_corp')
    invelitoare_corp_sindrila_lungime = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (lungime)')
    invelitoare_corp_sindrila_latime_medie = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (lățime medie)')
    invelitoare_corp_sindrila_grosime_medie = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (grosime medie)')
    invelitoare_corp_sindrila_pasul_latuirii = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (pasul lățuirii)')
    invelitoare_corp_sindrila_pasul_baterii = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (pasul baterii)')
    invelitoare_corp_sindrila_numar_straturi = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (număr straturi)')
    invelitoare_corp_sindrila_cu_horj = models.BooleanField(default=False, verbose_name='Șindrila cu horj')
    invelitoare_corp_sindrlia_tipul_de_batere = models.ForeignKey('nomenclatoare.TipBatereSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (tipul de batere)', related_name='invelitoare_corp')
    invelitoare_corp_sindrlia_tipul_prindere = models.ForeignKey('nomenclatoare.TipPrindereSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (tipul de prindere)', related_name='invelitoare_corp')
    invelitoare_corp_sindrlia_forma_botului = models.ForeignKey('nomenclatoare.TipBotSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (forma botului)', related_name='invelitoare_corp')
    invelitoare_corp_sindrila_cu_tesitura = models.BooleanField(default=False, verbose_name='Șindrila cu teșitură')
    invelitoare_corp_sindrlia_prelucrare = models.ForeignKey('nomenclatoare.TipPrelucrareSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (prelucrare)', related_name='invelitoare_corp')
    invelitoare_corp_sindrlia_esenta_lemnoasa = models.ForeignKey('nomenclatoare.EsentaLemnoasa', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (esență lemnoasă)', related_name='invelitoare_corp_sindrlia_esenta')
    invelitoare_corp_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    # Finisaje -  Învelitoare turn

    invelitoare_turn_material = models.ForeignKey('nomenclatoare.FinisajExterior', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Material', related_name='invelitoare_turn')
    invelitoare_turn_sindrila_lungime = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (lungime)')
    invelitoare_turn_sindrila_latime_medie = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (lățime medie)')
    invelitoare_turn_sindrila_grosime_medie = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (grosime medie)')
    invelitoare_turn_sindrila_pasul_latuirii = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (pasul lățuirii)')
    invelitoare_turn_sindrila_pasul_baterii = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (pasul baterii)')
    invelitoare_turn_sindrila_numar_straturi = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (număr straturi)')
    invelitoare_turn_sindrila_cu_horj = models.BooleanField(default=False, verbose_name='Șindrila cu horj')
    invelitoare_turn_sindrlia_tipul_de_batere = models.ForeignKey('nomenclatoare.TipBatereSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (tipul de batere)', related_name='invelitoare_turn')
    invelitoare_turn_sindrlia_tipul_prindere = models.ForeignKey('nomenclatoare.TipPrindereSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (tipul de prindere)', related_name='invelitoare_turn')
    invelitoare_turn_sindrlia_forma_botului = models.ForeignKey('nomenclatoare.TipBotSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (forma botului)', related_name='invelitoare_turn')
    invelitoare_turn_sindrila_cu_tesitura = models.BooleanField(default=False, verbose_name='Șindrila cu teșitură')
    invelitoare_turn_sindrlia_prelucrare = models.ForeignKey('nomenclatoare.TipPrelucrareSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (prelucrare)', related_name='invelitoare_turn')
    invelitoare_turn_sindrlia_esenta_lemnoasa = models.ForeignKey('nomenclatoare.EsentaLemnoasa', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (esență lemnoasă)', related_name='invelitoare_turn_sindrlia_esenta')
    invelitoare_turn_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    # Finisaje -  Închidere tambur turn

    inchidere_tambur_turn_material = models.ForeignKey('nomenclatoare.FinisajExterior', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Material', related_name='inchidere_tambur')
    inchidere_tambur_turn_sindrila_lungime = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (lungime)')
    inchidere_tambur_turn_sindrila_latime_medie = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (lățime medie)')
    inchidere_tambur_turn_sindrila_grosime_medie = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (grosime medie)')
    inchidere_tambur_turn_sindrila_pasul_latuirii = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (pasul lățuirii)')
    inchidere_tambur_turn_sindrila_pasul_baterii = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (pasul baterii)')
    inchidere_tambur_turn_sindrila_numar_straturi = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (număr straturi)')
    inchidere_tambur_turn_sindrila_cu_horj = models.BooleanField(default=False, verbose_name='Șindrila cu horj')
    inchidere_tambur_turn_sindrlia_tipul_de_batere = models.ForeignKey('nomenclatoare.TipBatereSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (tipul de batere)', related_name='inchidere_tambur_turn')
    inchidere_tambur_turn_sindrlia_tipul_prindere = models.ForeignKey('nomenclatoare.TipPrindereSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (tipul de prindere)', related_name='inchidere_tambur_turn')
    inchidere_tambur_turn_sindrlia_forma_botului = models.ForeignKey('nomenclatoare.TipBotSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (forma botului)', related_name='inchidere_tambur_turn')
    inchidere_tambur_turn_sindrila_cu_tesitura = models.BooleanField(default=False, verbose_name='Șindrila cu teșitură')
    inchidere_tambur_turn_sindrlia_prelucrare = models.ForeignKey('nomenclatoare.TipPrelucrareSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (prelucrare)', related_name='inchidere_tambur_turn')
    inchidere_tambur_turn_sindrlia_esenta_lemnoasa = models.ForeignKey('nomenclatoare.EsentaLemnoasa', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (esență lemnoasă)', related_name='inchidere_tambur_turn_sindrlia_esenta')
    inchidere_tambur_turn_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    # Finisaje -  Învelitoare turle
    invelitoare_turle_material = models.ManyToManyField('nomenclatoare.MaterialInvelitoareTurle', blank=True, verbose_name='Material')
    invelitoare_turle_sindrila_lungime = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (lungime)')
    invelitoare_turle_sindrila_latime_medie = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (lățime medie)')
    invelitoare_turle_sindrila_grosime_medie = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (grosime medie)')
    invelitoare_turle_sindrila_pasul_latuirii = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (pasul lățuirii)')
    invelitoare_turle_sindrila_pasul_baterii = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (pasul baterii)')
    invelitoare_turle_sindrila_numar_straturi = models.IntegerField(null=True, blank=True, verbose_name='Șindrila (număr straturi)')
    invelitoare_turle_sindrila_cu_horj = models.BooleanField(default=False, verbose_name='Șindrila cu horj')
    invelitoare_turle_sindrlia_tipul_de_batere = models.ForeignKey('nomenclatoare.TipBatereSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (tipul de batere)', related_name='invelitoare_turle')
    invelitoare_turle_sindrlia_tipul_prindere = models.ForeignKey('nomenclatoare.TipPrindereSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (tipul de prindere)', related_name='invelitoare_turle')
    invelitoare_turle_sindrlia_forma_botului = models.ForeignKey('nomenclatoare.TipBotSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (forma botului)', related_name='invelitoare_turle')
    invelitoare_turle_sindrila_cu_tesitura = models.BooleanField(default=False, verbose_name='Șindrila cu teșitură')
    invelitoare_turle_sindrlia_prelucrare = models.ForeignKey('nomenclatoare.TipPrelucrareSindrila', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (prelucrare)', related_name='invelitoare_turle')
    invelitoare_turle_sindrlia_esenta_lemnoasa = models.ForeignKey('nomenclatoare.EsentaLemnoasa', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șindrila (esență lemnoasă)', related_name='invelitoare_turle_sindrlia_esenta')
    invelitoare_turle_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')


    # Interventii arhitecturale vizibile in timp

    invelitoare_actuala_an  = models.IntegerField(null=True, blank=True, verbose_name='An montaj')
    invelitoare_actuala_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    interventii_invelitoare_etape_anterioare_vizibile = models.BooleanField(default=False)
    interventii_invelitoare_sindrila_pasul_latuirii = models.IntegerField(null=True, blank=True)
    interventii_invelitoare_sindrila_numar_straturi = models.IntegerField(null=True, blank=True)
    interventii_invelitoare_sindrila_cu_horj = models.BooleanField(default=False)
    interventii_invelitoare_sindrlia_tipul_de_batere = models.ForeignKey('nomenclatoare.TipBatereSindrila', null=True, blank=True, on_delete=models.SET_NULL, related_name='interventii_invelitoare')
    interventii_invelitoare_sindrlia_forma_botului = models.ForeignKey('nomenclatoare.TipBotSindrila', null=True, blank=True, on_delete=models.SET_NULL, related_name='interventii_invelitoare')
    interventii_invelitoare_sindrila_cu_tesitura = models.BooleanField(default=False)
    interventii_invelitoare_sindrlia_esenta_lemnoasa = models.ForeignKey('nomenclatoare.EsentaLemnoasa', null=True, blank=True, on_delete=models.SET_NULL, related_name='interventii_invelitoare')
    interventii_invelitoare_alte_tipuri_invelitoare = RichTextField(features=[], null=True, blank=True, verbose_name='Alte tipuri')
    interventii_invelitoare_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    localizare_panels = [
       MultiFieldPanel([
            FieldPanel("amplasament"),],
            heading = 'amplasament',
            classname='collapsible collapsed'
        ),
       MultiFieldPanel([
            FieldPanel("topografie"),],
            heading = 'topografie',
            classname='collapsible collapsed'
        ),
       MultiFieldPanel([
            FieldPanel("toponim"),],
            heading = 'toponim',
            classname='collapsible collapsed'
        ),
       MultiFieldPanel([
            FieldPanel("toponim_sursa"),],
            heading = 'toponim_sursa',
            classname='collapsible collapsed'
        ),
       MultiFieldPanel([
            FieldPanel("relatia_cu_cimitirul"),],
            heading = 'relatia_cu_cimitirul',
            classname='collapsible collapsed'
        ),
       MultiFieldPanel([
            FieldPanel("peisagistica_sitului", widget=forms.CheckboxSelectMultiple),],
            heading = 'peisagistica_sitului',
            classname='collapsible collapsed'
        ),
       MultiFieldPanel([
            FieldPanel("observatii"),],
            heading = 'observatii',
            classname='collapsible collapsed'
        ),
    ]

    ansamblu_panels = [
        InlinePanel('elemente_ansamblu_construit', label="element arhitectural", classname="collapsible collapsed "),
        InlinePanel('elemente_importante_ansamblu_construit', label="Alte componente importante ale sitului "),
    ]

    arhitectura_panels = [
        MultiFieldPanel([
            FieldPanel('materiale', widget=forms.CheckboxSelectMultiple),
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
                FieldPanel('masa_altar_material_picior'),
                FieldPanel('masa_altar_material_blat'),
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
                FieldPanel('bolta_peste_pronaos_material', widget=forms.CheckboxSelectMultiple),
                FieldPanel('bolta_peste_pronaos_tipul_de_arc', widget=forms.CheckboxSelectMultiple),
                FieldPanel('bolta_peste_pronaos_observatii'),
                FieldPanel('bolta_peste_naos'),
                FieldPanel('bolta_peste_naos_material', widget=forms.CheckboxSelectMultiple),
                FieldPanel('bolta_peste_naos_tipul_de_arc', widget=forms.CheckboxSelectMultiple),
                FieldPanel('bolta_peste_naos_observatii'),
                FieldPanel('bolta_peste_altar'),
                FieldPanel('bolta_peste_altar_tip'),
                FieldPanel('bolta_peste_altar_material', widget=forms.CheckboxSelectMultiple),
                FieldPanel('bolta_peste_altar_tipul_de_arc', widget=forms.CheckboxSelectMultiple),
                FieldPanel('bolta_peste_altar_observatii'),
            ],
            heading="Bolți",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [ 
                FieldPanel('cor'),
                FieldPanel('cor_material', widget=forms.CheckboxSelectMultiple),
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
                FieldPanel('sarpanta_tip', widget=forms.CheckboxSelectMultiple),
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
                FieldPanel('turle_pozitionare', widget=forms.CheckboxSelectMultiple),
                FieldPanel('turle_numar_goluri'),
                FieldPanel('turle_forma_sarpanta'),
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
            ],
            heading="FUNDAȚIA",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('sistem_in_cheotoare'),
                FieldPanel('sistem_in_cheotoare_observatii'),
            ],
            heading="SISTEM STRUCTURAL AL CORPULUI BISERICII ÎN CHEOTOARE",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('sistem_in_catei'),
                FieldPanel('sistem_in_catei_observatii'),
            ],
            heading="SISTEM STRUCTURAL AL CORPULUI BISERICII ÎN CĂȚEI",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('sistem_mixt'),
            ],
            heading="SISTEM STRUCTURAL AL CORPULUI BISERICII MIXT",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('tiranti_numar'),
                FieldPanel('tiranti_tip'),
                FieldPanel('tiranti_observatii'),
            ],
            heading="Tiranți",
            classname="collapsible collapsed ",
        ),
    ]

    finisaje_panels = [
        MultiFieldPanel(
            [
                FieldPanel('finisaj_exterior_tip', widget=forms.CheckboxSelectMultiple),
                FieldPanel('finisaj_exterior_observatii'),
            ],
            heading="Exterior corp biserică",
            classname="collapsible collapsed ",
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
            ],
            heading="Învelitoare corp biserică",
            classname="collapsible collapsed ",
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
            ],
            heading="Închidere tambur turn",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('invelitoare_turle_material', widget=forms.CheckboxSelectMultiple),
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
            heading="Învelitoare actuală",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [
                FieldPanel('interventii_invelitoare_etape_anterioare_vizibile'),
                FieldPanel('interventii_invelitoare_sindrila_pasul_latuirii'),
                FieldPanel('interventii_invelitoare_sindrila_numar_straturi'),
                FieldPanel('interventii_invelitoare_sindrila_cu_horj'),
                FieldPanel('interventii_invelitoare_sindrlia_tipul_de_batere'),
                FieldPanel('interventii_invelitoare_sindrlia_forma_botului'),
                FieldPanel('interventii_invelitoare_sindrila_cu_tesitura'),
                FieldPanel('interventii_invelitoare_sindrlia_esenta_lemnoasa'),
                FieldPanel('interventii_invelitoare_alte_tipuri_invelitoare'),
                FieldPanel('interventii_invelitoare_observatii'),
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

    edit_handler = TabbedInterface(
        [
            ObjectList(localizare_panels, heading='Localizare/peisaj'),
            ObjectList(ansamblu_panels, heading='Ansamblu construit'),
            ObjectList(arhitectura_panels, heading='Arhitectura bisericii'),
            ObjectList(structura_panels, heading='Structura'),
            ObjectList(finisaje_panels, heading='Finisaje'),
            ObjectList(interventii_panels, heading='Intervenții arhitecturale vizibile în timp'),
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

class Persoana(models.Model):
    nume = models.CharField(max_length=250)
    observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')
    sursa = RichTextField(features=[], null=True, blank=True, verbose_name='Sursa')

    panels = [
        FieldPanel('nume'),
        FieldPanel('observatii'),
        FieldPanel('sursa'),
    ]

    class Meta:
        abstract = True


class Ctitori(Orderable, Persoana):
    page = ParentalKey('IstoricPage', on_delete=models.PROTECT, related_name='ctitori')

class Mesteri(Orderable, Persoana):
    page = ParentalKey('IstoricPage', on_delete=models.PROTECT, related_name='mesteri')

class Zugravi(Orderable, Persoana):
    page = ParentalKey('IstoricPage', on_delete=models.PROTECT, related_name='zugravi')

class Personalitati(Orderable, Persoana):
    page = ParentalKey('IstoricPage', on_delete=models.PROTECT, related_name='personalitati')


class Eveniment(models.Model):
    nume = models.CharField(max_length=250)
    observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        FieldPanel('nume'),
        FieldPanel('observatii'),
    ]

    class Meta:
        abstract = True

class Evenimente(Orderable, Eveniment):
    page = ParentalKey('IstoricPage', on_delete=models.CASCADE, related_name='evenimente')


class MutareBiserica(models.Model):
    localitate = models.ForeignKey('nomenclatoare.Localitate', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_biserici_mutari')
    adresa = models.CharField(max_length=250, null=True, blank=True)
    latitudine = models.FloatField(null=True, blank=True)
    longitudine = models.FloatField(null=True, blank=True)

    observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')
    sursa = RichTextField(features=[], null=True, blank=True, verbose_name='Sursa')

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

class MutariBiserica(Orderable, MutareBiserica):
    page = ParentalKey('IstoricPage', on_delete=models.CASCADE, related_name='mutari')


class PovesteBiserica(models.Model):
    observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')
    sursa = RichTextField(features=[], null=True, blank=True, verbose_name='Sursa')

    panels = [
        FieldPanel('observatii'),
        FieldPanel('sursa'),
    ]

    class Meta:
        abstract = True

class PovestiBiserica(Orderable, PovesteBiserica):
    page = ParentalKey('IstoricPage', on_delete=models.CASCADE, related_name='povesti')

class IstoricPage(Page):
    sursa_datare = models.ManyToManyField('nomenclatoare.SursaDatare', related_name='p_biserici', blank=True)
    an_constructie = models.IntegerField(null=True, blank=True)
    datare_prin_interval_timp = models.CharField(max_length=50, null=True, blank=True)
    datare_secol = models.ForeignKey('nomenclatoare.Secol', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_biserici')
    datare_secol_observatii  = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')
    datare_secol_sursa  = RichTextField(features=[], null=True, blank=True, verbose_name='Sursa')

    studiu_dendocronologic_fisier = models.ForeignKey('wagtaildocs.Document', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Fișier')
    studiu_dendocronologic_autor = models.CharField(max_length=150, null=True, blank=True, verbose_name='Autor')
    studiu_dendocronologic_an = models.IntegerField(null=True, blank=True, verbose_name='An')
    studiu_dendocronologic_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    pisanie_traducere = RichTextField(features=[], null=True, blank=True, verbose_name='Traducere')
    pisanie_secol_observatii  = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')
    pisanie_secol_sursa  = RichTextField(features=[], null=True, blank=True, verbose_name='Sursa')

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


class ValoarePage(Page):
    vechime = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, help_text= "Printr-un algorim definit se va da automat o notă de la 1-5 în funcție de vechimea monumentului si a picturii descrise conform OMCC2682/2003 ETC", verbose_name='Clasa')
    vechime_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    integritate = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, help_text= "Integritate / Autenticitate", verbose_name='Clasa')
    integritate_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    unicitate = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, help_text= "Unicitate / raritate", verbose_name='Clasa')
    unicitate_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    valoare_memoriala = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, help_text= "evenimente, personalități", verbose_name='Clasa')
    valoare_memoriala_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    peisaj_cultural = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, help_text= "Parte definitorie a peisajului cultural al zonei", verbose_name='Clasa')
    peisaj_cultural_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    valoare_sit = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, help_text= "Valoarea sitului împreună cu toate componentele ansamblului din care face parte, ținând cont de integritate, autenticitate, estetică peisageră, biodiversitate, etc. SUBIECTIV", verbose_name='Clasa')
    valoare_sit_observatii = models.TextField(null=True, blank=True, help_text= "Descriere a elementelor valoroase, particulare", verbose_name='Observații')

    estetica = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, help_text= "Estetică / Arhitectură", verbose_name='Clasa')
    estetica_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    mestesug = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, help_text= "Meșteșug (calitatea muncii -  a se vedea golurile dintre lemne (dintre bârne în general dar în special la așezarea elementelor orizontale peste cele verticale))", verbose_name='Clasa')
    mestesug_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    pictura = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, verbose_name='Clasa')
    pictura_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    folosinta_actuala = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, help_text= "Folosință actuală / singura biserică din sat / loc al patrimoniului imaterial", verbose_name='Clasa')
    folosinta_actuala_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    relevanta_actuala = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, help_text= "Relevanța actuală pentru comunitatea locală (prin reprezentanții săi: preot, crâsnic, învățător, familii de bază)", verbose_name='Clasa')
    relevanta_actuala_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    potential = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, help_text= "Potențialul de beneficii aduse comunității locale", verbose_name='Clasa')
    potential_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

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


class ConservarePage(Page):
    # Sit
    sit = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    sit_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    elemente_arhitecturale = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    elemente_arhitecturale_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    alte_elemente_importante = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    alte_elemente_importante_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    vegetatie = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    vegetatie_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    vegetatie_observatii = RichTextField(features=[], null=True, blank=True, help_text="Vegetație invazivă ce poate pune monumentul în pericol", verbose_name='Observații')

    # Structura bisericii
    teren = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    teren_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    teren_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    fundatii = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    fundatii_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    fundatii_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')
    
    talpi = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    talpi_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    talpi_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    corp_biserica = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    corp_biserica_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    corp_biserica_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')
    
    bolti = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    bolti_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    bolti_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')
    
    cosoroabe = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    cosoroabe_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    cosoroabe_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')
    
    sarpanta_peste_corp_biserica = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    sarpanta_peste_corp_biserica_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    sarpanta_peste_corp_biserica_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')
    
    turn = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    turn_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    turn_observatii = RichTextField(features=[], null=True, blank=True, help_text="tarea structurii turnului, inclusiv a tălpilor și a coifului", verbose_name='Observații')

    # Finisaje biserică
    zona_din_jurul_biserici = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    zona_din_jurul_biserici_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    zona_din_jurul_biserici_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    pardoseli_interioare = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    pardoseli_interioare_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    pardoseli_interioare_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    finisaj_exterior = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    finisaj_exterior_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    finisaj_exterior_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    finisaj_pereti_interiori = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    finisaj_pereti_interiori_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    finisaj_pereti_interiori_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    finisaj_tavane_si_bolti = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    finisaj_tavane_si_bolti_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    finisaj_tavane_si_bolti_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    tamplarii = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    tamplarii_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    tamplarii_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')


    invelitoare_sarpanta_si_turn = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    invelitoare_sarpanta_si_turn_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    invelitoare_sarpanta_si_turn_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')


    instalatie_electrica = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    instalatie_electrica_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    instalatie_electrica_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    instalatie_termica = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    instalatie_termica_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    instalatie_termica_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')


    paratraznet = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    paratraznet_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    paratraznet_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')


    # Starea componenta artistică
    strat_pictural = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    strat_pictural_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    strat_pictural_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    obiecte_de_cult = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    obiecte_de_cult_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    obiecte_de_cult_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    mobilier = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    mobilier_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    mobilier_observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')


    subpage_types = []
    promote_panels = []

    sit_panels = [
        MultiFieldPanel(
            [ 
                FieldPanel('sit'),
                FieldPanel('sit_observatii'),
            ],
            heading="Sit",
            classname="collapsible collapsed ",
        ),

        MultiFieldPanel(
            [ 
                FieldPanel('elemente_arhitecturale'),
                FieldPanel('elemente_arhitecturale_observatii'),
            ],
            heading="Elemente arhitecturale",
            classname="collapsible collapsed ",
        ),

        MultiFieldPanel(
            [ 
                FieldPanel('alte_elemente_importante'),
                FieldPanel('alte_elemente_importante_observatii'),
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
            ],
            heading="Finisaj exterior",
            classname="collapsible collapsed ",
        ),
        MultiFieldPanel(
            [   
                FieldRowPanel([
                    FieldPanel('finisaj_pereti_interiori'),
                    FieldPanel('finisaj_pereti_interiori_pericol'),
                    ]),
                FieldPanel('finisaj_pereti_interiori_observatii'),
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
            ObjectList(componenta_artistica_panels, heading='Componenta Artistică'),
        ])

    class Meta:  # noqa

        verbose_name = "Conservare"
        verbose_name_plural = "Conservare"


class ArtisticEtapeIstoriceVizibile(ClusterableModel, Orderable):
    page = ParentalKey('ComponentaArtisticaPage', on_delete=models.CASCADE, related_name='etape_istorice_vizibile')

    element = models.ForeignKey('nomenclatoare.ElementBiserica', on_delete=models.SET_NULL, null=True, blank=True)
    datat = models.BooleanField(default=False)
    an = models.IntegerField(null=True, blank=True)
    interventie_neconforma = models.BooleanField(default=False)
    sursa = RichTextField(features=[], null=True, blank=True)
    observatii = RichTextField(features=[], null=True, blank=True, verbose_name='Observații')

    panels = [
        FieldPanel('element'),
        FieldPanel('datat'),
        FieldPanel('an'),
        FieldPanel('interventie_neconforma'),
        FieldPanel('sursa'),
        FieldPanel('observatii'),
    ]


class ComponentaArtisticaPage(Page):
    proscomidie = models.BooleanField(default=False, verbose_name="Proscomidie în exteriorul altarului")
    suport_proscomidie = models.ManyToManyField('nomenclatoare.SuportPictura', blank=True)

    elemente_sculptate = models.BooleanField(default=False, verbose_name="Elemente sculptate / decoruri în biserică")
    elemente_observatii = RichTextField(features=[], null=True, blank=True, verbose_name="Observații")

    alte_icoane_vechi = models.BooleanField(default=False, verbose_name="Alte icoane vechi")
    alte_icoane_vechi_observatii = RichTextField(features=[], null=True, blank=True, verbose_name="Observații")

    obiecte_de_cult = models.ManyToManyField('nomenclatoare.ObiectCult', verbose_name="Obiecte de cult", blank=True)
    obiecte_de_cult_observatii = RichTextField(features=[], null=True, blank=True, verbose_name="Observații")

    mobiliere = models.ManyToManyField('nomenclatoare.Material', verbose_name="Mobilier", blank=True)
    mobiliere_observatii = RichTextField(features=[], null=True, blank=True, verbose_name="Observații")

    obiecte_instrainate = models.BooleanField(default=False, verbose_name="Obiecte de cult înstrăinate")
    obiecte_instrainate_observatii = RichTextField(features=[], null=True, blank=True, verbose_name="Observații")



    # Pictură exterioară aplicată
    # Pictură interioară aplicată


    # Iconostasul  (dintre naos și altar)
    iconostas_naos_altar_tip = models.ForeignKey('nomenclatoare.TipIconostas',verbose_name='Tip', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_iconostasuri_naos_altar')
    iconostas_naos_altar_numar_intrari =  models.IntegerField(verbose_name='Număr intrări',null=True, blank=True)
    iconostas_naos_altar_tehnica = models.ManyToManyField('nomenclatoare.FinisajIconostas',verbose_name='Tehnică', related_name='p_iconostasuri_naos_altar', blank=True)
    iconostas_naos_altar_registre = models.ManyToManyField('nomenclatoare.RegistruIconostas',verbose_name='Registru', related_name='p_iconostasuri_naos_altar', blank=True)
    iconostas_naos_altar_tip_usi = models.ManyToManyField('nomenclatoare.TipUsiIconostas',verbose_name='Tip uși', related_name='p_iconostasuri_naos_altar', blank=True)
    iconostas_naos_altar_observatii = RichTextField(features=[], null=True, blank=True, verbose_name="Observații")

    iconostas_naos_altar_materiale = models.ManyToManyField('nomenclatoare.Material',verbose_name='Material', blank=True, related_name='p_iconostasuri_naos_altar')

    # Iconostasul  (dintre pronaos și naos)
    iconostas_pronaos_naos_tip = models.ForeignKey('nomenclatoare.TipIconostas',verbose_name='Tip', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_iconostasuri_pronaos_naos')
    iconostas_pronaos_naos_material = models.ForeignKey('nomenclatoare.Material',verbose_name='Material', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_iconostasuri_pronaos_naos')
    iconostas_pronaos_naos_numar_intrari =  models.IntegerField(verbose_name='Număr intrări',null=True, blank=True)
    iconostas_pronaos_naos_tehnica = models.ManyToManyField('nomenclatoare.FinisajIconostas', verbose_name='Tehnica',related_name='p_iconostasuri_pronaos_naos', blank=True)
    iconostas_pronaos_naos_observatii = RichTextField(features=[], null=True, blank=True, verbose_name="Observații")

    # Altar
    altar_placa_mesei = models.ManyToManyField('nomenclatoare.Material',verbose_name='Placa mesei', blank=True, related_name='p_placa_mesei')
    altar_piciorul_mesei = models.ManyToManyField('nomenclatoare.Material',verbose_name='Piciorul mesei', blank=True, related_name='p_piciorul_mesei')
    altar_decor = models.ForeignKey('nomenclatoare.FinisajIconostas', verbose_name = "Decor", on_delete=models.SET_NULL, null=True, blank=True, related_name='p_decoruri_altar')
    altar_observatii = RichTextField(features=[], null=True, blank=True, verbose_name="Observații")


    # Pictura Exterioara
    pictura_exterioara_localizare = models.ForeignKey('nomenclatoare.LocalizarePictura', on_delete=models.SET_NULL, null=True, blank=True, related_name='p_localizari_exterioare', verbose_name='Proporția de suprafață acoperită')
    pictura_exterioara_localizare_observatii = RichTextField(features=[], null=True, blank=True, verbose_name="Observații")
    pictura_exterioara_tehnica = models.ForeignKey('nomenclatoare.TehnicaPictura', on_delete=models.SET_NULL, null=True, blank=True, related_name='p_localizari_exterioare', verbose_name='Tehnică')
    pictura_exterioara_suport = models.ManyToManyField('nomenclatoare.SuportPictura', blank=True, related_name='p_localizari_exterioare', verbose_name='Suport')
    pictura_exterioara_numar_straturi_pictura = models.IntegerField(null=True, blank=True, verbose_name='Număr straturi')

    pictura_exterioara_sursa_datare = models.ManyToManyField('nomenclatoare.SursaDatare', related_name='p_componente_artistice_exterioare', blank=True, verbose_name='Sursa datare')
    pictura_exterioara_anul_picturii = models.IntegerField(null=True, blank=True, verbose_name='Anul picturii')
    pictura_exterioara_datare_prin_interval_timp = models.CharField(max_length=50, null=True, blank=True, verbose_name='Datare prin interval de timp')
    pictura_exterioara_datare_secol = models.ForeignKey('nomenclatoare.Secol', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_localizari_exterioare', verbose_name='Datare secol')
    pictura_exterioara_datare_observatii = RichTextField(features=[], null=True, blank=True, verbose_name="Observații")

    # Pictura Interioara
    pictura_interioara_localizare = models.ForeignKey('nomenclatoare.LocalizarePictura', verbose_name="Proporția de suprafață acoperită", on_delete=models.SET_NULL, null=True, blank=True, related_name='p_localizari_interioare')
    pictura_interioara_localizare_observatii = RichTextField(features=[], null=True, blank=True, verbose_name="Observatii")
    pictura_interioara_tehnica_pictura = models.ForeignKey('nomenclatoare.TehnicaPictura', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Tehnică')
    pictura_interioara_suport = models.ManyToManyField('nomenclatoare.SuportPictura', blank=True, related_name='p_localizari_interioare', verbose_name='Suport')
    pictura_interioara_numar_straturi_pictura = models.IntegerField(null=True, blank=True, verbose_name='Număr straturi')

    pictura_interioara_sursa_datare = models.ManyToManyField('nomenclatoare.SursaDatare', related_name='p_componente_artistice_interioare', blank=True, verbose_name='Sursa datare')
    pictura_interioara_anul_picturii = models.IntegerField(null=True, blank=True, verbose_name='Anul picturii')
    pictura_interioara_datare_prin_interval_timp = models.CharField(max_length=50, null=True, blank=True, verbose_name='Datare prin interval de timp')
    pictura_interioara_datare_secol = models.ForeignKey('nomenclatoare.Secol', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_localizari_interioare', verbose_name='Datare secol')
    pictura_interioara_datare_observatii = RichTextField(features=[], null=True, blank=True, verbose_name="Observații")

    general_panels = [
        MultiFieldPanel(
                [
                    FieldPanel('proscomidie'),
                    FieldPanel('suport_proscomidie', widget=forms.CheckboxSelectMultiple),
                ],
                heading="Proscomidie",
                classname="collapsible collapsed ",
            ),
        MultiFieldPanel(
                [
                    FieldPanel('elemente_sculptate'),
                    FieldPanel('elemente_observatii'),
                ],
                heading="Elemente Sculptate",
                classname="collapsible collapsed ",
            ),
        MultiFieldPanel(
                [
                    FieldPanel('alte_icoane_vechi'),
                    FieldPanel('alte_icoane_vechi_observatii'),
                ],
                heading="Alte icoane vechi",
                classname="collapsible collapsed ",
            ),
        MultiFieldPanel(
                [
                    FieldPanel('obiecte_de_cult', widget=forms.CheckboxSelectMultiple),
                    FieldPanel('obiecte_de_cult_observatii'),
                ],
                heading="Obiecte de cult",
                classname="collapsible collapsed ",
            ),
        MultiFieldPanel(
                [
                    FieldPanel('mobiliere', widget=forms.CheckboxSelectMultiple),
                    FieldPanel('mobiliere_observatii'),
                ],
                heading="Mobiliere",
                classname="collapsible collapsed ",
            ),
        MultiFieldPanel(
                [
                    FieldPanel('obiecte_instrainate'),
                    FieldPanel('obiecte_instrainate_observatii'),
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
                    FieldPanel('iconostas_naos_altar_materiale', widget=forms.CheckboxSelectMultiple),
                    FieldPanel('iconostas_naos_altar_tehnica', widget=forms.CheckboxSelectMultiple),
                    FieldPanel('iconostas_naos_altar_registre', widget=forms.CheckboxSelectMultiple),
                    FieldPanel('iconostas_naos_altar_tip_usi', widget=forms.CheckboxSelectMultiple),
                    FieldPanel('iconostas_naos_altar_observatii'),
                ],
                heading="",
                classname="collapsible ",
            ),
    ]

    perete_despartitor_panels = [
        MultiFieldPanel(
                [
                    FieldPanel('iconostas_pronaos_naos_tip'),
                    FieldPanel('iconostas_pronaos_naos_material'),
                    FieldPanel('iconostas_pronaos_naos_numar_intrari'),
                    FieldPanel('iconostas_pronaos_naos_tehnica', widget=forms.CheckboxSelectMultiple),
                    FieldPanel('iconostas_pronaos_naos_observatii'),
                ],
                heading="",
                classname="collapsible ",
            ),
    ]

    altar_panels = [
        MultiFieldPanel(
                [
                    FieldPanel('altar_placa_mesei', widget=forms.CheckboxSelectMultiple),
                    FieldPanel('altar_piciorul_mesei', widget=forms.CheckboxSelectMultiple),
                    FieldPanel('altar_decor'),
                    FieldPanel('altar_observatii'),
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
                    FieldPanel('pictura_exterioara_suport', widget=forms.CheckboxSelectMultiple),
                    FieldPanel('pictura_exterioara_numar_straturi_pictura'),
                ],
                heading="",
                classname="collapsible ",
            ),

        MultiFieldPanel(
                [
                    FieldPanel('pictura_exterioara_sursa_datare', widget=forms.CheckboxSelectMultiple),
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
                    FieldPanel('pictura_interioara_suport', widget=forms.CheckboxSelectMultiple),
                    FieldPanel('pictura_interioara_numar_straturi_pictura'),
                ],
                heading="",
                classname="collapsible ",
            ),

        MultiFieldPanel(
                [
                    FieldPanel('pictura_interioara_sursa_datare', widget=forms.CheckboxSelectMultiple),
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
            ObjectList(perete_despartitor_panels, heading='Perete despărțitor (pronaos/naos)'),
            ObjectList(altar_panels, heading='Altar'),
            ObjectList(exterior_panels, heading='Pictură exterioară'),
            ObjectList(interior_panels, heading='Pictură interioară'),
            ObjectList(interventii_panels, heading='Intervenții'),
        ])

    class Meta:  # noqa

        verbose_name = "Componenta Artistică"
        verbose_name_plural = "Componenta Artistică"
