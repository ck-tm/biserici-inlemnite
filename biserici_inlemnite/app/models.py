from django.db import models
from django import forms
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel,
    PageChooserPanel,
    ObjectList,
    TabbedInterface,
    InlinePanel,
    FieldRowPanel
)
from wagtail.search import index

from wagtail.core.models import Orderable, Page
from modelcluster.fields import ParentalKey

from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from wagtailmodelchooser.edit_handlers import ModelChooserPanel



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
        "FinisajPage",
        "ComponentaArtisticaPage",
        "ConservarePage",
        "PatrimoniuPage",
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
    denumire_oberservatii =  RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name="Observații")
    cult = models.ForeignKey('nomenclatoare.CultBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_biserici')
    utilizare = models.ForeignKey('nomenclatoare.UtilizareBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_biserici')
    utilizare_detalii =  RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name="Observații")
    singularitate = models.ForeignKey('nomenclatoare.SingularitateBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_biserici')
    singularitate_detalii =  RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name="Observații")
    functiune = models.ForeignKey('nomenclatoare.FunctiuneBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_biserici')
    functiune_detalii =  RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True)
    functiune_initiala = models.ForeignKey('nomenclatoare.FunctiuneBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_biserici_initiale')
    functiune_initiala_detalii =  RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True)
    proprietate_actuala = models.ForeignKey('nomenclatoare.ProprietateBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_biserici_initiale')
    proprietate_detalii =  RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True)
    proprietar_actual =  RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True)
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
            classname="collapsible ",
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
            classname="collapsible ",
        ),
        FieldPanel("cult"),
        MultiFieldPanel(
            [ 
                FieldPanel("utilizare"),
                FieldPanel("utilizare_detalii"),
            ],
            heading="Utilizare",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [ 
                FieldPanel("singularitate"),
                FieldPanel("singularitate_detalii"),
            ],
            heading="Singularitate",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [ 
                FieldPanel("functiune"),
                FieldPanel("functiune_detalii"),
                FieldPanel("functiune_initiala"),
                FieldPanel("functiune_initiala_detalii"),
            ],
            heading="Funcțiune",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [ 
                FieldPanel("proprietate_actuala"),
                FieldPanel("proprietate_detalii"),
                FieldPanel("proprietar_actual"),
            ],
            heading="Proprietate",
            classname="collapsible ",
        ),
        FieldPanel("inscriere_documente_cadastrale")
    ]
    class Meta:  # noqa

        verbose_name = "Identificare"
        verbose_name_plural = "Identificare"



class ElementAnsambluConstruit(models.Model):
    element = models.ForeignKey('nomenclatoare.ElementAnsambluConstruit', on_delete=models.CASCADE)
    observatii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')

    panels = [
        SnippetChooserPanel('element'),
        FieldPanel('observatii'),
    ]

    class Meta:
        abstract = True


class ElementeAnsambluConstruit(Orderable, ElementAnsambluConstruit):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE, related_name='elemente_ansamblu_construit')


class ElementImportantAnsambluConstruit(models.Model):
    element = models.ForeignKey('nomenclatoare.ElementImportant', on_delete=models.CASCADE)
    observatii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')

    panels = [
        FieldPanel('element'),
        FieldPanel('observatii'),
    ]

    class Meta:
        abstract = True


class ElementeImportanteAnsambluConstruit(Orderable, ElementImportantAnsambluConstruit):
    page = ParentalKey('DescrierePage', on_delete=models.CASCADE, related_name='elemente_importante_ansamblu_construit')


class DescrierePage(Page):
    """
    Capitol: Descriere Biserica
    """

    # Localizare/peisaj
    amplasament = models.ForeignKey('nomenclatoare.AmplasamentBiserica', null=True, blank=True, on_delete=models.SET_NULL)
    topografie = models.ForeignKey('nomenclatoare.TopografieBiserica', null=True, blank=True, on_delete=models.SET_NULL)
    toponim = models.CharField(max_length=150, null=True, blank=True, help_text="denumirea locului")
    toponim_sursa  = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Sursă informații')
    relatia_cu_cimitirul = models.ForeignKey('nomenclatoare.RelatieCimitir', null=True, blank=True, on_delete=models.SET_NULL)
    peisagistica_sitului = models.ManyToManyField('nomenclatoare.PeisagisticaSit', blank=True)
    observatii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True)

    # Ansamblu construit
    elemente = models.ManyToManyField('nomenclatoare.ElementBiserica', help_text="Elemente ansamblu construit", blank=True)
    detalii_elemente = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True)

    elemente_importante = models.ManyToManyField('nomenclatoare.ElementImportant', help_text="Elemente ansamblu construit", blank=True)
    detalii_elemente_importante = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True)

    
    # Arhitectura bisericii
    planimetria_bisericii = models.ForeignKey('nomenclatoare.Planimetrie', null=True, blank=True, on_delete=models.SET_NULL)
    gabarit_exterior_al_talpilor = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', help_text='o schiță a planului tălpilor / elevației /  turnului / triunghiului șarpantei')
    materiale = models.ManyToManyField('nomenclatoare.Material', help_text="Materiale folosite in construcția bisericii", blank=True)
    detalii_materiale = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, help_text="Materialele care compun structura de rezistentă a bisericii")

    # Elemente arhitecturale

    turn_dimensiune = models.ForeignKey('nomenclatoare.DimensiuneTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Dimensiune')
    turn_tip = models.ForeignKey('nomenclatoare.TipTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Tip')
    turn_numar = models.IntegerField(null=True, blank=True, verbose_name='Număr de turnuri')
    turn_decor = models.ForeignKey('nomenclatoare.DecorTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Decor')
    turn_plan = models.ForeignKey('nomenclatoare.PlanTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Plan')
    turn_amplasare = models.ForeignKey('nomenclatoare.AmplasareTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Amplasare')
    turn_galerie = models.ForeignKey('nomenclatoare.GalerieTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Galerie')
    turn_numar_arcade = models.IntegerField(null=True, blank=True, verbose_name='Număr arcade Turn deschis')
    turn_numar_arcade_detalii =RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Detalii arcade Turn deschis')
    turn_asezare_talpi  = models.ForeignKey('nomenclatoare.AsezareTalpaTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Așezarea tălpilor turnului în legătură cu corpul bisericii')
    turn_relatie_talpi  = models.ForeignKey('nomenclatoare.RelatieTalpaTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Relația dintre tălpile turnului')
    turn_numar_talpi = models.IntegerField(null=True, blank=True, verbose_name='Număr de tălpi')
    turn_observatii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name="Observații")

    clopote_an = models.IntegerField(null=True, blank=True, verbose_name='An')
    clopote_inscriptie =RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Inscripție')

    sarpanta_tip  = models.ManyToManyField('nomenclatoare.TipSarpanta', blank=True, verbose_name='Tip')
    sarpanta_veche_nefolosita = models.BooleanField(default=False, verbose_name='Veche nefolosită sub șarpanta actuală')
    sarpanta_numar_turnulete  = models.IntegerField(null=True, blank=True, verbose_name='Număr turnulețe decorative')
    sarpanta_numar_cruci  = models.IntegerField(null=True, blank=True, verbose_name='Număr cruci')
    sarpanta_material_cruci  = models.ForeignKey('nomenclatoare.Material', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Material cruci', related_name="p_material_cruci")
    sarpanta_detalii =RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')

    numar_accese_pridvor  = models.IntegerField(null=True, blank=True, verbose_name='Număr accese pridvor')
    numar_accese_pridvor_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații Pridvor')
    numar_accese_pronaos  = models.IntegerField(null=True, blank=True, verbose_name='Număr accese pronaos')
    numar_accese_pronaos_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații Pronaos')
    numar_accese_naos  = models.IntegerField(null=True, blank=True, verbose_name='Număr accese naos')
    numar_accese_naos_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații Naos')
    numar_accese_altar  = models.IntegerField(null=True, blank=True, verbose_name='Număr accese altar')
    numar_accese_altar_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații Altar')


    numar_geamuri_pridvor  = models.IntegerField(null=True, blank=True, verbose_name='Număr geamuri pridvor')
    numar_geamuri_pridvor_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații Pridvor')
    numar_geamuri_pronaos  = models.IntegerField(null=True, blank=True, verbose_name='Număr geamuri pronaos')
    numar_geamuri_pronaos_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații Pronaos')
    numar_geamuri_naos  = models.IntegerField(null=True, blank=True, verbose_name='Număr geamuri naos')
    numar_geamuri_naos_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații Naos')
    numar_geamuri_altar  = models.IntegerField(null=True, blank=True, verbose_name='Număr geamuri altar')
    numar_geamuri_altar_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații Altar')


    oachiesi_aerisitoare = models.BooleanField(default=False, verbose_name='Ochieși / Aerisitoare ')
    oachiesi_aerisitoare_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')


    
    bolta_peste_pronaos  = models.ForeignKey('nomenclatoare.TipBoltaPronaos', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Boltă peste pronaos', related_name='p_biserici_bolta_peste_pronaos')
    bolta_peste_pronaos_material = models.ManyToManyField('nomenclatoare.Material', blank=True, related_name='p_biserici_bolta_peste_pronaos')
    bolta_peste_pronaos_tipul_de_arc = models.ManyToManyField('nomenclatoare.TipArcBolta', blank=True, related_name='p_biserici_bolta_peste_pronaos')
    bolta_peste_pronaos_observatii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')

    bolta_peste_naos  = models.ForeignKey('nomenclatoare.TipBoltaPronaos', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Boltă peste naos', related_name='p_biserici_bolta_peste_naos')
    bolta_peste_naos_material = models.ManyToManyField('nomenclatoare.Material', blank=True, related_name='p_biserici_bolta_peste_naos')
    bolta_peste_naos_tipul_de_arc = models.ManyToManyField('nomenclatoare.TipArcBolta', blank=True, related_name='p_biserici_bolta_peste_naos')
    bolta_peste_naos_observatii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')

    bolta_peste_altar  = models.ForeignKey('nomenclatoare.BoltaPesteAltar', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Boltă peste altar', related_name='p_biserici_bolta_peste_altar')
    bolta_peste_altar_tip  = models.ForeignKey('nomenclatoare.TipBoltaPesteAltar', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Tip', related_name='p_biserici')
    bolta_peste_altar_material = models.ManyToManyField('nomenclatoare.Material', blank=True, related_name='p_biserici_bolta_peste_altar', verbose_name='Material')
    bolta_peste_altar_tipul_de_arc = models.ManyToManyField('nomenclatoare.TipArcBolta', blank=True, related_name='p_biserici_bolta_peste_altar', verbose_name='Tipul de arc')
    bolta_peste_altar_observatii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')

    cor = models.BooleanField(default=False)
    cor_material = models.ManyToManyField('nomenclatoare.Material', blank=True, related_name='p_biserici_cor')
    cor_observatii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')

    solee = models.BooleanField(default=False)
    solee_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')

    masa_altar_material_picior  = models.ForeignKey('nomenclatoare.Material', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Materialul piciorului', related_name='p_masa_altar_picior')
    masa_altar_material_blat  = models.ForeignKey('nomenclatoare.Material', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Materialul blatului', related_name='p_masa_altar_blat')
    masa_altar_observatii =  RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')

    # Structura
    fundatia  = models.ForeignKey('nomenclatoare.TipFundatie', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Fundația', related_name='p_biserici')
    sistem_in_cheotoare  = models.ForeignKey('nomenclatoare.TipStructuraCheotoare', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Sistem structural al corpului bisericii În cheotoare', related_name='p_biserici')
    sistem_in_catei  = models.ForeignKey('nomenclatoare.TipStructuraCatei', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Sistem structural al corpului bisericii În căței', related_name='p_biserici')
    sistem_mixt = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Sistem structural al corpului bisericii mixt')


    subpage_types = []
    promote_panels = []

    content_panels = []
    localizare_panels = [
       FieldPanel("amplasament"),
       FieldPanel("topografie"),
       FieldPanel("toponim"),
       FieldPanel("toponim_sursa"),
       FieldPanel("relatia_cu_cimitirul"),
       FieldPanel("peisagistica_sitului", widget=forms.CheckboxSelectMultiple),
       FieldPanel("observatii"),
    ]

    ansamblu_panels = [
        InlinePanel('elemente_ansamblu_construit', label="Elemente arhitecturale", classname="collapsible "),
        InlinePanel('elemente_importante_ansamblu_construit', label="Alte elemente importante"),
    ]

    arhitectura_panels = [
        MultiFieldPanel([
            FieldPanel('materiale', widget=forms.CheckboxSelectMultiple),
            FieldPanel('detalii_materiale'),
            ],
            heading="Materiale",
            classname="collapsible"
        ),
        FieldPanel('planimetria_bisericii'),
        ImageChooserPanel('gabarit_exterior_al_talpilor'),
        MultiFieldPanel(
            [ 
                FieldPanel('turn_dimensiune'),
                FieldPanel('turn_tip'),
                FieldPanel('turn_numar'),
                FieldPanel('turn_decor'),
                FieldPanel('turn_plan'),
                FieldPanel('turn_amplasare'),
                FieldPanel('turn_galerie'),
                FieldPanel('turn_numar_arcade'),
                FieldPanel('turn_numar_arcade_detalii'),
                FieldPanel('turn_asezare_talpi'),
                FieldPanel('turn_relatie_talpi'),
                FieldPanel('turn_numar_talpi'),
                FieldPanel('turn_observatii'),
            ],
            heading="Turn",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [ 
                FieldPanel('clopote_an'),
                FieldPanel('clopote_inscriptie'),
            ],
            heading="Clopote",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [ 
                FieldPanel('sarpanta_tip', widget=forms.CheckboxSelectMultiple),
                FieldPanel('sarpanta_veche_nefolosita'),
                FieldPanel('sarpanta_numar_turnulete'),
                FieldPanel('sarpanta_numar_cruci'),
                FieldPanel('sarpanta_material_cruci'),
                FieldPanel('sarpanta_detalii'),
            ],
            heading="Șarpanta",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [ 
                FieldPanel('numar_accese_pridvor'),
                FieldPanel('numar_accese_pridvor_detalii'),
                FieldPanel('numar_accese_pronaos'),
                FieldPanel('numar_accese_pronaos_detalii'),
                FieldPanel('numar_accese_naos'),
                FieldPanel('numar_accese_naos_detalii'),
                FieldPanel('numar_accese_altar'),
                FieldPanel('numar_accese_altar_detalii'),
            ],
            heading="Număr accese",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [ 
                FieldPanel('numar_geamuri_pridvor'),
                FieldPanel('numar_geamuri_pridvor_detalii'),
                FieldPanel('numar_geamuri_pronaos'),
                FieldPanel('numar_geamuri_pronaos_detalii'),
                FieldPanel('numar_geamuri_naos'),
                FieldPanel('numar_geamuri_naos_detalii'),
                FieldPanel('numar_geamuri_altar'),
                FieldPanel('numar_geamuri_altar_detalii'),
            ],
            heading="Număr geamuri",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [ 
                FieldPanel('oachiesi_aerisitoare'),
                FieldPanel('oachiesi_aerisitoare_detalii'),
            ],
            heading="Oachiesi / Aerisitoare",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [ 
                FieldPanel('bolta_peste_pronaos'),
                FieldPanel('bolta_peste_pronaos_material', widget=forms.CheckboxSelectMultiple),
                FieldPanel('bolta_peste_pronaos_tipul_de_arc', widget=forms.CheckboxSelectMultiple),
                FieldPanel('bolta_peste_pronaos_observatii'),
            ],
            heading="Bolta peste pronaos",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [ 
                FieldPanel('bolta_peste_naos'),
                FieldPanel('bolta_peste_naos_material', widget=forms.CheckboxSelectMultiple),
                FieldPanel('bolta_peste_naos_tipul_de_arc', widget=forms.CheckboxSelectMultiple),
                FieldPanel('bolta_peste_naos_observatii'),
            ],
            heading="Bolta peste naos",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [ 
                FieldPanel('bolta_peste_altar'),
                FieldPanel('bolta_peste_altar_tip'),
                FieldPanel('bolta_peste_altar_material', widget=forms.CheckboxSelectMultiple),
                FieldPanel('bolta_peste_altar_tipul_de_arc', widget=forms.CheckboxSelectMultiple),
                FieldPanel('bolta_peste_altar_observatii'),
            ],
            heading="Bolta peste altar",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [ 
                FieldPanel('cor'),
                FieldPanel('cor_material', widget=forms.CheckboxSelectMultiple),
                FieldPanel('cor_observatii'),
            ],
            heading="Cor",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [ 
                FieldPanel('solee'),
                FieldPanel('solee_detalii'),
            ],
            heading="Solee",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [ 
                FieldPanel('masa_altar_material_picior'),
                FieldPanel('masa_altar_material_blat'),
                FieldPanel('masa_altar_observatii'),
            ],
            heading="Masă altar",
            classname="collapsible ",
        ),
    ]


    structura_panels = [
        FieldPanel('fundatia'),
        FieldPanel('sistem_in_cheotoare'),
        FieldPanel('sistem_in_catei'),
        FieldPanel('sistem_mixt'),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(localizare_panels, heading='Localizare/peisaj'),
            ObjectList(ansamblu_panels, heading='Ansamblu construit'),
            ObjectList(arhitectura_panels, heading='Arhitectura bisericii'),
            ObjectList(structura_panels, heading='Structura'),
            # ObjectList(localizare_panels, heading='Finisaje'),
            # ObjectList(localizare_panels, heading='Intervenții arhitecturale vizibile în timp'),

            # ObjectList(banner_panels, heading="Banner Settings"),
            # ObjectList(Page.promote_panels, heading='Promotional Stuff'),
            # ObjectList(Page.settings_panels, heading='Settings Stuff'),
        ]
    )

    class Meta:  # noqa

        verbose_name = "Capitol Descriere"
        verbose_name_plural = "Capitole Descriere"


class IstoricPage(Page):
    subpage_types = []
    promote_panels = []

    content_panels = []

    class Meta:  # noqa

        verbose_name = "Istoric"
        verbose_name_plural = "Istoric"


class PatrimoniuPage(Page):
    subpage_types = []
    promote_panels = []

    content_panels = []

    class Meta:  # noqa

        verbose_name = "Patrimoniu"
        verbose_name_plural = "Patrimoniu"


class ConservarePage(Page):
    # Sit
    sit = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    sit_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')

    elemente_arhitecturale = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    elemente_arhitecturale_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')

    alte_elemente_importante = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    alte_elemente_importante_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')

    vegetatie = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    vegetatie_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    vegetatie_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, help_text="Vegetație invazivă ce poate pune monumentul în pericol", verbose_name='Observații')

    # Structura bisericii
    teren = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    teren_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    teren_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')

    fundatii = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    fundatii_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    fundatii_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')
    
    talpi = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    talpi_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    talpi_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')

    corp_biserica = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    corp_biserica_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    corp_biserica_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')
    
    bolti = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    bolti_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    bolti_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')
    
    cosoroabe = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    cosoroabe_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    cosoroabe_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')
    
    sarpanta_peste_corp_biserica = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    sarpanta_peste_corp_biserica_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    sarpanta_peste_corp_biserica_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')
    
    turn = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    turn_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    turn_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, help_text="tarea structurii turnului, inclusiv a tălpilor și a coifului", verbose_name='Observații')

    # Finisaje biserică
    zona_din_jurul_biserici = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    zona_din_jurul_biserici_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    zona_din_jurul_biserici_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')

    pardoseli_interioare = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    pardoseli_interioare_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    pardoseli_interioare_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')

    finisaj_exterior = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    finisaj_exterior_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    finisaj_exterior_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')

    finisaj_pereti_interiori = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    finisaj_pereti_interiori_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    finisaj_pereti_interiori_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')

    finisaj_tavane_si_bolti = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    finisaj_tavane_si_bolti_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    finisaj_tavane_si_bolti_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')

    tamplarii = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    tamplarii_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    tamplarii_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')


    invelitoare_sarpanta_si_turn = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    invelitoare_sarpanta_si_turn_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    invelitoare_sarpanta_si_turn_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')


    instalatie_electrica = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    instalatie_electrica_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    instalatie_electrica_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')

    instalatie_termica = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    instalatie_termica_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    instalatie_termica_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')


    paratraznet = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    paratraznet_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    paratraznet_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')


    # Starea componenta artistică
    strat_pictural = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    strat_pictural_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    strat_pictural_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')

    obiecte_de_cult = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    obiecte_de_cult_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    obiecte_de_cult_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')

    mobilier = models.IntegerField(choices=NR15, null=True, blank=True, verbose_name='Stare')
    mobilier_pericol = models.BooleanField(default=False, verbose_name='Pericol')
    mobilier_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Observații')


    subpage_types = []
    promote_panels = []

    sit_panels = [
        MultiFieldPanel(
            [ 
                FieldPanel('sit'),
                FieldPanel('sit_detalii'),
            ],
            heading="Sit",
            classname="collapsible ",
        ),

        MultiFieldPanel(
            [ 
                FieldPanel('elemente_arhitecturale'),
                FieldPanel('elemente_arhitecturale_detalii'),
            ],
            heading="Elemente arhitecturale",
            classname="collapsible ",
        ),

        MultiFieldPanel(
            [ 
                FieldPanel('alte_elemente_importante'),
                FieldPanel('alte_elemente_importante_detalii'),
            ],
            heading="Alte elemente importante",
            classname="collapsible ",
        ),

        MultiFieldPanel(
            [   
                FieldRowPanel([
                    FieldPanel('vegetatie'),
                    FieldPanel('vegetatie_pericol'),
                    ]),
                FieldPanel('vegetatie_detalii'),
            ],
            heading="Vegetație",
            classname="collapsible ",
        ),
    ]

    structura_panels = [
        MultiFieldPanel(
            [   
                FieldRowPanel([
                    FieldPanel('teren'),
                    FieldPanel('teren_pericol'),
                    ]),
                FieldPanel('teren_detalii'),
            ],
            heading="Teren",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [   
                FieldRowPanel([
                    FieldPanel('fundatii'),
                    FieldPanel('fundatii_pericol'),
                    ]),
                FieldPanel('fundatii_detalii'),
            ],
            heading="Fundații",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [   
                FieldRowPanel([
                    FieldPanel('talpi'),
                    FieldPanel('talpi_pericol'),
                    ]),
                FieldPanel('talpi_detalii'),
            ],
            heading="Tălpi",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [   
                FieldRowPanel([
                    FieldPanel('corp_biserica'),
                    FieldPanel('corp_biserica_pericol'),
                    ]),
                FieldPanel('corp_biserica_detalii'),
            ],
            heading="Corp biserică",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [   
                FieldRowPanel([
                    FieldPanel('bolti'),
                    FieldPanel('bolti_pericol'),
                    ]),
                FieldPanel('bolti_detalii'),
            ],
            heading="Bolți",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [   
                FieldRowPanel([
                    FieldPanel('cosoroabe'),
                    FieldPanel('cosoroabe_pericol'),
                    ]),
                FieldPanel('cosoroabe_detalii'),
            ],
            heading="Cosoroabe",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [   
                FieldRowPanel([
                    FieldPanel('sarpanta_peste_corp_biserica'),
                    FieldPanel('sarpanta_peste_corp_biserica_pericol'),
                    ]),
                FieldPanel('sarpanta_peste_corp_biserica_detalii'),
            ],
            heading="Șarpantă corp biserică",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [   
                FieldRowPanel([
                    FieldPanel('turn'),
                    FieldPanel('turn_pericol'),
                    ]),
                FieldPanel('turn_detalii'),
            ],
            heading="Turn",
            classname="collapsible ",
        ),
        
    ]

    finisaje_panels = [
        MultiFieldPanel(
            [   
                FieldRowPanel([
                    FieldPanel('zona_din_jurul_biserici'),
                    FieldPanel('zona_din_jurul_biserici_pericol'),
                    ]),
                FieldPanel('zona_din_jurul_biserici_detalii'),
            ],
            heading="Zona din jurul biserici",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [   
                FieldRowPanel([
                    FieldPanel('pardoseli_interioare'),
                    FieldPanel('pardoseli_interioare_pericol'),
                    ]),
                FieldPanel('pardoseli_interioare_detalii'),
            ],
            heading="Pardoseli interioare",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [   
                FieldRowPanel([
                    FieldPanel('finisaj_exterior'),
                    FieldPanel('finisaj_exterior_pericol'),
                    ]),
                FieldPanel('finisaj_exterior_detalii'),
            ],
            heading="Finisaj exterior",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [   
                FieldRowPanel([
                    FieldPanel('finisaj_pereti_interiori'),
                    FieldPanel('finisaj_pereti_interiori_pericol'),
                    ]),
                FieldPanel('finisaj_pereti_interiori_detalii'),
            ],
            heading="Finisaj pereți interiori",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [   
                FieldRowPanel([
                    FieldPanel('finisaj_tavane_si_bolti'),
                    FieldPanel('finisaj_tavane_si_bolti_pericol'),
                    ]),
                FieldPanel('finisaj_tavane_si_bolti_detalii'),
            ],
            heading="Finisaj tavane și bolți",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [   
                FieldRowPanel([
                    FieldPanel('tamplarii'),
                    FieldPanel('tamplarii_pericol'),
                    ]),
                FieldPanel('tamplarii_detalii'),
            ],
            heading="Tâmplării",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [   
                FieldRowPanel([
                    FieldPanel('invelitoare_sarpanta_si_turn'),
                    FieldPanel('invelitoare_sarpanta_si_turn_pericol'),
                    ]),
                FieldPanel('invelitoare_sarpanta_si_turn_detalii'),
            ],
            heading="Învelitoare șarpantă și turn",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [   
                FieldRowPanel([
                    FieldPanel('instalatie_electrica'),
                    FieldPanel('instalatie_electrica_pericol'),
                    ]),
                FieldPanel('instalatie_electrica_detalii'),
            ],
            heading="Instalație electrică",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [   
                FieldRowPanel([
                    FieldPanel('instalatie_termica'),
                    FieldPanel('instalatie_termica_pericol'),
                    ]),
                FieldPanel('instalatie_termica_detalii'),
            ],
            heading="Instalație termică",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [   
                FieldRowPanel([
                    FieldPanel('paratraznet'),
                    FieldPanel('paratraznet_pericol'),
                    ]),
                FieldPanel('paratraznet_detalii'),
            ],
            heading="Paratrăznet",
            classname="collapsible ",
        ),

    ]

    componenta_artistica_panels = [
        MultiFieldPanel(
            [   
                FieldRowPanel([
                    FieldPanel('strat_pictural'),
                    FieldPanel('strat_pictural_pericol'),
                    ]),
                FieldPanel('strat_pictural_detalii'),
            ],
            heading="Strat pictural",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [   
                FieldRowPanel([
                    FieldPanel('obiecte_de_cult'),
                    FieldPanel('obiecte_de_cult_pericol'),
                    ]),
                FieldPanel('obiecte_de_cult_detalii'),
            ],
            heading="Obiecte de cult",
            classname="collapsible ",
        ),
        MultiFieldPanel(
            [   
                FieldRowPanel([
                    FieldPanel('mobilier'),
                    FieldPanel('mobilier_pericol'),
                    ]),
                FieldPanel('mobilier_detalii'),
            ],
            heading="Mobilier",
            classname="collapsible ",
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


class FinisajPage(Page):
    subpage_types = []
    promote_panels = []

    content_panels = []

    class Meta:  # noqa

        verbose_name = "Finisaj"
        verbose_name_plural = "Finisaj"


class ComponentaArtisticaPage(Page):
    subpage_types = []
    promote_panels = []

    content_panels = []

    class Meta:  # noqa

        verbose_name = "Componenta Artistică"
        verbose_name_plural = "Componenta Artistică"
