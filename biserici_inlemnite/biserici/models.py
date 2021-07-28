from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from guardian.shortcuts import get_objects_for_user, assign_perm, remove_perm

User = get_user_model()

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


class Judet(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=50)
    cod = models.CharField(max_length=2)
    

    class Meta:
        verbose_name_plural = "_Județe"

    def __str__(self):
        return self.nume

class Localitate(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=50)
    judet = models.ForeignKey('Judet', on_delete=models.CASCADE)
    

    class Meta:
        verbose_name_plural = "_Localități"


    def __str__(self):
        return self.nume


class Biserica(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=50)

    last_edit_date = models.DateTimeField(auto_now=True)
    last_edit_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Biserici"

    def __str__(self):
        return self.nume


    def completare(self):
        return 0

class FunctiuneBiserica(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "_Funcțiuni Biserică"

    def __str__(self):
        return self.nume


class StatutBiserica(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "_Statuturi Biserică"

    def __str__(self):
        return self.nume


class CultBiserica(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "_Culturi Biserică"

    def __str__(self):
        return self.nume


class UtilizareBiserica(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "_Utilizări Biserică"

    def __str__(self):
        return self.nume


class SingularitateBiserica(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "_Singularități Biserică"

    def __str__(self):
        return self.nume


class ProprietateBiserica(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "_Proprietăți Biserică"

    def __str__(self):
        return self.nume


class Identificare(models.Model):
    """
    Capitol: Identificare Biserica
    """
    biserica = models.OneToOneField('Biserica', on_delete=models.CASCADE)
    judet = models.ForeignKey('Judet', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici')
    localitate = models.ForeignKey('Localitate', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici')
    latitudine = models.FloatField(null=True, blank=True)
    longitudine = models.FloatField(null=True, blank=True)
    statut = models.ForeignKey('StatutBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici')
    denumire_actuala = models.CharField(max_length=150, null=True, blank=True)
    denumire_precedenta = models.CharField(max_length=150, null=True, blank=True)
    denumire_locala = models.CharField(max_length=150, null=True, blank=True)
    denumire_oberservatii = models.TextField(null=True, blank=True)
    cult = models.ForeignKey('CultBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici')
    utilizare = models.ForeignKey('UtilizareBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici')
    utilizare_detalii = models.TextField(null=True, blank=True)
    singularitate = models.ForeignKey('SingularitateBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici')
    singularitate_detalii = models.TextField(null=True, blank=True)
    functiune = models.ForeignKey('FunctiuneBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici')
    functiune_detalii = models.TextField(null=True, blank=True)
    functiune_initiala = models.ForeignKey('FunctiuneBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici_initiale')
    functiune_initiala_detalii = models.TextField(null=True, blank=True)
    proprietate_actuala = models.ForeignKey('ProprietateBiserica', null=True, blank=True, on_delete=models.SET_NULL, related_name='biserici_initiale')
    proprietate_detalii = models.TextField(null=True, blank=True)
    proprietar_actual = models.TextField(null=True, blank=True)
    inscriere_documente_cadastrale = models.IntegerField(choices=IDENTIFICARE_DOC_CADASTRALE, null=True, blank=True)

    last_edit_date = models.DateTimeField(auto_now=True)
    last_edit_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Identificare Biserici"

    def __str__(self):
        return f"Identificare {self.biserica.nume}"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_judet = self.judet

    def save(self, *args, **kwargs):
        print(kwargs)
        if self.judet:
            if self.__original_judet != self.judet or kwargs.get('force_update', False) == True:
                biserica = self.biserica

                judet_biserica = self.judet.nume
                grup_judet, _ = Group.objects.get_or_create(name=judet_biserica)
                assign_perm('view_biserica', grup_judet, biserica)
                assign_perm('change_biserica', grup_judet, biserica)

                for t in ['identificare', 'istoric', 'descriere', 'patrimoniu', 'conservare']:
                        assign_perm(f'view_{t}', grup_judet, getattr(biserica, t))
                        assign_perm(f'change_{t}', grup_judet, getattr(biserica, t))

                for judet in Group.objects.exclude(name=judet_biserica):
                    remove_perm('view_biserica', judet, biserica)
                    remove_perm('change_biserica', judet, biserica)

                    for t in ['identificare', 'istoric', 'descriere', 'patrimoniu', 'conservare']:
                        remove_perm(f'view_{t}', judet, getattr(biserica, t))
                        remove_perm(f'change_{t}', judet, getattr(biserica, t))
        super().save(*args, **kwargs)


class MutareBiserica(models.Model):
    """
    Description: Model Description
    """
    istoric = models.ForeignKey('Istoric', on_delete=models.CASCADE)
    localitate = models.ForeignKey('Localitate', null=True, blank=True, on_delete=models.SET_NULL)
    latitudine = models.FloatField(null=True, blank=True)
    longitudine = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name_plural = '_Mutări Biserică'


class SursaDatare(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = '_Surse Datări'

    def __str__(self):
        return self.nume


class StudiuDendocronologic(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)
    fisier = models.FileField()
    an = models.IntegerField(null=True, blank=True)
    autor = models.CharField(max_length=150, null=True, blank=True)
    detalii = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = '_Studii dendocronologice'

    def __str__(self):
        return f"{self.nume} - {self.autor} ({self.an})"

class Persoana(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = '_Persoane'

    def __str__(self):
        return self.nume


class Eveniment(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = '_Evenimente'

    def __str__(self):
        return self.nume


class CtitorBiserica(models.Model):
    """
    Description: Model Description
    """
    persoana = models.ForeignKey('Persoana', on_delete=models.CASCADE)
    istoric = models.ForeignKey('Istoric', on_delete=models.CASCADE)
    detalii = models.TextField()
    sursa = models.TextField()

    class Meta:
        verbose_name_plural = 'Ctitori'

    def __str__(self):
        return self.nume

class ZugravBiserica(models.Model):
    """
    Description: Model Description
    """
    persoana = models.ForeignKey('Persoana', on_delete=models.CASCADE)
    istoric = models.ForeignKey('Istoric', on_delete=models.CASCADE)
    detalii = models.TextField()
    sursa = models.TextField()

    class Meta:
        verbose_name_plural = 'Zugravi'

    def __str__(self):
        return self.nume

class MesterBiserica(models.Model):
    """
    Description: Model Description
    """
    persoana = models.ForeignKey('Persoana', on_delete=models.CASCADE)
    istoric = models.ForeignKey('Istoric', on_delete=models.CASCADE)
    detalii = models.TextField()
    sursa = models.TextField()

    class Meta:
        verbose_name_plural = 'Meșteri'

    def __str__(self):
        return self.nume

class PersonalitateBiserica(models.Model):
    """
    Description: Model Description
    """
    persoana = models.ForeignKey('Persoana', on_delete=models.CASCADE)
    istoric = models.ForeignKey('Istoric', on_delete=models.CASCADE)
    detalii = models.TextField()
    sursa = models.TextField()

    class Meta:
        verbose_name_plural = '_Personalități Biserică'

    def __str__(self):
        return self.nume


class EvenimentBiserica(models.Model):
    """
    Description: Model Description
    """
    eveniment = models.ForeignKey('Eveniment', on_delete=models.CASCADE)
    istoric = models.ForeignKey('Istoric', on_delete=models.CASCADE)
    detalii = models.TextField()
    sursa = models.TextField()

    class Meta:
        verbose_name_plural = 'Evenimente Istorice'

    def __str__(self):
        return self.nume


class Studiu(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)
    fisier = models.FileField()

    class Meta:
        verbose_name_plural = '_Studii'

    def __str__(self):
        return self.nume


class Secol(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = '_Secole'

    def __str__(self):
        return self.nume



class StudiuIstoric(models.Model):
    """
    Description: Model Description
    """
    istoric = models.ForeignKey('Istoric', on_delete=models.CASCADE)
    nume = models.CharField(max_length=150)
    fisier = models.FileField()
    drepturi_de_autor = models.TextField()

    class Meta:
        verbose_name_plural = 'Studii Istorice'

    def __str__(self):
        return self.studiu.nume



class Istoric(models.Model):
    """
    Capitol: Istoric Biserica
    """

    biserica = models.OneToOneField('Biserica', on_delete=models.CASCADE)
    sursa_datare = models.ManyToManyField(SursaDatare, related_name='biserici')
    anul_constructiei = models.IntegerField(null=True, blank=True)
    datare_prin_interval_timp = models.CharField(max_length=50, null=True, blank=True)
    datare_secol = models.ForeignKey('Secol', null=True, blank=True, on_delete=models.CASCADE, related_name='biserici')
    datare_secol_detalii  = models.TextField(null=True, blank=True)
    datare_secol_sursa  = models.TextField(null=True, blank=True)
    studiu_dendocronologic = models.ForeignKey('StudiuDendocronologic', null=True, blank=True, on_delete=models.CASCADE)
    pisanie_traducere = models.TextField(null=True, blank=True)
    pisanie_secol_detalii  = models.TextField(null=True, blank=True)
    pisanie_secol_sursa  = models.TextField(null=True, blank=True)
    ctitori = models.ManyToManyField('Persoana', through=CtitorBiserica, related_name='ctitor')
    mesteri = models.ManyToManyField('Persoana', through=MesterBiserica, related_name='mester')
    zugravi = models.ManyToManyField('Persoana', through=ZugravBiserica, related_name='zugrav')
    personalitati = models.ManyToManyField('Persoana', through=PersonalitateBiserica, related_name='personalitate')
    evenimente = models.ManyToManyField('Eveniment', through=EvenimentBiserica)

    mutari_biserica = models.ManyToManyField(Localitate, through=MutareBiserica)

    last_edit_date = models.DateTimeField(auto_now=True)
    last_edit_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Istoric Biserici"

    def __str__(self):
        return f"Istoric {self.biserica.nume}"


class Descriere(models.Model):
    """
    Capitol: Descriere Biserica
    """

    biserica = models.OneToOneField('Biserica', on_delete=models.CASCADE)

    last_edit_date = models.DateTimeField(auto_now=True)
    last_edit_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Descriere Biserici"

    def __str__(self):
        return f"Descriere {self.biserica.nume}"


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

    last_edit_date = models.DateTimeField(auto_now=True)
    last_edit_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

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

    last_edit_date = models.DateTimeField(auto_now=True)
    last_edit_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Stare conservare Biserici"

    def __str__(self):
        return f"Stare conservare {self.biserica.nume}"