from django.db import models
from django import forms
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel,
    PageChooserPanel,
    ObjectList,
    TabbedInterface,
)
from wagtail.search import index
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
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
        # "IdentificarePage"
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
    #     print(qs)
    #     return qs

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
    utilizare_detalii =  RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True)
    singularitate = models.ForeignKey('nomenclatoare.SingularitateBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='p_biserici')
    singularitate_detalii =  RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True)
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
            heading="Denumire"
        ),
        FieldPanel("cult"),
        FieldPanel("utilizare"),
        FieldPanel("utilizare_detalii"),
        FieldPanel("singularitate"),
        FieldPanel("singularitate_detalii"),
        FieldPanel("functiune"),
        FieldPanel("functiune_detalii"),
        FieldPanel("functiune_initiala"),
        FieldPanel("functiune_initiala_detalii"),
        FieldPanel("proprietate_actuala"),
        FieldPanel("proprietate_detalii"),
        FieldPanel("proprietar_actual"),
        FieldPanel("inscriere_documente_cadastrale"),


        
    ]
    class Meta:  # noqa

        verbose_name = "Identificare"
        verbose_name_plural = "Identificare"



class DescrierePage(Page):
    """
    Capitol: Descriere Biserica
    """

    # Localizare/peisaj
    amplasament = models.ForeignKey('nomenclatoare.AmplasamentBiserica', null=True, blank=True, on_delete=models.SET_NULL)
    topografie = models.ForeignKey('nomenclatoare.TopografieBiserica', null=True, blank=True, on_delete=models.SET_NULL)
    toponim = models.CharField(max_length=150, null=True, blank=True, help_text="denumirea locului")
    toponim_sursa  =RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Sursă informații')
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
    gabarit_exterior_al_talpilor = models.ImageField(upload_to='schite', max_length=100, null=True, blank=True, help_text='o schiță a planului tălpilor / elevației /  turnului / triunghiului șarpantei')
    materiale = models.ManyToManyField('nomenclatoare.Material', help_text="Materiale folosite in construcția bisericii", blank=True)
    detalii_materiale = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, help_text="Materialele care compun structura de rezistentă a bisericii")

    # Elemente arhitecturale

    turn_dimensiune = models.ForeignKey('nomenclatoare.DimensiuneTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Turn (dimensiune)')
    turn_tip = models.ForeignKey('nomenclatoare.TipTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Turn (tip)')
    turn_numar = models.IntegerField(null=True, blank=True, verbose_name='Număr de turnuri')
    turn_decor = models.ForeignKey('nomenclatoare.DecorTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Turn (decor)')
    turn_plan = models.ForeignKey('nomenclatoare.PlanTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Turn (plan)')
    turn_amplasare = models.ForeignKey('nomenclatoare.AmplasareTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Turn (amplasare)')
    turn_galerie = models.ForeignKey('nomenclatoare.GalerieTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Turn (galerie)')
    turn_numar_arcade = models.IntegerField(null=True, blank=True, verbose_name='Număr arcade Turn deschis')
    turn_numar_arcade_detalii =RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Detalii arcade Turn deschis')
    turn_asezare_talpi  = models.ForeignKey('nomenclatoare.AsezareTalpaTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Turn (așezarea tălpilor turnului în legătură cu butea bisericii)')
    turn_relatie_talpi  = models.ForeignKey('nomenclatoare.RelatieTalpaTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Turn (relația dintre tălpile turnului)')
    turn_numar_talpi = models.IntegerField(null=True, blank=True, verbose_name='Turn (număr de tălpi)')
    turn_observatii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True)

    clopote_an = models.IntegerField(null=True, blank=True, verbose_name='Clopote (an)')
    clopote_inscriptie =RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Clopote (Inscripție)')

    sarpanta_tip  = models.ManyToManyField('nomenclatoare.TipSarpanta', blank=True, verbose_name='Șarpantă (tip)')
    sarpanta_veche_nefolosita = models.BooleanField(default=False, verbose_name='Șarpantă veche nefolosită sub șarpanta actuală')
    sarpanta_numar_turnulete  = models.IntegerField(null=True, blank=True, verbose_name='Șarpantă (număr turnulețe decorative)')
    sarpanta_numar_cruci  = models.IntegerField(null=True, blank=True, verbose_name='Șarpantă (număr cruci)')
    sarpanta_material_cruci  = models.ForeignKey('nomenclatoare.Material', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șarpantă (material cruci)', related_name="p_material_cruci")
    sarpanta_detalii =RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Șarpantă (observații)')

    numar_accese_pridvor  = models.IntegerField(null=True, blank=True, verbose_name='Număr accese pridvor')
    numar_accese_pridvor_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Număr accese pridvor (observații)')
    numar_accese_pronaos  = models.IntegerField(null=True, blank=True, verbose_name='Număr accese pronaos')
    numar_accese_pronaos_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Număr accese pronaos (observații)')
    numar_accese_naos  = models.IntegerField(null=True, blank=True, verbose_name='Număr accese naos')
    numar_accese_naos_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Număr accese naos (observații)')
    numar_accese_altar  = models.IntegerField(null=True, blank=True, verbose_name='Număr accese altar')
    numar_accese_altar_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Număr accese altar (observații)')


    numar_geamuri_pridvor  = models.IntegerField(null=True, blank=True, verbose_name='Număr geamuri pridvor')
    numar_geamuri_pridvor_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Număr geamuri pridvor (observații)')
    numar_geamuri_pronaos  = models.IntegerField(null=True, blank=True, verbose_name='Număr geamuri pronaos')
    numar_geamuri_pronaos_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Număr geamuri pronaos (observații)')
    numar_geamuri_naos  = models.IntegerField(null=True, blank=True, verbose_name='Număr geamuri naos')
    numar_geamuri_naos_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Număr geamuri naos (observații)')
    numar_geamuri_altar  = models.IntegerField(null=True, blank=True, verbose_name='Număr geamuri altar')
    numar_geamuri_altar_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Număr geamuri altar (observații)')


    oachiesi_aerisitoare = models.BooleanField(default=False, verbose_name='Ochieși / Aerisitoare ')
    oachiesi_aerisitoare_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Ochieși / Aerisitoare (observații)')


    
    bolta_peste_pronaos  = models.ForeignKey('nomenclatoare.TipBoltaPronaos', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Boltă peste pronaos', related_name='p_biserici_bolta_peste_pronaos')
    bolta_peste_pronaos_material = models.ManyToManyField('nomenclatoare.Material', blank=True, related_name='p_biserici_bolta_peste_pronaos')
    bolta_peste_pronaos_tipul_de_arc = models.ManyToManyField('nomenclatoare.TipArcBolta', blank=True, related_name='p_biserici_bolta_peste_pronaos')
    bolta_peste_pronaos_observatii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True)

    bolta_peste_naos  = models.ForeignKey('nomenclatoare.TipBoltaPronaos', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Boltă peste naos', related_name='p_biserici_bolta_peste_naos')
    bolta_peste_naos_material = models.ManyToManyField('nomenclatoare.Material', blank=True, related_name='p_biserici_bolta_peste_naos')
    bolta_peste_naos_tipul_de_arc = models.ManyToManyField('nomenclatoare.TipArcBolta', blank=True, related_name='p_biserici_bolta_peste_naos')
    bolta_peste_naos_observatii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True)

    bolta_peste_altar  = models.ForeignKey('nomenclatoare.BoltaPesteAltar', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Boltă peste altar', related_name='p_biserici_bolta_peste_altar')
    bolta_peste_altar_tip  = models.ForeignKey('nomenclatoare.TipBoltaPesteAltar', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Tip bolta peste altar', related_name='p_biserici')
    bolta_peste_altar_material = models.ManyToManyField('nomenclatoare.Material', blank=True, related_name='p_biserici_bolta_peste_altar')
    bolta_peste_altar_tipul_de_arc = models.ManyToManyField('nomenclatoare.TipArcBolta', blank=True, related_name='p_biserici_bolta_peste_altar')
    bolta_peste_altar_observatii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True)

    cor = models.BooleanField(default=False)
    cor_material = models.ManyToManyField('nomenclatoare.Material', blank=True, related_name='p_biserici_cor')
    cor_observatii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True)

    solee = models.BooleanField(default=False)
    solee_detalii = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Solee (observații)')

    masa_altar_material_picior  = models.ForeignKey('nomenclatoare.Material', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Sfânta masă a altarului (materialul piciorului)', related_name='p_masa_altar_picior')
    masa_altar_material_blat  = models.ForeignKey('nomenclatoare.Material', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Sfânta masă a altarului (materialul blatului)', related_name='p_masa_altar_blat')
    masa_altar_observatii =  RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True)

    # Structura
    fundatia  = models.ForeignKey('nomenclatoare.TipFundatie', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Fundația', related_name='p_biserici')
    sistem_in_cheotoare  = models.ForeignKey('nomenclatoare.TipStructuraCheotoare', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Sistem structural al corpului bisericii În cheotoare', related_name='p_biserici')
    sistem_in_catei  = models.ForeignKey('nomenclatoare.TipStructuraCatei', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Sistem structural al corpului bisericii În căței', related_name='p_biserici')
    sistem_mixt =RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'document-link',], null=True, blank=True, verbose_name='Sistem structural al corpului bisericii mixt')



    subpage_types = []
    promote_panels = []

    content_panels = []
    localizare_panels = [
       ModelChooserPanel("amplasament"),
       ModelChooserPanel("topografie"),
       FieldPanel("toponim"),
       FieldPanel("toponim_sursa"),
       ModelChooserPanel("relatia_cu_cimitirul"),
       FieldPanel("peisagistica_sitului", widget=forms.CheckboxSelectMultiple),
       FieldPanel("observatii"),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(localizare_panels, heading='Localizare/peisaj'),
            ObjectList(localizare_panels, heading='Ansamblu construit'),
            ObjectList(localizare_panels, heading='Arhitectura bisericii'),
            ObjectList(localizare_panels, heading='Finisaje'),
            ObjectList(localizare_panels, heading='Intervenții arhitecturale vizibile în timp'),

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
    subpage_types = []
    promote_panels = []

    content_panels = []

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
