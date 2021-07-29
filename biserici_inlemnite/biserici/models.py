from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from guardian.shortcuts import get_objects_for_user, assign_perm, remove_perm
from simple_history.models import HistoricalRecords
from simple_history import register

from nomenclatoare import models as nmodels


User = get_user_model()
register(User, app=__package__)

IDENTIFICARE_DOC_CADASTRALE = (
    (1, 'Da'),
    (2, 'Nu'),
    (3, 'În curs de'),
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


class Biserica(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=50)

    
    history = HistoricalRecords()
    
    class Meta:
        verbose_name_plural = "Biserici"

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
    proprietate_actuala = models.ForeignKey('nomenclatoare.ProprietateBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici_initiale')
    proprietate_detalii = models.TextField(null=True, blank=True)
    proprietar_actual = models.TextField(null=True, blank=True)
    inscriere_documente_cadastrale = models.IntegerField(choices=IDENTIFICARE_DOC_CADASTRALE, null=True, blank=True)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Identificare Biserici"

    def __str__(self):
        return f"Identificare {self.biserica.nume}"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_judet = self.judet

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
    toponim_sursa  = models.TextField(null=True, blank=True)
    relatia_cu_cimitirul = models.ForeignKey('nomenclatoare.RelatieCimitir', null=True, blank=True, on_delete=models.SET_NULL)
    peisagistica_sitului = models.ManyToManyField('nomenclatoare.PeisagisticaSit')


    # Ansamblu construit
    elemente = models.ManyToManyField('nomenclatoare.ElementBiserica', help_text="Elemente ansamblu construit")
    detalii_elemente = models.TextField(null=True, blank=True)

    elemente_importante = models.ManyToManyField('nomenclatoare.ElementImportant', help_text="Elemente ansamblu construit")
    detalii_elemente_importante = models.TextField(null=True, blank=True)

    

    amplasament = models.ForeignKey('nomenclatoare.AmplasamentBiserica', null=True, blank=True, on_delete=models.SET_NULL)
    topografie = models.ForeignKey('nomenclatoare.TopografieBiserica', null=True, blank=True, on_delete=models.SET_NULL)
    toponim = models.CharField(max_length=150, null=True, blank=True, help_text="denumirea locului")
    toponim_sursa  = models.TextField(null=True, blank=True)
    relatia_cu_cimitirul = models.ForeignKey('nomenclatoare.RelatieCimitir', null=True, blank=True, on_delete=models.SET_NULL)



    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Descriere Biserici"

    def __str__(self):
        return f"Descriere {self.biserica.nume}"


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
    element = models.ForeignKey('nomenclatoare.ElementBiserica', on_delete=models.CASCADE)
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
    ctitori = models.ManyToManyField('nomenclatoare.Persoana', through=nmodels.CtitorBiserica, related_name='ctitor')
    mesteri = models.ManyToManyField('nomenclatoare.Persoana', through=nmodels.MesterBiserica, related_name='mester')
    zugravi = models.ManyToManyField('nomenclatoare.Persoana', through=nmodels.ZugravBiserica, related_name='zugrav')
    personalitati = models.ManyToManyField('nomenclatoare.Persoana', through=nmodels.PersonalitateBiserica, related_name='personalitate')
    evenimente = models.ManyToManyField('nomenclatoare.Eveniment', through=nmodels.EvenimentBiserica)

    mutari_biserica = models.ManyToManyField('nomenclatoare.Localitate', through=nmodels.MutareBiserica)


    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Istoric Biserici"
        

    def __str__(self):
        return f"Istoric {self.biserica.nume}"

class Patrimoniu(models.Model):
    """
    Capitol: Valoare Patrimoniu Cultural Biserica
    """
    biserica = models.OneToOneField('Biserica', on_delete=models.CASCADE)

    vechime = models.IntegerField(choices=NR15, null=True, blank=True, help_text= "Printr-un algorim definit se va da automat o notă de la 1-5 în funcție de vechimea monumentului si a picturii descrise conform OMCC2682/2003 ETC")
    vechime_detalii = models.TextField(null=True, blank=True)
    integritate = models.IntegerField(choices=NR15, null=True, blank=True, help_text= "Integritate / Autenticitate")
    integritate_detalii = models.TextField(null=True, blank=True)
    unicitate = models.IntegerField(choices=NR15, null=True, blank=True, help_text= "Unicitate / raritate")
    unicitate_detalii = models.TextField(null=True, blank=True)
    valoare_memoriala = models.IntegerField(choices=NR15, null=True, blank=True, help_text= "evenimente, personalități")
    valoare_memoriala_detalii = models.TextField(null=True, blank=True)
    peisaj_cultural = models.IntegerField(choices=NR15, null=True, blank=True, help_text= "Parte definitorie a peisajului cultural al zonei")
    peisaj_cultural_detalii = models.TextField(null=True, blank=True)
    valoare_sit = models.IntegerField(choices=NR15, null=True, blank=True, help_text= "Valoarea sitului împreună cu toate componentele ansamblului din care face parte, ținând cont de integritate, autenticitate, estetică peisageră, biodiversitate, etc. SUBIECTIV")
    valoare_sit_detalii = models.TextField(null=True, blank=True, help_text= "Descriere a elementelor valoroase, particulare")
    estetica = models.IntegerField(choices=NR15, null=True, blank=True, help_text= "Estetică / Arhitectură")
    estetica_detalii = models.TextField(null=True, blank=True)
    mestesug = models.IntegerField(choices=NR15, null=True, blank=True, help_text= "Meșteșug (calitatea muncii -  a se vedea golurile dintre lemne (dintre bârne în general dar în special la așezarea elementelor orizontale peste cele verticale))")
    mestesug_detalii = models.TextField(null=True, blank=True)
    pictura = models.IntegerField(choices=NR15, null=True, blank=True, )
    pictura_detalii = models.TextField(null=True, blank=True)
    folosinta_actuala = models.IntegerField(choices=NR135, null=True, blank=True, help_text= "Folosință actuală / singura biserică din sat / loc al patrimoniului imaterial")
    folosinta_actuala_detalii = models.TextField(null=True, blank=True)
    relevanta_actuala = models.IntegerField(choices=NR135, null=True, blank=True, help_text= "Relevanța actuală pentru comunitatea locală (prin reprezentanții săi: preot, crâsnic, învățător, familii de bază)")
    relevanta_actuala_detalii = models.TextField(null=True, blank=True)
    potential = models.IntegerField(choices=NR135, null=True, blank=True, help_text= "Potențialul de beneficii aduse comunității locale")
    potential_detalii = models.TextField(null=True, blank=True)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Valoare Patrimoniu"

    def __str__(self):
        return f"Valoare patrimoniu cultural {self.biserica.nume}"


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


    # Obiecte de cult
    stare_icoane_istorice = models.IntegerField(choices=NR15, null=True, blank=True)
    stare_icoane_istorice_detalii = models.TextField( null=True, blank=True)
    starea_obiecte_de_cult = models.IntegerField(choices=NR15, null=True, blank=True)
    starea_obiecte_de_cult_detalii = models.TextField( null=True, blank=True)
    starea_mobilier = models.IntegerField(choices=NR15, null=True, blank=True)
    starea_mobilier_detalii = models.TextField( null=True, blank=True)


    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Stare conservare Biserici"

    def __str__(self):
        return f"Stare conservare {self.biserica.nume}"


class FotografieAnsamblu(models.Model):
    """
    Description: Model Description
    """
    fotografii = models.ForeignKey('Fotografii', on_delete=models.CASCADE)
    poza = models.ImageField(upload_to='fotografii', max_length=250)
    detalii = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=150, null=True, blank=True)

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

    class Meta:
        pass


class Fotografii(models.Model):
    """
    Capitol: Fotografii Biserica
    """

    biserica = models.OneToOneField('Biserica', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Fotografii"

