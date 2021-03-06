from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from guardian.shortcuts import get_objects_for_user, assign_perm, remove_perm
from simple_history.models import HistoricalRecords
from simple_history import register
from adminsortable.models import SortableMixin

from nomenclatoare import models as nmodels


User = get_user_model()
register(User, app=__package__)

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


def get_completare(self):
        fields = self._meta.get_fields()
        n_fields = len(self._meta.get_fields()) - 2
        n_count = 0
        missing_fields = []

        for field in fields:
            if field.name in ['completare', 'missing_fields']:
                continue
            try:
                if getattr(self, field.name):
                    n_count += 1
                else:
                    missing_fields.append(field.verbose_name)
            except:
                if getattr(self, field.name+'_set').count():
                    n_count += 1
                else:
                    # print('---')
                    # print(field)
                    # print(dir(field))
                    # print(field.__dict__['related_model'])
                    # print(dir(field.__dict__['related_model']._meta))
                    # print(field.__dict__['related_model']._meta.verbose_name)
                    # print('====')
                    # print(field.__class__)
                    # print(dir(field.__class__))
                    missing_fields.append(field.__dict__['related_model']._meta.verbose_name)

        return round(n_count / n_fields * 100, 2), missing_fields


class Biserica(SortableMixin):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=50)

    the_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    history = HistoricalRecords()

    class Meta:
        ordering = ['the_order']
        verbose_name_plural = " Biserici"

    def __str__(self):
        return self.nume


    def completare(self):
        return 0


class Identificare(models.Model):
    """
    Capitol: Identificare Biserica
    """
    biserica = models.OneToOneField('Biserica', on_delete=models.CASCADE)
    judet = models.ForeignKey('nomenclatoare.Judet', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici')
    localitate = models.ForeignKey('nomenclatoare.Localitate', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici')
    adresa = models.CharField(max_length=250, null=True, blank=True)
    latitudine = models.FloatField(null=True, blank=True)
    longitudine = models.FloatField(null=True, blank=True)
    statut = models.ForeignKey('nomenclatoare.StatutBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici')
    denumire_actuala = models.CharField(max_length=150, null=True, blank=True)
    denumire_precedenta = models.CharField(max_length=150, null=True, blank=True)
    denumire_locala = models.CharField(max_length=150, null=True, blank=True)
    denumire_oberservatii = models.TextField(null=True, blank=True)
    cult = models.ForeignKey('nomenclatoare.CultBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici')
    utilizare = models.ForeignKey('nomenclatoare.UtilizareBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici')
    utilizare_detalii = models.TextField(null=True, blank=True)
    singularitate = models.ForeignKey('nomenclatoare.SingularitateBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici')
    singularitate_detalii = models.TextField(null=True, blank=True)
    functiune = models.ForeignKey('nomenclatoare.FunctiuneBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici')
    functiune_detalii = models.TextField(null=True, blank=True)
    functiune_initiala = models.ForeignKey('nomenclatoare.FunctiuneBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici_initiale')
    functiune_initiala_detalii = models.TextField(null=True, blank=True)
    proprietate_actuala = models.ForeignKey('nomenclatoare.RegimProprietate', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici_initiale')
    proprietate_detalii = models.TextField(null=True, blank=True)
    proprietar_actual = models.TextField(null=True, blank=True)
    inscriere_documente_cadastrale = models.IntegerField(choices=IDENTIFICARE_DOC_CADASTRALE, null=True, blank=True)

    completare = models.FloatField(default=0)
    missing_fields = models.JSONField(null=True, blank=True)

    history = HistoricalRecords()

    class Meta:
        ordering = ["biserica__the_order"]
        verbose_name_plural = "1. Identificare"

    def __str__(self):
        return f"Identificare {self.biserica.nume}"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_judet = self.judet



    def save(self, *args, **kwargs):
        completare = get_completare(self)
        self.completare = completare[0]
        self.missing_fields = completare[1]
        super().save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     print(kwargs)
    #     if self.judet:
    #         if self.__original_judet != self.judet or kwargs.get('force_update', False) == True:
    #             biserica = self.biserica

    #             judet_biserica = self.judet.nume
    #             grup_judet, _ = Group.objects.get_or_create(name=judet_biserica)
    #             assign_perm('view_biserica', grup_judet, biserica)
    #             assign_perm('change_biserica', grup_judet, biserica)

    #             for t in ['identificare', 'istoric', 'descriere', 'patrimoniu', 'conservare']:
    #                     assign_perm(f'view_{t}', grup_judet, getattr(biserica, t))
    #                     assign_perm(f'change_{t}', grup_judet, getattr(biserica, t))

    #             for judet in Group.objects.exclude(name=judet_biserica):
    #                 remove_perm('view_biserica', judet, biserica)
    #                 remove_perm('change_biserica', judet, biserica)

    #                 for t in ['identificare', 'istoric', 'descriere', 'patrimoniu', 'conservare']:
    #                     remove_perm(f'view_{t}', judet, getattr(biserica, t))
    #                     remove_perm(f'change_{t}', judet, getattr(biserica, t))
    #     super().save(*args, **kwargs)


class Descriere(models.Model):
    """
    Capitol: Descriere Biserica
    """

    biserica = models.OneToOneField('Biserica', on_delete=models.CASCADE)

    # Localizare/peisaj
    amplasament = models.ForeignKey('nomenclatoare.AmplasamentBiserica', null=True, blank=True, on_delete=models.SET_NULL)
    topografie = models.ForeignKey('nomenclatoare.TopografieBiserica', null=True, blank=True, on_delete=models.SET_NULL)
    toponim = models.CharField(max_length=150, null=True, blank=True, help_text="denumirea locului")
    toponim_sursa  = models.TextField(null=True, blank=True, verbose_name='Sursă informații')
    relatia_cu_cimitirul = models.ForeignKey('nomenclatoare.RelatieCimitir', null=True, blank=True, on_delete=models.SET_NULL)
    peisagistica_sitului = models.ManyToManyField('nomenclatoare.PeisagisticaSit', blank=True)
    observatii = models.TextField(null=True, blank=True)

    # Ansamblu construit
    elemente = models.ManyToManyField('nomenclatoare.ElementInteriorBiserica', help_text="Elemente ansamblu construit", blank=True)
    detalii_elemente = models.TextField(null=True, blank=True)

    elemente_importante = models.ManyToManyField('nomenclatoare.ElementImportant', help_text="Elemente ansamblu construit", blank=True)
    detalii_elemente_importante = models.TextField(null=True, blank=True)

    
    # Arhitectura
    planimetria_bisericii = models.ForeignKey('nomenclatoare.Planimetrie', null=True, blank=True, on_delete=models.SET_NULL)
    gabarit_exterior_al_talpilor = models.ImageField(upload_to='schite', max_length=100, null=True, blank=True, help_text='o schiță a planului tălpilor / elevației /  turnului / triunghiului șarpantei')
    materiale = models.ManyToManyField('nomenclatoare.Material', help_text="Materiale folosite in construcția bisericii", blank=True)
    detalii_materiale = models.TextField(null=True, blank=True, help_text="Materialele care compun structura de rezistentă a bisericii")

    # Elemente arhitecturale

    turn_dimensiune = models.ForeignKey('nomenclatoare.DimensiuneTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Turn (dimensiune)')
    turn_tip = models.ForeignKey('nomenclatoare.TipTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Turn (tip)')
    turn_numar = models.IntegerField(null=True, blank=True, verbose_name='Număr de turnuri')
    turn_decor = models.ForeignKey('nomenclatoare.DecorTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Turn (decor)')
    turn_plan = models.ForeignKey('nomenclatoare.PlanTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Turn (plan)')
    turn_amplasare = models.ForeignKey('nomenclatoare.AmplasareTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Turn (amplasare)')
    turn_galerie = models.ForeignKey('nomenclatoare.GalerieTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Turn (galerie)')
    turn_numar_arcade = models.IntegerField(null=True, blank=True, verbose_name='Număr arcade Turn deschis')
    turn_numar_arcade_detalii = models.TextField(null=True, blank=True, verbose_name='Detalii arcade Turn deschis')
    turn_asezare_talpi  = models.ForeignKey('nomenclatoare.AsezareTalpaTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Turn (așezarea tălpilor turnului în legătură cu butea bisericii)')
    turn_relatie_talpi  = models.ForeignKey('nomenclatoare.RelatieTalpaTurn', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Turn (relația dintre tălpile turnului)')
    turn_numar_talpi = models.IntegerField(null=True, blank=True, verbose_name='Turn (număr de tălpi)')
    turn_observatii = models.TextField(null=True, blank=True)

    clopote_an = models.IntegerField(null=True, blank=True, verbose_name='Clopote (an)')
    clopote_inscriptie = models.TextField(null=True, blank=True, verbose_name='Clopote (Inscripție)')

    sarpanta_tip  = models.ManyToManyField('nomenclatoare.TipSarpanta', blank=True, verbose_name='Șarpantă (tip)')
    sarpanta_veche_nefolosita = models.BooleanField(default=False, verbose_name='Șarpantă veche nefolosită sub șarpanta actuală')
    sarpanta_numar_turnulete  = models.IntegerField(null=True, blank=True, verbose_name='Șarpantă (număr turnulețe decorative)')
    sarpanta_numar_cruci  = models.IntegerField(null=True, blank=True, verbose_name='Șarpantă (număr cruci)')
    sarpanta_material_cruci  = models.ForeignKey('nomenclatoare.Material', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Șarpantă (material cruci)', related_name="material_cruci")
    sarpanta_detalii = models.TextField(null=True, blank=True, verbose_name='Șarpantă (observații)')

    numar_accese_pridvor  = models.IntegerField(null=True, blank=True, verbose_name='Număr accese pridvor')
    numar_accese_pridvor_detalii =  models.TextField(null=True, blank=True, verbose_name='Număr accese pridvor (observații)')
    numar_accese_pronaos  = models.IntegerField(null=True, blank=True, verbose_name='Număr accese pronaos')
    numar_accese_pronaos_detalii =  models.TextField(null=True, blank=True, verbose_name='Număr accese pronaos (observații)')
    numar_accese_naos  = models.IntegerField(null=True, blank=True, verbose_name='Număr accese naos')
    numar_accese_naos_detalii =  models.TextField(null=True, blank=True, verbose_name='Număr accese naos (observații)')
    numar_accese_altar  = models.IntegerField(null=True, blank=True, verbose_name='Număr accese altar')
    numar_accese_altar_detalii =  models.TextField(null=True, blank=True, verbose_name='Număr accese altar (observații)')


    numar_geamuri_pridvor  = models.IntegerField(null=True, blank=True, verbose_name='Număr geamuri pridvor')
    numar_geamuri_pridvor_detalii =  models.TextField(null=True, blank=True, verbose_name='Număr geamuri pridvor (observații)')
    numar_geamuri_pronaos  = models.IntegerField(null=True, blank=True, verbose_name='Număr geamuri pronaos')
    numar_geamuri_pronaos_detalii =  models.TextField(null=True, blank=True, verbose_name='Număr geamuri pronaos (observații)')
    numar_geamuri_naos  = models.IntegerField(null=True, blank=True, verbose_name='Număr geamuri naos')
    numar_geamuri_naos_detalii =  models.TextField(null=True, blank=True, verbose_name='Număr geamuri naos (observații)')
    numar_geamuri_altar  = models.IntegerField(null=True, blank=True, verbose_name='Număr geamuri altar')
    numar_geamuri_altar_detalii =  models.TextField(null=True, blank=True, verbose_name='Număr geamuri altar (observații)')


    oachiesi_aerisitoare = models.BooleanField(default=False, verbose_name='Ochieși / Aerisitoare ')
    oachiesi_aerisitoare_detalii =  models.TextField(null=True, blank=True, verbose_name='Ochieși / Aerisitoare (observații)')


    
    bolta_peste_pronaos  = models.ForeignKey('nomenclatoare.TipBoltaPronaos', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Boltă peste pronaos', related_name='biserici_bolta_peste_pronaos')
    bolta_peste_pronaos_material = models.ManyToManyField('nomenclatoare.Material', blank=True, related_name='biserici_bolta_peste_pronaos')
    bolta_peste_pronaos_tipul_de_arc = models.ManyToManyField('nomenclatoare.TipArcBolta', blank=True, related_name='biserici_bolta_peste_pronaos')
    bolta_peste_pronaos_observatii = models.TextField(null=True, blank=True)

    bolta_peste_naos  = models.ForeignKey('nomenclatoare.TipBoltaPronaos', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Boltă peste naos', related_name='biserici_bolta_peste_naos')
    bolta_peste_naos_material = models.ManyToManyField('nomenclatoare.Material', blank=True, related_name='biserici_bolta_peste_naos')
    bolta_peste_naos_tipul_de_arc = models.ManyToManyField('nomenclatoare.TipArcBolta', blank=True, related_name='biserici_bolta_peste_naos')
    bolta_peste_naos_observatii = models.TextField(null=True, blank=True)

    bolta_peste_altar  = models.ForeignKey('nomenclatoare.BoltaPesteAltar', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Boltă peste altar', related_name='biserici_bolta_peste_altar')
    bolta_peste_altar_tip  = models.ForeignKey('nomenclatoare.TipBoltaPesteAltar', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Tip bolta peste altar', related_name='biserici')
    bolta_peste_altar_material = models.ManyToManyField('nomenclatoare.Material', blank=True, related_name='biserici_bolta_peste_altar')
    bolta_peste_altar_tipul_de_arc = models.ManyToManyField('nomenclatoare.TipArcBolta', blank=True, related_name='biserici_bolta_peste_altar')
    bolta_peste_altar_observatii = models.TextField(null=True, blank=True)

    cor = models.BooleanField(default=False)
    cor_material = models.ManyToManyField('nomenclatoare.Material', blank=True, related_name='biserici_cor')
    cor_observatii = models.TextField(null=True, blank=True)

    solee = models.BooleanField(default=False)
    solee_detalii =  models.TextField(null=True, blank=True, verbose_name='Solee (observații)')

    masa_altar_material_picior  = models.ForeignKey('nomenclatoare.Material', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Sfânta masă a altarului (materialul piciorului)', related_name='masa_altar_picior')
    masa_altar_material_blat  = models.ForeignKey('nomenclatoare.Material', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Sfânta masă a altarului (materialul blatului)', related_name='masa_altar_blat')
    masa_altar_observatii =  models.TextField(null=True, blank=True)

    # Structura
    fundatia  = models.ForeignKey('nomenclatoare.TipFundatie', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Fundația', related_name='biserici')
    sistem_in_cheotoare  = models.ForeignKey('nomenclatoare.TipStructuraCheotoare', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Sistem structural al corpului bisericii În cheotoare', related_name='biserici')
    sistem_in_catei  = models.ForeignKey('nomenclatoare.TipStructuraCatei', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Sistem structural al corpului bisericii În căței', related_name='biserici')
    sistem_mixt = models.TextField(null=True, blank=True, verbose_name='Sistem structural al corpului bisericii mixt')

    # amplasament = models.ForeignKey('nomenclatoare.AmplasamentBiserica', null=True, blank=True, on_delete=models.SET_NULL)
    # toponim = models.CharField(max_length=150, null=True, blank=True, help_text="denumirea locului")
    # toponim_sursa  = models.TextField(null=True, blank=True)
    # elemente = models.ManyToManyField('nomenclatoare.ElementInteriorBiserica', help_text="Elemente ansamblu construit", blank=True)
    # datat = models.BooleanField(default=False)

    completare = models.FloatField(default=0)
    missing_fields = models.JSONField(null=True, blank=True)

    history = HistoricalRecords()

    class Meta:
        ordering = ["biserica__the_order"]
        verbose_name_plural = "3. Descriere"

    def __str__(self):
        return f"Descriere {self.biserica.nume}"

    


    def save(self, *args, **kwargs):
        completare = get_completare(self)
        self.completare = completare[0]
        self.missing_fields = completare[1]
        super().save(*args, **kwargs)

class PovesteBiserica(models.Model):
    """
    Description: Model Description
    """
    istoric = models.ForeignKey('Istoric', on_delete=models.CASCADE)
    detalii = models.TextField()
    sursa = models.TextField()

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = 'Povești Biserică'


class InterventieBiserica(models.Model):
    """
    Description: Model Description
    """
    istoric = models.ForeignKey('Istoric', on_delete=models.CASCADE)
    element = models.ForeignKey('nomenclatoare.ElementInteriorBiserica', on_delete=models.CASCADE)
    datat = models.BooleanField(default=False)
    an = models.IntegerField(null=True, blank=True)
    observatii = models.TextField(null=True, blank=True)
    sursa = models.TextField(null=True, blank=True)
    este_ultima_interventie = models.BooleanField(default=False)


    class Meta:
        pass

class Istoric(models.Model):
    """
    Capitol: Istoric Biserica
    """

    biserica = models.OneToOneField('Biserica', on_delete=models.CASCADE)
    sursa_datare = models.ManyToManyField('nomenclatoare.SursaDatare', related_name='biserici', blank=True)
    anul_constructiei = models.IntegerField(null=True, blank=True)
    datare_prin_interval_timp = models.CharField(max_length=50, null=True, blank=True)
    datare_secol = models.ForeignKey('nomenclatoare.Secol', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici')
    datare_secol_detalii  = models.TextField(null=True, blank=True)
    datare_secol_sursa  = models.TextField(null=True, blank=True)
    studiu_dendocronologic = models.ForeignKey('nomenclatoare.StudiuDendocronologic', null=True, blank=True, on_delete=models.SET_NULL)
    pisanie_traducere = models.TextField(null=True, blank=True)
    pisanie_secol_detalii  = models.TextField(null=True, blank=True)
    pisanie_secol_sursa  = models.TextField(null=True, blank=True)
    ctitori = models.ManyToManyField('nomenclatoare.Persoana', through=nmodels.CtitorBiserica, related_name='ctitor', blank=True)
    mesteri = models.ManyToManyField('nomenclatoare.Persoana', through=nmodels.MesterBiserica, related_name='mester', blank=True)
    zugravi = models.ManyToManyField('nomenclatoare.Persoana', through=nmodels.ZugravBiserica, related_name='zugrav', blank=True)
    personalitati = models.ManyToManyField('nomenclatoare.Persoana', through=nmodels.PersonalitateBiserica, related_name='personalitate', blank=True)
    evenimente = models.ManyToManyField('nomenclatoare.Eveniment', through=nmodels.EvenimentBiserica, blank=True)

    mutari_biserica = models.ManyToManyField('nomenclatoare.Localitate', through=nmodels.MutareBiserica, blank=True)

    completare = models.FloatField(default=0)
    missing_fields = models.JSONField(null=True, blank=True)

    history = HistoricalRecords()

    class Meta:
        ordering = ["biserica__the_order"]
        verbose_name_plural = "2. Istoric"
        

    def __str__(self):
        return f"Istoric {self.biserica.nume}"



    def save(self, *args, **kwargs):
        completare = get_completare(self)
        self.completare = completare[0]
        self.missing_fields = completare[1]
        super().save(*args, **kwargs)

class Patrimoniu(models.Model):
    """
    Capitol: Valoare Patrimoniu Cultural Biserica
    """
    biserica = models.OneToOneField('Biserica', on_delete=models.CASCADE)

    vechime = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, help_text= "Printr-un algorim definit se va da automat o notă de la 1-5 în funcție de vechimea monumentului si a picturii descrise conform OMCC2682/2003 ETC")
    vechime_detalii = models.TextField(null=True, blank=True)
    integritate = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, help_text= "Integritate / Autenticitate")
    integritate_detalii = models.TextField(null=True, blank=True)
    unicitate = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, help_text= "Unicitate / raritate")
    unicitate_detalii = models.TextField(null=True, blank=True)
    valoare_memoriala = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, help_text= "evenimente, personalități")
    valoare_memoriala_detalii = models.TextField(null=True, blank=True)
    peisaj_cultural = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, help_text= "Parte definitorie a peisajului cultural al zonei")
    peisaj_cultural_detalii = models.TextField(null=True, blank=True)
    valoare_sit = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, help_text= "Valoarea sitului împreună cu toate componentele ansamblului din care face parte, ținând cont de integritate, autenticitate, estetică peisageră, biodiversitate, etc. SUBIECTIV")
    valoare_sit_detalii = models.TextField(null=True, blank=True, help_text= "Descriere a elementelor valoroase, particulare")
    estetica = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, help_text= "Estetică / Arhitectură")
    estetica_detalii = models.TextField(null=True, blank=True)
    mestesug = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, help_text= "Meșteșug (calitatea muncii -  a se vedea golurile dintre lemne (dintre bârne în general dar în special la așezarea elementelor orizontale peste cele verticale))")
    mestesug_detalii = models.TextField(null=True, blank=True)
    pictura = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, )
    pictura_detalii = models.TextField(null=True, blank=True)
    folosinta_actuala = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, help_text= "Folosință actuală / singura biserică din sat / loc al patrimoniului imaterial")
    folosinta_actuala_detalii = models.TextField(null=True, blank=True)
    relevanta_actuala = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, help_text= "Relevanța actuală pentru comunitatea locală (prin reprezentanții săi: preot, crâsnic, învățător, familii de bază)")
    relevanta_actuala_detalii = models.TextField(null=True, blank=True)
    potential = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, help_text= "Potențialul de beneficii aduse comunității locale")
    potential_detalii = models.TextField(null=True, blank=True)


    completare = models.FloatField(default=0)
    missing_fields = models.JSONField(null=True, blank=True)
    history = HistoricalRecords()

    class Meta:
        ordering = ["biserica__the_order"]
        verbose_name_plural = "4. Valoare Patrimoniu Cultural"

    def __str__(self):
        return f"Valoare patrimoniu cultural {self.biserica.nume}"

    


    def save(self, *args, **kwargs):
        completare = get_completare(self)
        self.completare = completare[0]
        self.missing_fields = completare[1]
        super().save(*args, **kwargs)


class Conservare(models.Model):
    """
    Capitol: Stare conservare Biserica
    """
    biserica = models.OneToOneField('Biserica', on_delete=models.CASCADE)

    # Sit
    stare_cimitir = models.IntegerField(choices=NR15, null=True, blank=True)
    stare_cimitir_detalii = models.TextField( null=True, blank=True)
    stare_monumente_funerare_valoroase = models.IntegerField(choices=NR15, null=True, blank=True)
    stare_monumente_funerare_valoroase_detalii = models.TextField( null=True, blank=True)
    vegetatie_invaziva = models.IntegerField(choices=NR15, null=True, blank=True)
    vegetatie_invaziva_detalii = models.TextField( null=True, blank=True, help_text="Vegetație invazivă ce poate pune monumentul în pericol")
    stare_elemente_arhitecturale = models.IntegerField(choices=NR15, null=True, blank=True)
    stare_elemente_arhitecturale_detalii = models.TextField( null=True, blank=True)

    # Structura bisericii
    stare_teren = models.IntegerField(choices=NR15, null=True, blank=True)
    stare_teren_detalii = models.TextField( null=True, blank=True)
    stare_fundatii = models.IntegerField(choices=NR15, null=True, blank=True)
    stare_fundatii_detalii = models.TextField( null=True, blank=True)
    stare_corp_biserica = models.IntegerField(choices=NR15, null=True, blank=True)
    stare_corp_biserica_detalii = models.TextField( null=True, blank=True)
    stare_bolti = models.IntegerField(choices=NR15, null=True, blank=True)
    stare_bolti_detalii = models.TextField( null=True, blank=True)
    stare_sarpanta_peste_corp_biserica = models.IntegerField(choices=NR15, null=True, blank=True)
    stare_sarpanta_peste_corp_biserica_detalii = models.TextField( null=True, blank=True)
    stare_structura_turn = models.IntegerField(choices=NR15, null=True, blank=True)
    stare_structura_turn_detalii = models.TextField( null=True, blank=True, help_text="tarea structurii turnului, inclusiv a tălpilor și a coifului")
    stare_talpi = models.IntegerField(choices=NR15, null=True, blank=True)
    stare_talpi_detalii = models.TextField( null=True, blank=True)
    stare_cosoroabe = models.IntegerField(choices=NR15, null=True, blank=True)
    stare_cosoroabe_detalii = models.TextField( null=True, blank=True)
    stare_sarpanta_turn = models.IntegerField(choices=NR15, null=True, blank=True)
    stare_sarpanta_turn_detalii = models.TextField( null=True, blank=True)



    # Finisaje de arhitectură
    stare_invelitoare = models.IntegerField(choices=NR15, null=True, blank=True)
    stare_invelitoare_detalii = models.TextField( null=True, blank=True)
    stare_finisaj_peste_corp = models.IntegerField(choices=NR15, null=True, blank=True)
    stare_finisaj_peste_corp_detalii = models.TextField( null=True, blank=True)
    stare_finisaj_tambur_turn = models.IntegerField(choices=NR15, null=True, blank=True)
    stare_finisaj_tambur_turn_detalii = models.TextField( null=True, blank=True)
    stare_pardoseli_interioare = models.IntegerField(choices=NR15, null=True, blank=True)
    stare_pardoseli_interioare_detalii = models.TextField( null=True, blank=True)
    stare_usi_si_ferestre = models.IntegerField(choices=NR15, null=True, blank=True)
    stare_usi_si_ferestre_detalii = models.TextField( null=True, blank=True)

    # Starea stratului pictural
    stare_picturi_exterioare = models.IntegerField(choices=NR15, null=True, blank=True)
    stare_picturi_exterioare_detalii = models.TextField( null=True, blank=True)
    stare_picturi_interioare = models.IntegerField(choices=NR15, null=True, blank=True)
    stare_picturi_interioare_detalii = models.TextField( null=True, blank=True)
    stare_iconostas = models.IntegerField(choices=NR15, null=True, blank=True)
    stare_iconostas_detalii = models.TextField( null=True, blank=True)


    # Obiecte de cult
    stare_icoane_istorice = models.IntegerField(choices=NR15, null=True, blank=True)
    stare_icoane_istorice_detalii = models.TextField( null=True, blank=True)
    starea_obiecte_de_cult = models.IntegerField(choices=NR15, null=True, blank=True)
    starea_obiecte_de_cult_detalii = models.TextField( null=True, blank=True)
    starea_mobilier = models.IntegerField(choices=NR15, null=True, blank=True)
    starea_mobilier_detalii = models.TextField( null=True, blank=True)

    completare = models.FloatField(default=0)
    missing_fields = models.JSONField(null=True, blank=True)
    history = HistoricalRecords()

    class Meta:
        ordering = ["biserica__the_order"]
        verbose_name_plural = "5. Stare de conservare"

    def __str__(self):
        return f"Stare conservare {self.biserica.nume}"

    


    def save(self, *args, **kwargs):
        completare = get_completare(self)
        self.completare = completare[0]
        self.missing_fields = completare[1]
        super().save(*args, **kwargs)


class FotografieAnsamblu(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass


class FotografieFatada(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass


class FotografiePortal(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass

class FotografieFereastra(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass

class FotografieCheotoar(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass

class FotografieTalpa(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass

class FotografieStreasina(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass

class FotografieInvelitoare(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass

class FotografieCruceBiserica(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass

class FotografieTurn(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass

class FotografieDegradariExterioare(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass

class FotografieInteriorDesfasurat(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass

class FotografiePisanieInscriptieCtitorMester(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass

class FotografiePortalPronaos(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass

class FotografiePortalNaos(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass

class FotografieDetaliuBolta(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass


class FotografieDetaliuSculptura(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass


class FotografieDetaliuImaginePereti(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass



class FotografieUrmeSemneSimboluri(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass


class FotografieProgramIconografic(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    titlu = models.CharField(max_length=250, null=True, blank=True)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass


class FotografieIconostasNaos(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass

class FotografieIconostasAltar(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass

class FotografieIcoana(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass

class FotografieObiectCult(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass

class FotografieMobilierCandelabre(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass

class FotografieDegradariInterior(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass

class FotografieDegradariPod(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass


class FotografieDetaliuPod(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    detaliu = models.ForeignKey('nomenclatoare.DetaliuPodTurn', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass


class Fotografii(models.Model):
    """
    Capitol: Fotografii Biserica
    """

    biserica = models.OneToOneField('Biserica', on_delete=models.CASCADE)
    completare = models.FloatField(default=0)
    missing_fields = models.JSONField(null=True, blank=True)
    history = HistoricalRecords()

    class Meta:
        ordering = ["biserica__the_order"]
        verbose_name_plural = "3.1 Fotografii"

    def __str__(self):
        return f"Fotografii {self.biserica.nume}"

    


    def save(self, *args, **kwargs):
        completare = get_completare(self)
        self.completare = completare[0]
        self.missing_fields = completare[1]
        super().save(*args, **kwargs)


class FinisajActualInvelitoare(models.Model):
    """
    Description: Model Description
    """
    finisaj = models.ForeignKey('Finisaj', on_delete=models.CASCADE, related_name='finisaje_actuale')
    material = models.ForeignKey('nomenclatoare.FinisajExterior', on_delete=models.CASCADE)
    sindrila_lungime = models.IntegerField(null=True, blank=True)
    sindrila_latime_medie = models.IntegerField(null=True, blank=True)
    sindrila_grosime_medie = models.IntegerField(null=True, blank=True)
    sindrila_pasul_latuirii = models.IntegerField(null=True, blank=True)
    sindrila_pasul_baterii = models.IntegerField(null=True, blank=True)
    sindrila_numar_straturi = models.IntegerField(null=True, blank=True)
    sindrila_cu_horj = models.BooleanField(default=False)
    sindrlia_tipul_de_batere = models.ForeignKey('nomenclatoare.TipBatereSindrila', null=True, blank=True, on_delete=models.SET_NULL)
    sindrlia_tipul_prindere = models.ForeignKey('nomenclatoare.TipPrindereSindrila', null=True, blank=True, on_delete=models.SET_NULL)
    sindrlia_forma_botului = models.ForeignKey('nomenclatoare.TipBotSindrila', null=True, blank=True, on_delete=models.SET_NULL)
    sindrila_cu_tesitura = models.BooleanField(default=False)
    sindrlia_prelucrare = models.ForeignKey('nomenclatoare.TipPrelucrareSindrila', null=True, blank=True, on_delete=models.SET_NULL)
    sindrlia_esenta_lemnoasa = models.ForeignKey('nomenclatoare.EsentaLemnoasa', null=True, blank=True, on_delete=models.SET_NULL)
    observatii = models.TextField(null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass


class FinisajAnteriorInvelitoare(models.Model):
    """
    Description: Model Description
    """
    finisaj = models.ForeignKey('Finisaj', on_delete=models.CASCADE, related_name='finisaje_anterioare')
    etape_anterioare_vizibile = models.BooleanField(default=False)

    sindrila_pasul_latuirii = models.IntegerField(null=True, blank=True)
    sindrila_numar_straturi = models.IntegerField(null=True, blank=True)
    sindrila_cu_horj = models.BooleanField(default=False)
    sindrlia_tipul_de_batere = models.ForeignKey('nomenclatoare.TipBatereSindrila', null=True, blank=True, on_delete=models.SET_NULL)
    sindrlia_forma_botului = models.ForeignKey('nomenclatoare.TipBotSindrila', null=True, blank=True, on_delete=models.SET_NULL)
    sindrila_cu_tesitura = models.BooleanField(default=False)
    sindrlia_esenta_lemnoasa = models.ForeignKey('nomenclatoare.EsentaLemnoasa', null=True, blank=True, on_delete=models.SET_NULL)

    alte_tipuri_invelitoare = models.TextField(null=True, blank=True)
    observatii = models.TextField(null=True, blank=True)

    history = HistoricalRecords()
    class Meta:
        pass

class FinisajTamburTurn(models.Model):
    """
    Description: Model Description
    """
    finisaj = models.ForeignKey('Finisaj', on_delete=models.CASCADE, related_name='finisaje_tambur_turn')
    material = models.ForeignKey('nomenclatoare.FinisajExterior', on_delete=models.CASCADE)
    sindrila_lungime = models.IntegerField(null=True, blank=True)
    sindrila_latime_medie = models.IntegerField(null=True, blank=True)
    sindrila_grosime_medie = models.IntegerField(null=True, blank=True)
    sindrila_pasul_latuirii = models.IntegerField(null=True, blank=True)
    sindrila_pasul_baterii = models.IntegerField(null=True, blank=True)
    sindrila_numar_straturi = models.IntegerField(null=True, blank=True)
    sindrila_cu_horj = models.BooleanField(default=False)
    sindrlia_tipul_de_batere = models.ForeignKey('nomenclatoare.TipBatereSindrila', null=True, blank=True, on_delete=models.SET_NULL)
    sindrlia_tipul_prindere = models.ForeignKey('nomenclatoare.TipPrindereSindrila', null=True, blank=True, on_delete=models.SET_NULL)
    sindrlia_forma_botului = models.ForeignKey('nomenclatoare.TipBotSindrila', null=True, blank=True, on_delete=models.SET_NULL)
    sindrila_cu_tesitura = models.BooleanField(default=False)
    sindrlia_prelucrare = models.ForeignKey('nomenclatoare.TipPrelucrareSindrila', null=True, blank=True, on_delete=models.SET_NULL)
    sindrlia_esenta_lemnoasa = models.ForeignKey('nomenclatoare.EsentaLemnoasa', null=True, blank=True, on_delete=models.SET_NULL)

    observatii = models.TextField(null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass


class FinisajInvelitoareTurn(models.Model):
    """
    Description: Model Description
    """
    finisaj = models.ForeignKey('Finisaj', on_delete=models.CASCADE, related_name='finisaje_invelitoare_turn')
    material = models.ForeignKey('nomenclatoare.FinisajExterior', on_delete=models.CASCADE)
    sindrila_lungime = models.IntegerField(null=True, blank=True)
    sindrila_latime_medie = models.IntegerField(null=True, blank=True)
    sindrila_grosime_medie = models.IntegerField(null=True, blank=True)
    sindrila_pasul_latuirii = models.IntegerField(null=True, blank=True)
    sindrila_pasul_baterii = models.IntegerField(null=True, blank=True)
    sindrila_numar_straturi = models.IntegerField(null=True, blank=True)
    sindrila_cu_horj = models.BooleanField(default=False)
    sindrlia_tipul_de_batere = models.ForeignKey('nomenclatoare.TipBatereSindrila', null=True, blank=True, on_delete=models.SET_NULL)
    sindrlia_tipul_prindere = models.ForeignKey('nomenclatoare.TipPrindereSindrila', null=True, blank=True, on_delete=models.SET_NULL)
    sindrlia_forma_botului = models.ForeignKey('nomenclatoare.TipBotSindrila', null=True, blank=True, on_delete=models.SET_NULL)
    sindrila_cu_tesitura = models.BooleanField(default=False)
    sindrlia_prelucrare = models.ForeignKey('nomenclatoare.TipPrelucrareSindrila', null=True, blank=True, on_delete=models.SET_NULL)
    sindrlia_esenta_lemnoasa = models.ForeignKey('nomenclatoare.EsentaLemnoasa', null=True, blank=True, on_delete=models.SET_NULL)

    observatii = models.TextField(null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass

class FinisajPardosea(models.Model):
    """
    Description: Model Description
    """
    finisaj = models.ForeignKey('Finisaj', on_delete=models.CASCADE, related_name='finisaje_pardosea')
    element = models.ForeignKey('nomenclatoare.ElementInteriorBiserica', on_delete=models.CASCADE)
    material = models.ForeignKey('nomenclatoare.MaterialFinisajPardoseli', on_delete=models.CASCADE)

    observatii = models.TextField(null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass


class FinisajPeretiInterior(models.Model):
    """
    Description: Model Description
    """
    finisaj = models.ForeignKey('Finisaj', on_delete=models.CASCADE, related_name='finisaje_pereti_interiori')
    element = models.ForeignKey('nomenclatoare.ElementInteriorBiserica', on_delete=models.CASCADE)
    material = models.ForeignKey('nomenclatoare.MaterialFinisajPeretiInteriori', on_delete=models.CASCADE)

    observatii = models.TextField(null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass


class FinisajBolti(models.Model):
    """
    Description: Model Description
    """
    finisaj = models.ForeignKey('Finisaj', on_delete=models.CASCADE, related_name='finisaje_bolti')
    element = models.ForeignKey('nomenclatoare.ElementInteriorBiserica', on_delete=models.CASCADE)
    material = models.ForeignKey('nomenclatoare.Finisaj', on_delete=models.CASCADE)

    observatii = models.TextField(null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass


class FinisajTavan(models.Model):
    """
    Description: Model Description
    """
    finisaj = models.ForeignKey('Finisaj', on_delete=models.CASCADE, related_name='finisaje_tavan')
    element = models.ForeignKey('nomenclatoare.ElementInteriorBiserica', on_delete=models.CASCADE)
    material = models.ForeignKey('nomenclatoare.Finisaj', on_delete=models.CASCADE)

    observatii = models.TextField(null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass






class FinisajPortic(models.Model):
    """
    Description: Model Description
    """
    finisaj = models.ForeignKey('Finisaj', on_delete=models.CASCADE, related_name='finisaje_portic')
    element = models.CharField(choices=ELEMENTE_BISERICA, null=True, blank=True, max_length=100)
    material = models.ForeignKey('nomenclatoare.Finisaj', null=True, blank=True, on_delete=models.CASCADE)

    observatii = models.TextField(null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass

class FinisajPronaos(models.Model):
    """
    Description: Model Description
    """
    finisaj = models.ForeignKey('Finisaj', on_delete=models.CASCADE, related_name='finisaje_pronaos')
    element = models.CharField(choices=ELEMENTE_BISERICA, null=True, blank=True, max_length=100)
    material = models.ForeignKey('nomenclatoare.Finisaj', null=True, blank=True, on_delete=models.CASCADE)

    observatii = models.TextField(null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass

class FinisajNaos(models.Model):
    """
    Description: Model Description
    """
    finisaj = models.ForeignKey('Finisaj', on_delete=models.CASCADE, related_name='finisaje_naos')
    element = models.CharField(choices=ELEMENTE_BISERICA, null=True, blank=True, max_length=100)
    material = models.ForeignKey('nomenclatoare.Finisaj', null=True, blank=True, on_delete=models.CASCADE)

    observatii = models.TextField(null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass

class FinisajAltar(models.Model):
    """
    Description: Model Description
    """
    finisaj = models.ForeignKey('Finisaj', on_delete=models.CASCADE, related_name='finisaje_altar')
    element = models.CharField(choices=ELEMENTE_BISERICA, null=True, blank=True, max_length=100)
    material = models.ForeignKey('nomenclatoare.Finisaj', null=True, blank=True, on_delete=models.CASCADE)

    observatii = models.TextField(null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        pass


class Finisaj(models.Model):
    """
    Capitol: Fotografii Biserica
    """

    biserica = models.OneToOneField('Biserica', on_delete=models.CASCADE)
    finisaj_exterior_tip = models.ManyToManyField('nomenclatoare.FinisajExterior', blank=True)
    finisaj_exterior_observatii = models.TextField(null=True, blank=True)

    # finisaj_actual_invelitoare = models.ForeignKey('FinisajInvelitoare', on_delete=models.SET_NULL, null=True, blank=True)
    # finisaj_tambur_turn = models.ForeignKey('FinisajInvelitoare', related_name='finisaje_tambur_turn', on_delete=models.SET_NULL, null=True, blank=True)

    completare = models.FloatField(default=0)
    missing_fields = models.JSONField(null=True, blank=True)

    history = HistoricalRecords()
    class Meta:
        ordering = ["biserica__the_order"]
        verbose_name_plural = "3.2 Finisaje"

    def __str__(self):
        return f"Finisaj Artistica {self.biserica.nume}"

    


    def save(self, *args, **kwargs):
        completare = get_completare(self)
        self.completare = completare[0]
        self.missing_fields = completare[1]
        super().save(*args, **kwargs)


class PicturaExterioara(models.Model):
    """
    Description: Model Description
    """
    componenta_artistica = models.ForeignKey('ComponentaArtistica', on_delete=models.CASCADE)

    localizare = models.ForeignKey('nomenclatoare.LocalizarePictura', on_delete=models.SET_NULL, null=True, blank=True, related_name='localizari_exterioare')
    localizare_detalii = models.TextField(null=True, blank=True)
    tehnica = models.ForeignKey('nomenclatoare.TehnicaPictura', on_delete=models.SET_NULL, null=True, blank=True)
    suport = models.ManyToManyField('nomenclatoare.SuportPictura', blank=True)
    numar_straturi_pictura = models.IntegerField(null=True, blank=True)

    sursa_datare = models.ManyToManyField('nomenclatoare.SursaDatare', related_name='componente_artistice_exterioare', blank=True)
    anul_picturii = models.IntegerField(null=True, blank=True)
    datare_prin_interval_timp = models.CharField(max_length=50, null=True, blank=True)
    datare_secol = models.ForeignKey('nomenclatoare.Secol', null=True, blank=True, on_delete=models.SET_NULL, related_name='localizari_exterioare')
    datare_detalii = models.TextField(null=True, blank=True)

    history = HistoricalRecords()

    class Meta:
        pass


class PicturaInterioara(models.Model):
    """
    Description: Model Description
    """
    componenta_artistica = models.ForeignKey('ComponentaArtistica', on_delete=models.CASCADE)

    localizare = models.ForeignKey('nomenclatoare.LocalizarePictura', verbose_name="Proporția de suprafață acoperită", on_delete=models.SET_NULL, null=True, blank=True, related_name='localizari_interioare')
    localizare_detalii = models.TextField(null=True, blank=True, verbose_name="Proporția de suprafață acoperită detalii",)
    tehnica_pictura = models.ForeignKey('nomenclatoare.TehnicaPictura', on_delete=models.SET_NULL, null=True, blank=True)
    suport = models.ManyToManyField('nomenclatoare.SuportPictura', blank=True)
    numar_straturi_pictura = models.IntegerField(null=True, blank=True)

    sursa_datare = models.ManyToManyField('nomenclatoare.SursaDatare', related_name='componente_artistice_interioare', blank=True)
    anul_picturii = models.IntegerField(null=True, blank=True)
    datare_prin_interval_timp = models.CharField(max_length=50, null=True, blank=True)
    datare_secol = models.ForeignKey('nomenclatoare.Secol', null=True, blank=True, on_delete=models.SET_NULL, related_name='localizari_interioare')
    datare_detalii = models.TextField(null=True, blank=True)


    history = HistoricalRecords()

    class Meta:
        pass

class ComponentaArtistica(models.Model):
    """
    Capitol: Fotografii Biserica
    """

    biserica = models.OneToOneField('Biserica', on_delete=models.CASCADE)

    proscomidie = models.BooleanField(default=False, verbose_name="Proscomidie în exteriorul altarului")
    suport_proscomidie = models.ManyToManyField('nomenclatoare.SuportPictura', blank=True)
    elemente_sculptate = models.BooleanField(default=False, verbose_name="Elemente sculptate / decoruri în biserică")
    elemente_detalii = models.TextField(null=True, blank=True, verbose_name="Elemente sculptate / decoruri în biserică observații")

    alte_icoane_vechi = models.BooleanField(default=False, verbose_name="Alte icoane vechi")
    alte_icoane_vechi_detalii = models.TextField(null=True, blank=True, help_text="Alte icoane vechi observații")

    obiecte_de_cult = models.ManyToManyField('nomenclatoare.ObiectCult', verbose_name="Obiecte de cult", blank=True)
    obiecte_de_cult_detalii = models.TextField(null=True, blank=True)

    mobiliere = models.ManyToManyField('nomenclatoare.Material', verbose_name="Mobilier", blank=True)
    mobiliere_detalii = models.TextField(null=True, blank=True, help_text="strane, scaun arhieresc, tetrapoade, bănucuțe, cuiere, anvone, cafas, cor")

    obiecte_instrainate = models.BooleanField(default=False, verbose_name="Obiecte de cult înstrăinate")
    obiecte_instrainate_detalii = models.TextField(null=True, blank=True, help_text="Observații privind înstrăinarea obiectelor de cult aparținătoare bisericii ")



    # Pictură exterioară aplicată
    # Pictură interioară aplicată


    # Iconostasul  (dintre naos și altar)
    iconostas_naos_altar_tip = models.ForeignKey('nomenclatoare.TipIconostas',verbose_name='Tip', null=True, blank=True, on_delete=models.SET_NULL, related_name='iconostasuri_naos_altar')
    iconostas_naos_altar_numar_intrari =  models.IntegerField(verbose_name='Număr intrări',null=True, blank=True)
    iconostas_naos_altar_tehnica = models.ManyToManyField('nomenclatoare.TehnicaIconostas',verbose_name='Tehnică', related_name='iconostasuri_naos_altar', blank=True)
    iconostas_naos_altar_registre = models.ManyToManyField('nomenclatoare.RegistruIconostas',verbose_name='Registru', related_name='iconostasuri_naos_altar', blank=True)
    iconostas_naos_altar_tip_usi = models.ManyToManyField('nomenclatoare.TipUsiIconostas',verbose_name='Tip uși', related_name='iconostasuri_naos_altar', blank=True)
    iconostas_naos_altar_detalii = models.TextField(verbose_name='Detalii', null=True, blank=True, help_text="Particularități ale iconostasului ce merită a fi precizate (de urmărit care este standardul de iconostas în zonă și care sunt eventualele deviații de la standard")

    iconostas_naos_altar_materiale = models.ManyToManyField('nomenclatoare.Material',verbose_name='Material', blank=True, related_name='iconostasuri_naos_altar')

    # Iconostasul  (dintre pronaos și naos)
    iconostas_pronaos_naos_tip = models.ForeignKey('nomenclatoare.TipIconostas',verbose_name='Tip', null=True, blank=True, on_delete=models.SET_NULL, related_name='iconostasuri_pronaos_naos')
    iconostas_pronaos_naos_material = models.ForeignKey('nomenclatoare.Material',verbose_name='Material', null=True, blank=True, on_delete=models.SET_NULL, related_name='iconostasuri_pronaos_naos')
    iconostas_pronaos_naos_numar_intrari =  models.IntegerField(verbose_name='Număr intrări',null=True, blank=True)
    iconostas_pronaos_naos_tehnica = models.ManyToManyField('nomenclatoare.TehnicaIconostas', verbose_name='Tehnica',related_name='iconostasuri_pronaos_naos', blank=True)
    iconostas_pronaos_naos_detalii = models.TextField(verbose_name='Detalii',null=True, blank=True, help_text="Particularități ale iconostasului ce merită a fi precizate (de urmărit care este standardul de iconostas în zonă și care sunt eventualele deviații de la standard")

    # Altar
    altar_placa_mesei = models.ManyToManyField('nomenclatoare.Material',verbose_name='Placa mesei', blank=True, related_name='placa_mesei')
    altar_piciorul_mesei = models.ManyToManyField('nomenclatoare.Material',verbose_name='Piciorul mesei', blank=True, related_name='piciorul_mesei')
    altar_decor = models.ForeignKey('nomenclatoare.TehnicaIconostas', verbose_name = "Decor", on_delete=models.SET_NULL, null=True, blank=True, related_name='decoruri_altar')
    altar_detalii = models.TextField(null=True, blank=True, verbose_name='Detalii')

    completare = models.FloatField(default=0)
    missing_fields = models.JSONField(null=True, blank=True)

    history = HistoricalRecords()
    class Meta:
        ordering = ["biserica__the_order"]
        verbose_name_plural = "3.3 Componenta Artistică"

    def __str__(self):
        return f"Componenta Artistica {self.biserica.nume}"

    

    def save(self, *args, **kwargs):
        completare = get_completare(self)
        self.completare = completare[0]
        self.missing_fields = completare[1]
        super().save(*args, **kwargs)
