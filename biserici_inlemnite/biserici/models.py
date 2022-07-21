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


class Biserica(SortableMixin):
    """
    Description: Model Description
    """

    nume = models.CharField(max_length=50)
    the_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    history = HistoricalRecords()

    class Meta:
        ordering = ["the_order"]
        verbose_name_plural = " Biserici"

    def __str__(self):
        return self.nume


class Fotografie(models.Model):
    """
    Description: Model Description
    """

    titlu = models.CharField(max_length=150, null=True, blank=True)
    fisier = models.ImageField(upload_to="fotografii", max_length=200)
    copyright = models.CharField(max_length=150, null=True, blank=True)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Fotografii"

    def __str__(self):
        return self.titlu


class Interventie(models.Model):
    denumire = models.CharField("Denumire", max_length=250, null=True, blank=True)
    datat = models.BooleanField("Datat", default=False)
    an = models.IntegerField(null=True, blank=True, verbose_name="An")
    neconforma = models.BooleanField("Neconformă", default=False)
    sursa = models.TextField("Sursa", null=True, blank=True)
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class StareConservare(models.Model):
    nota = models.ForeignKey(
        "fragmente.NotaStareConservare",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    tipul_de_degradari = models.ManyToManyField("fragmente.TipDegradare", blank=True)
    descriere_degradari = models.TextField("Descriere degradări", null=True, blank=True)
    tipul_riscului = models.ManyToManyField("fragmente.TipRisc", blank=True)
    descriere_risc = models.TextField("Descriere risc", null=True, blank=True)
    interventii_necesare = models.ManyToManyField("fragmente.InterventiiNecesare", blank=True)
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class IdentificareFrecventaUtilizarii(models.Model):
    """
    Rubrica: Identificare / Frecventa Utilizarii
    """

    frecventa_utilizarii = models.ForeignKey(
        "fragmente.FrecventaUtilizarii",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Frecvența utilizării",
    )
    observatii = models.TextField("Observații", null=True, blank=True)


class IdentificareSingularitate(models.Model):
    """
    Rubrica: Identificare / Singularitate
    """

    singularitate = models.ForeignKey(
        "fragmente.Singularitate",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    observatii = models.TextField("Observații", null=True, blank=True)


class Identificare(models.Model):
    """
    Capitol: Identificare Biserica
    """

    biserica = models.OneToOneField("Biserica", on_delete=models.CASCADE, related_name="identificare")
    codul_lmi = models.CharField("Codul LMI", max_length=50, null=True, blank=True)
    categoria = models.ForeignKey(
        "fragmente.CategorieObiectiv",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    statut = models.ForeignKey(
        "fragmente.Statut",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    denumire_oficiala = models.CharField("Denumire oficială actuală LMI", max_length=250, null=True, blank=True)
    hram = models.ForeignKey(
        "fragmente.Hram",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    cult = models.ForeignKey(
        "fragmente.Cult",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    frecventa_utilizarii = models.ForeignKey(
        "IdentificareFrecventaUtilizarii",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    singularitate = models.ForeignKey(
        "IdentificareSingularitate",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    history = HistoricalRecords()

    class Meta:
        ordering = ["biserica__the_order"]
        verbose_name = "Identificare / Denumire / Funcțiune"
        verbose_name_plural = "Identificare / Denumire / Funcțiune"

    def __str__(self):
        return f"Identificare {self.biserica.nume}"


class LocalizareUnitatiTeritoriale(models.Model):
    """
    Description: Model Description
    """

    stat = models.CharField(max_length=50, null=True, blank=True)
    regiune = models.CharField(max_length=50, null=True, blank=True)
    uat_1 = models.CharField("UAT 1 (superior)", max_length=50, null=True, blank=True)
    uat = models.CharField("UAT (intermediar)", max_length=50, null=True, blank=True)
    uat_2 = models.CharField("UAT 2 (inferior)", max_length=50, null=True, blank=True)
    ut = models.CharField("UT", max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "Unități Teritoriale"


class LocalizareAdresaCoordonateGPS(models.Model):
    """
    Description: Model Description
    """

    latitudine = models.FloatField(null=True, blank=True)
    longitudine = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = "Unități Teritoriale"


class LocalizareAdresa(models.Model):
    """
    Description: Model Description
    """

    coordonate_gps = models.ForeignKey(
        "LocalizareAdresaCoordonateGPS",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Coordonate GPS",
    )
    tip_artera = models.ForeignKey(
        "fragmente.TipArtera",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    denumire_artera = models.CharField("Denumire Arteră", max_length=50, null=True, blank=True)
    nr_postal = models.IntegerField("Număr Poștal", null=True, blank=True)
    cod_postal = models.IntegerField("Cod Poștal", null=True, blank=True)
    observatii = models.TextField("Observații", null=True, blank=True)

    class Meta:
        verbose_name = "Adresă"


class LocalizareReferinteCadastrale(models.Model):
    """
    Description: Model Description
    """

    nr_carte_funciara = models.CharField("Număr carte funciară", max_length=50, null=True, blank=True)
    nr_cadastru = models.IntegerField("Număr cadastru", null=True, blank=True)
    nr_cop_cadastru = models.CharField("Număr cop conform cadastru", max_length=150, null=True, blank=True)
    nr_parcela = models.IntegerField("Număr parcelă / topografic", null=True, blank=True)
    suprafata_parcela = models.IntegerField("Suprafață parcelă", null=True, blank=True)
    observatii = models.TextField("Observații", null=True, blank=True)

    class Meta:
        verbose_name = "Referințe Cadastrale"


class LocalizareRegimulDeProprietate(models.Model):
    """
    Description: Model Description
    """

    tip_regim = models.ForeignKey(
        "fragmente.TipRegimProprietate",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Tipul Regimului de Proprietate",
    )
    observatii = models.TextField("Observații", null=True, blank=True)

    class Meta:
        verbose_name = "Regimul de Proprietate"


class Localizare(models.Model):
    """
    Capitol: Localizare Biserica
    """

    biserica = models.OneToOneField("Biserica", on_delete=models.CASCADE, related_name="localizare")
    unitati_teritoriale = models.ForeignKey(
        "LocalizareUnitatiTeritoriale",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Unități Teritoriale",
    )
    adresa = models.ForeignKey(
        "LocalizareAdresa",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Adresă",
    )
    referinte_cadastrale = models.ForeignKey(
        "LocalizareReferinteCadastrale",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Referințe Cadastrale",
    )
    regim_proprietate = models.ForeignKey(
        "LocalizareRegimulDeProprietate",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Regimul de Proprietate",
    )

    history = HistoricalRecords()

    class Meta:
        ordering = ["biserica__the_order"]
        verbose_name = "Localizare / Proprietate"
        verbose_name_plural = "Localizare / Proprietate"

    def __str__(self):
        return f"Localizare {self.biserica.nume}"


class RepereGeograficeFormaRelief(models.Model):
    tip_forma = models.ForeignKey(
        "fragmente.TipFormaRelief",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Tipul Formei de Relief",
    )
    denumire = models.CharField("Denumire Formă de Relief", max_length=150, null=True, blank=True)
    observatii = models.TextField("Observații", null=True, blank=True)


class RepereGeograficeReperHidrografic(models.Model):
    tip_reper = models.ForeignKey(
        "fragmente.TipReperHidrografic",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Tipul Reperului Hidrografic",
    )
    denumire = models.CharField("Denumire Reper Hidrografic", max_length=150, null=True, blank=True)
    observatii = models.TextField("Observații", null=True, blank=True)


class RepereGeograficeZoneNaturale(models.Model):
    tip_zone = models.ManyToManyField(
        "fragmente.TipZoneNaturale",
        blank=True,
        verbose_name="Tip Zone Naturale",
    )
    observatii = models.TextField("Observații", null=True, blank=True)


class RepereGeografice(models.Model):
    """
    Capitol: Localizare Biserica
    """

    biserica = models.OneToOneField("Biserica", on_delete=models.CASCADE, related_name="repere_geografice")

    forma_relief = models.ForeignKey(
        "RepereGeograficeFormaRelief",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Formă de relief",
    )
    reper_hidrografic = models.ForeignKey(
        "RepereGeograficeReperHidrografic",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Reper Hidrografic",
    )
    zone_naturale = models.ForeignKey(
        "RepereGeograficeZoneNaturale",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Zone Naturale (Arii Protejate)",
    )

    history = HistoricalRecords()

    class Meta:
        ordering = ["biserica__the_order"]
        verbose_name = "Repere Geografice"
        verbose_name_plural = "Repere Geografice"

    def __str__(self):
        return f"Repere Geografice {self.biserica.nume}"


class Datare(models.Model):
    an = models.IntegerField(null=True, blank=True, verbose_name="An")
    interval_timp = models.CharField("Datare prin interval de timp", max_length=50, null=True, blank=True)
    secol = models.ManyToManyField(
        "fragmente.Secol",
        blank=True,
        verbose_name="Secol",
    )


class JustificareDatare(models.Model):
    categorie = models.ForeignKey(
        "fragmente.JustificareDatare",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Justificare Datare",
    )
    observatii = models.TextField("Observații", null=True, blank=True)
    foto = models.ManyToManyField("Fotografie", blank=True)


class IstoricScurtIstoric(models.Model):
    sinteza = models.TextField("Sinteză istorică", null=True, blank=True)
    bibliografie = models.ManyToManyField(
        "fragmente.Bibliografie",
        blank=True,
        verbose_name="Bibliografie",
    )
    datare = models.ForeignKey(
        "Datare",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Pisanie",
    )
    justificare_datare = models.ManyToManyField("JustificareDatare", blank=True, verbose_name="Pisanie")


class IstoricPisanie(models.Model):
    tip = models.ManyToManyField(
        "fragmente.TipPisanie",
        blank=True,
        verbose_name="Tip Pisanie",
    )
    text = models.TextField("Text", null=True, blank=True)


class IstoricPersoana(models.Model):
    nume = models.CharField("Nume", max_length=150, null=True, blank=True)
    observatii = models.TextField("Observații", null=True, blank=True)
    sursa = models.TextField("Sursa", null=True, blank=True)
    foto = models.ManyToManyField("Fotografie", blank=True)


class IstoricEveniment(models.Model):
    observatii = models.TextField("Observații", null=True, blank=True)


class IstoricMutare(models.Model):
    localitate = models.ForeignKey(
        "fragmente.Localitate",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Tipul Formei de Relief",
    )
    adresa = models.TextField("Adresa", null=True, blank=True)
    latitudine = models.FloatField(null=True, blank=True)
    longitudine = models.FloatField(null=True, blank=True)
    observatii = models.TextField("Observații", null=True, blank=True)
    sursa = models.TextField("Sursa", null=True, blank=True)


class Istoric(models.Model):
    """
    Capitol: Localizare Biserica
    """

    biserica = models.OneToOneField("Biserica", on_delete=models.CASCADE, related_name="istoric")

    scurt_istoric = models.ForeignKey(
        "IstoricScurtIstoric",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Scurt Istoric",
    )
    pisanie = models.ForeignKey(
        "IstoricPisanie",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Pisanie",
    )
    ctitori = models.ManyToManyField(
        "IstoricPersoana",
        blank=True,
        verbose_name="Ctitori",
        related_name="ctitori",
    )
    mesteri = models.ManyToManyField(
        "IstoricPersoana",
        blank=True,
        verbose_name="Meșteri",
        related_name="mesteri",
    )
    zugravi = models.ManyToManyField(
        "IstoricPersoana",
        blank=True,
        verbose_name="Zugravi",
        related_name="zugravi",
    )
    personalitati = models.ManyToManyField(
        "IstoricPersoana",
        blank=True,
        verbose_name="Personalități",
        related_name="personalitati",
    )
    evenimente = models.ManyToManyField(
        "IstoricEveniment",
        blank=True,
        verbose_name="Evenimente",
        related_name="evenimente",
    )
    mutari = models.ManyToManyField(
        "IstoricMutare",
        blank=True,
        verbose_name="Mutări",
        related_name="mutari",
    )

    history = HistoricalRecords()

    class Meta:
        ordering = ["biserica__the_order"]
        verbose_name = "Istoric"
        verbose_name_plural = "Istoric"

    def __str__(self):
        return f"Istoric {self.biserica.nume}"

    cadru = models.CharField("Nume", max_length=150, null=True, blank=True)


class PeisajPeisajCulturalCadru(models.Model):
    tip = models.ForeignKey(
        "fragmente.TipCadruPeisaj",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Tip Cadru",
    )
    foto = models.ManyToManyField("Fotografie", blank=True)


class PeisajPeisajCulturalPatrimoniuImaterial(models.Model):
    exista = models.BooleanField("Există", default=False)
    descriere = models.TextField("Descriere", null=True, blank=True)
    foto = models.ManyToManyField("Fotografie", blank=True)


class PeisajPeisajCultural(models.Model):
    sinteza = models.TextField("Sinteză", null=True, blank=True)
    cadru = models.ForeignKey(
        "PeisajPeisajCulturalCadru",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    patrimoniu_imaterial = models.ForeignKey(
        "PeisajPeisajCulturalPatrimoniuImaterial",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Patrimoniu Imaterial",
    )
    observatii = models.TextField("Observații", null=True, blank=True)


class PeisajAmplasamentLoc(models.Model):
    tip_loc = models.ManyToManyField("fragmente.TipLoc", blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)
    observatii = models.TextField("Observații", null=True, blank=True)


class PeisajAmplasamentToponim(models.Model):
    exista = models.BooleanField("Există", default=False)
    denumire = models.TextField("Denumire", null=True, blank=True)
    sursa = models.TextField("Sursă informații", null=True, blank=True)
    observatii = models.TextField("Observații", null=True, blank=True)


class PeisajAmplasamentRelatiaCuCimitirul(models.Model):
    tip_relatie = models.ForeignKey(
        "fragmente.TipRelatieCuCimitirul",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    observatii = models.TextField("Observații", null=True, blank=True)


class PeisajAmplasament(models.Model):
    loc = models.ForeignKey(
        "PeisajAmplasamentLoc", on_delete=models.SET_NULL, verbose_name="Loc", null=True, blank=True
    )
    toponim = models.ForeignKey(
        "PeisajAmplasamentToponim", on_delete=models.SET_NULL, verbose_name="Toponim", null=True, blank=True
    )
    relatia_cu_cimitirul = models.ForeignKey(
        "PeisajAmplasamentRelatiaCuCimitirul",
        on_delete=models.SET_NULL,
        verbose_name="Relația cu cimitirul",
        null=True,
        blank=True,
    )
    interventii = models.ManyToManyField("Interventie", blank=True, verbose_name="Intervenții")
    stare_conservare = models.ForeignKey(
        "StareConservare", on_delete=models.SET_NULL, verbose_name="Stare Conservare", null=True, blank=True
    )


class PeisajAnsambluConstruitElementArhitectural(models.Model):
    tip = models.ForeignKey(
        "fragmente.TipElementArhitectural",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Tip",
    )
    element_important = models.BooleanField("Element Important", default=False)
    element_disonant = models.BooleanField("Element Disonant", default=False)
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class PeisajAnsambluConstruitElementPeisaj(models.Model):
    tip = models.ForeignKey(
        "fragmente.TipElementDePeisaj",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Tip",
    )
    element_important = models.BooleanField("Element Important", default=False)
    element_disonant = models.BooleanField("Element Disonant", default=False)
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class PeisajAnsambluConstruit(models.Model):
    sinteza = models.TextField("Sinteză", null=True, blank=True)
    elemente_arhitecturale = models.ManyToManyField(
        "PeisajAnsambluConstruitElementArhitectural",
        blank=True,
        verbose_name="Elemente Arhitecturale",
    )
    elemente_de_peisaj = models.ManyToManyField(
        "PeisajAnsambluConstruitElementPeisaj",
        blank=True,
        verbose_name="Elemente de Peisaj",
    )
    interventii = models.ManyToManyField("Interventie", blank=True, verbose_name="Intervenții")
    stare_conservare = models.ForeignKey(
        "StareConservare",
        on_delete=models.SET_NULL,
        verbose_name="Stare Conservare",
        null=True,
        blank=True,
    )


class Peisaj(models.Model):
    """
    Capitol: Peisaj Biserica
    """

    biserica = models.OneToOneField("Biserica", on_delete=models.CASCADE, related_name="peisaj")

    peisaj_cultural = models.ForeignKey(
        "PeisajPeisajCultural",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Scurt Istoric",
    )
    amplasament = models.ForeignKey(
        "PeisajAmplasament",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Pisanie",
    )
    ansamblu_construit = models.ForeignKey(
        "PeisajAnsambluConstruit",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Pisanie",
    )

    history = HistoricalRecords()

    class Meta:
        ordering = ["biserica__the_order"]
        verbose_name = "Peisaj"
        verbose_name_plural = "Peisaj"

    def __str__(self):
        return f"Peisaj {self.biserica.nume}"


class ABGeneralPlanimetriaBisericii(models.Model):
    imagine = models.ImageField(upload_to="planimetrii", max_length=250)
    spatii_biserica = models.ForeignKey(
        "fragmente.SpatiiBiserica",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Spații Biserică",
    )
    descriere = models.TextField("Descriere", null=True, blank=True)


class ABGeneral(models.Model):
    descriere = models.TextField("Descrierea Construcției", null=True, blank=True)
    etape_constructie = models.TextField("Etape ale construcției / Intervenției", null=True, blank=True)
    stare_conservare = models.TextField("Stare conservare", null=True, blank=True)
    valoare = models.TextField("Valoare", null=True, blank=True)
    model_3d = models.TextField("Model 3D", null=True, blank=True)
    planimetria_bisericii = models.ForeignKey(
        "ABGeneralPlanimetriaBisericii",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Planimetria bisericii",
    )
    releveu = models.FileField(upload_to="relevee", max_length=250)
    foto_generale_exterior = models.ManyToManyField(
        "Fotografie", blank=True, related_name="general_foto_generale_exterior"
    )
    foto_generale_interior = models.ManyToManyField(
        "Fotografie", blank=True, related_name="general_foto_generale_interior"
    )


class ABFundatieSocluFundatieStructura(models.Model):
    tip = models.ManyToManyField(
        "fragmente.TipStructuraFundatie",
        blank=True,
        verbose_name="Materiale Structură",
    )
    observatii = models.TextField("Observații", null=True, blank=True)


class ABFundatieSocluFundatieMateriale(models.Model):
    materiale_structura = models.ManyToManyField(
        "fragmente.MaterialeStructuraFundatieSoclu",
        blank=True,
        verbose_name="Materiale Structură",
    )
    observatii = models.TextField("Observații", null=True, blank=True)


class ABFundatieSocluFundatie(models.Model):
    structura = models.ForeignKey(
        "ABFundatieSocluFundatieStructura",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Structură",
    )
    materiale = models.ForeignKey(
        "ABFundatieSocluFundatieMateriale",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Materiale",
    )


class ABFundatieSocluSocluStructura(models.Model):
    tip = models.ManyToManyField(
        "fragmente.TipStructuraFundatie",
        blank=True,
        verbose_name="Materiale Structură",
    )
    observatii = models.TextField("Observații", null=True, blank=True)


class ABFundatieSocluSocluMateriale(models.Model):
    materiale_structura = models.ManyToManyField(
        "fragmente.MaterialeStructuraFundatieSoclu",
        blank=True,
        verbose_name="Materiale Structură",
    )
    observatii = models.TextField("Observații", null=True, blank=True)


class ABFundatieSocluSocluFinisaje(models.Model):
    tip = models.ManyToManyField("fragmente.FinisajeSoclu", blank=True, verbose_name="Tip")
    observatii = models.TextField("Observații", null=True, blank=True)


class ABFundatieSocluSoclu(models.Model):
    exista = models.BooleanField("Există", default=False)
    structura = models.ForeignKey(
        "ABFundatieSocluSocluStructura",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Structură",
    )
    materiale = models.ForeignKey(
        "ABFundatieSocluSocluMateriale",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Materiale",
    )
    finisaje = models.ForeignKey(
        "ABFundatieSocluSocluFinisaje",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Materiale",
    )


class ABFundatieSoclu(models.Model):
    fundatie = models.ForeignKey(
        "ABFundatieSocluFundatie",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Fundație",
    )
    soclu = models.ForeignKey(
        "ABFundatieSocluSoclu",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Soclu",
    )
    imagini = models.ManyToManyField("Fotografie", blank=True)
    interventii = models.ManyToManyField("Interventie", blank=True, verbose_name="Intervenții")
    stare_conservare = models.ForeignKey(
        "StareConservare",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Stare conservare",
    )


class ABCorpTalpiMaterial(models.Model):
    esenta_lemnoasa = models.ManyToManyField(
        "fragmente.EsentaLemnoasa",
        blank=True,
        verbose_name="Esența Lemnoasă a Structurii",
    )
    tip_prelucrare = models.ManyToManyField(
        "fragmente.TipPrelucrareALemnului",
        blank=True,
        verbose_name="Tip Prelucrare a Lemnului",
    )


class ABCorpTalpi(models.Model):
    tip_asezare = models.ForeignKey(
        "fragmente.TipAsezareTalpi",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Tip așezare",
    )
    observatii_tip_asezare = models.TextField("Observații tip așezare", null=True, blank=True)

    tip_asezare_talpi_transversale = models.ForeignKey(
        "fragmente.TipAsezareTalpiTransversaleFataDeCeleLongitudinale",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Tip așezare tălpi transversale față de cele longitudinale",
    )
    observatii_tip_asezare_talpi_transversale = models.TextField(
        "Observații Tip așezare tălpi transversale față de cele longitudinale",
        null=True,
        blank=True,
    )

    tip_imbinare_colt = models.ForeignKey(
        "fragmente.TipImbinareDeColtTalpi",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Tip îmbinare de colț",
    )
    observatii_imbinare_colt = models.TextField("Observații Tip îmbinare de colț", null=True, blank=True)

    material = models.ForeignKey(
        "ABCorpTalpiMaterial",
        null=True,
        blank=True,
        verbose_name="Material",
        on_delete=models.SET_NULL,
    )
    imagini = models.ManyToManyField("Fotografie", blank=True)

    interventii = models.ManyToManyField("Interventie", blank=True, verbose_name="Intervenții")
    stare_conservare = models.ForeignKey(
        "StareConservare",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Stare conservare",
    )


class ABCorpPardosealaStructuraPardoseala(models.Model):
    tip_structura = models.ForeignKey(
        "fragmente.TipStructuraMaterialePardoseala",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Tip structură",
    )
    descriere_structura = models.TextField("Descriere structură", null=True, blank=True)
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class ABCorpPardosealaFinisaje(models.Model):
    tip_finisaje = models.ManyToManyField("fragmente.FinisajePardoseala", blank=True, verbose_name="Tip structură")
    esenta_lemnoasa = models.ManyToManyField("fragmente.EsentaLemnoasa", blank=True, verbose_name="Esență lemnoasă")
    tip_prelucrare = models.ManyToManyField(
        "fragmente.TipPrelucrareALemnului",
        blank=True,
        verbose_name="Tip prelucrare a lemnului",
    )


class ABCorpPardoseala(models.Model):
    structura_pardosea = models.ForeignKey(
        "ABCorpPardosealaStructuraPardoseala",
        null=True,
        blank=True,
        verbose_name="Structura pardosea",
        on_delete=models.SET_NULL,
    )
    finisaje = models.ForeignKey(
        "ABCorpPardosealaFinisaje",
        null=True,
        blank=True,
        verbose_name="Finisaje",
        on_delete=models.SET_NULL,
    )
    interventii = models.ManyToManyField("Interventie", blank=True, verbose_name="Intervenții")
    stare_conservare = models.ForeignKey(
        "StareConservare",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Stare conservare",
    )


class StructuraPeretiInteriori(models.Model):
    tip_structura = models.ForeignKey(
        "fragmente.TipStructuraPeretiExteriori",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Tip structură",
    )
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class ABCorpPeretiExterioriStructuraChetoare(models.Model):
    tip_structura = models.ForeignKey(
        "fragmente.TipStructuraCheotoare",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Tip structură",
    )
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class ABCorpPeretiExterioriStructuraCatei(models.Model):
    tip_structura = models.ForeignKey(
        "fragmente.TipStructuraCatei",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Tip structură",
    )
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class ABCorpPeretiExterioriStructuraFurci(models.Model):
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class ABCorpPeretiExterioriSistemStructuralMixt(models.Model):
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class ABCorpPeretiExterioriConsole(models.Model):
    tip_structura = models.ForeignKey(
        "fragmente.TipConsole",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Tip console",
    )
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class MaterialStructuraPereti(models.Model):
    tip_material = models.ManyToManyField(
        "fragmente.TipMaterialStructuraPereti",
        blank=True,
        verbose_name="Tip material",
    )
    esenta_lemnoasa = models.ManyToManyField(
        "fragmente.EsentaLemnoasa",
        blank=True,
        verbose_name="Esența Lemnoasă a Structurii",
    )
    tip_prelucrare = models.ManyToManyField(
        "fragmente.TipPrelucrareALemnului",
        blank=True,
        verbose_name="Tip Prelucrare a Lemnului",
    )
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class ABCorpPeretiExterioriFinisajeExterioare(models.Model):
    tip_finisaj = models.ManyToManyField(
        "fragmente.TipFinisajExteriorPereti",
        blank=True,
        verbose_name="Tip finisaj",
    )
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class FinisajInterior(models.Model):
    tip_finisaj = models.ManyToManyField(
        "fragmente.TipFinisajInteriorPereti",
        blank=True,
        verbose_name="Tip finisaj",
    )
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class ABCorpPeretiExteriori(models.Model):
    structura_pereti = models.ForeignKey(
        "StructuraPeretiInteriori",
        null=True,
        blank=True,
        verbose_name="Structură Pereți Exteriori",
        on_delete=models.SET_NULL,
    )
    structura_cheotoare = models.ForeignKey(
        "ABCorpPeretiExterioriStructuraChetoare",
        null=True,
        blank=True,
        verbose_name="Structură Cheotoare",
        on_delete=models.SET_NULL,
    )
    structura_catei = models.ForeignKey(
        "ABCorpPeretiExterioriStructuraCatei",
        null=True,
        blank=True,
        verbose_name="Structură Căței",
        on_delete=models.SET_NULL,
    )
    structura_furci = models.ForeignKey(
        "ABCorpPeretiExterioriStructuraFurci",
        null=True,
        blank=True,
        verbose_name="Structură Furci",
        on_delete=models.SET_NULL,
    )
    sistem_structural_mixt = models.ForeignKey(
        "ABCorpPeretiExterioriSistemStructuralMixt",
        null=True,
        blank=True,
        verbose_name="Sistem Structural mixt",
        on_delete=models.SET_NULL,
    )
    console = models.ForeignKey(
        "ABCorpPeretiExterioriConsole",
        null=True,
        blank=True,
        verbose_name="Console",
        on_delete=models.SET_NULL,
    )
    material_structura_pereti = models.ForeignKey(
        "MaterialStructuraPereti",
        null=True,
        blank=True,
        verbose_name="Material Structură Pereți",
        on_delete=models.SET_NULL,
    )
    finisaje_exterioare = models.ForeignKey(
        "ABCorpPeretiExterioriFinisajeExterioare",
        null=True,
        blank=True,
        verbose_name="Finisaje Exterioare Pereți",
        on_delete=models.SET_NULL,
    )
    finisaje_interioare = models.ForeignKey(
        "FinisajInterior",
        null=True,
        blank=True,
        verbose_name="Finisaje Interioare Pereți",
        on_delete=models.SET_NULL,
    )


class MaterialStructuraPeretiInteriori(models.Model):
    tip_material = models.ManyToManyField(
        "fragmente.TipMaterialPeretiInteriori",
        blank=True,
        verbose_name="Tip material",
    )
    esenta_lemnoasa = models.ManyToManyField(
        "fragmente.EsentaLemnoasa",
        blank=True,
        verbose_name="Esența Lemnoasă a Structurii",
    )
    tip_prelucrare = models.ManyToManyField(
        "fragmente.TipPrelucrareALemnului",
        blank=True,
        verbose_name="Tip Prelucrare a Lemnului",
    )
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class ABCorpPereteNaosAltar(models.Model):
    structura = models.ForeignKey(
        "StructuraPeretiInteriori",
        null=True,
        blank=True,
        verbose_name="Finisaje",
        on_delete=models.SET_NULL,
    )
    material_structura = models.ForeignKey(
        "MaterialStructuraPeretiInteriori",
        null=True,
        blank=True,
        verbose_name="Material Structură",
        on_delete=models.SET_NULL,
    )
    finisaje = models.ForeignKey(
        "FinisajInterior",
        null=True,
        blank=True,
        verbose_name="Finisaje",
        on_delete=models.SET_NULL,
    )
    imagini_dinspre_naos = models.ManyToManyField(
        "Fotografie",
        blank=True,
        related_name="perete_na_imagini_dinspre_naos",
        verbose_name="Imagini Generale dinspre Naos",
    )
    imagini_dinspre_altar = models.ManyToManyField(
        "Fotografie",
        blank=True,
        related_name="perete_na_imagini_dinspre_altar",
        verbose_name="Imagini Generale dinspre Altar",
    )


class ABCorpPeretePronaosNaos(models.Model):
    structura = models.ForeignKey(
        "StructuraPeretiInteriori",
        null=True,
        blank=True,
        verbose_name="Finisaje",
        on_delete=models.SET_NULL,
    )
    material_structura = models.ForeignKey(
        "MaterialStructuraPeretiInteriori",
        null=True,
        blank=True,
        verbose_name="Material Structură",
        on_delete=models.SET_NULL,
    )
    finisaje = models.ForeignKey(
        "FinisajInterior",
        null=True,
        blank=True,
        verbose_name="Finisaje",
        on_delete=models.SET_NULL,
    )
    imagini_dinspre_naos = models.ManyToManyField(
        "Fotografie",
        blank=True,
        related_name="perete_pn_imagini_dinspre_naos",
        verbose_name="Imagini Generale dinspre Naos",
    )
    imagini_dinspre_altar = models.ManyToManyField(
        "Fotografie",
        blank=True,
        related_name="perete_pn_imagini_dinspre_altar",
        verbose_name="Imagini Generale dinspre Altar",
    )


class ABCorpGoluriIntrariDinspreExterior(models.Model):
    total_numar_intrari_dinspre_exterior = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Total Număr Intrări dinspre Exterior",
    )
    descriere_intrari_dinspre_exterior = models.TextField(
        verbose_name="Descriere Intrări dinspre Exterior", null=True, blank=True
    )

    numar_intrari_pridvor = models.IntegerField(null=True, blank=True, verbose_name="Număr Intrări Pridvor")
    tamplarie_istorica_pridvor = models.BooleanField(verbose_name="Tâmplărie Istorică Pridvor", default=False)
    descriere_intrari_pridvor = models.TextField(verbose_name="Descriere Intrări Pridvor", null=True, blank=True)
    imagini_intrari_pridvor = models.ManyToManyField(
        "Fotografie",
        blank=True,
        related_name="exterior_imagini_intrari_pridvor",
        verbose_name="Imagini Intrări Pridvor",
    )

    numar_intrari_pronaos = models.IntegerField(null=True, blank=True, verbose_name="Număr Intrări Pronaos")
    tamplarie_istorica_pronaos = models.BooleanField(verbose_name="Tâmplărie Istorică Pronaos", default=False)
    descriere_intrari_pronaos = models.TextField(verbose_name="Descriere Intrări Pronaos", null=True, blank=True)
    imagini_intrari_pronaos = models.ManyToManyField(
        "Fotografie",
        blank=True,
        related_name="exterior_imagini_intrari_pronaos",
        verbose_name="Imagini Intrări Pronaos",
    )

    numar_intrari_naos = models.IntegerField(null=True, blank=True, verbose_name="Număr Intrări Naos")
    tamplarie_istorica_naos = models.BooleanField(verbose_name="Tâmplărie Istorică Naos", default=False)
    descriere_intrari_naos = models.TextField(verbose_name="Descriere Intrări Naos", null=True, blank=True)
    imagini_intrari_naos = models.ManyToManyField(
        "Fotografie",
        blank=True,
        related_name="exterior_imagini_intrari_naos",
        verbose_name="Imagini Intrări Naos",
    )

    numar_intrari_altar = models.IntegerField(null=True, blank=True, verbose_name="Număr Intrări Altar")
    tamplarie_istorica_altar = models.BooleanField(verbose_name="Tâmplărie Istorică Altar", default=False)
    descriere_intrari_altar = models.TextField(verbose_name="Descriere Intrări Altar", null=True, blank=True)
    imagini_intrari_altar = models.ManyToManyField(
        "Fotografie",
        blank=True,
        related_name="exterior_imagini_intrari_altar",
        verbose_name="Imagini Intrări Altar",
    )


class ABCorpGoluriTreceriIntreSpatii(models.Model):
    numar_intrari_naos_altar = models.IntegerField(null=True, blank=True, verbose_name="Număr Intrări Naos-Altar")
    tamplarie_istorica_naos_altar = models.BooleanField(
        verbose_name="Tâmplărie Istorică la perete Naos-Altar", default=False
    )
    descriere_intrari_naos_altar = models.TextField(verbose_name="Descriere Intrări Naos-Altar", null=True, blank=True)
    imagini_naos_altar = models.ManyToManyField(
        "Fotografie",
        blank=True,
        related_name="spatii_imagini_naos_altar",
        verbose_name="Imagini Naos-Altar",
    )

    numar_intrari_pronaos_naos = models.IntegerField(null=True, blank=True, verbose_name="Număr Intrări Pronaos-Naos")
    tamplarie_istorica_pronaos_naos = models.BooleanField(
        verbose_name="Tâmplărie Istorică la perete Pronaos-Naos", default=False
    )
    descriere_intrari_pronaos_naos = models.TextField(
        verbose_name="Descriere Intrări Pronaos-Naos", null=True, blank=True
    )
    imagini_intrari_pronaos_naos = models.ManyToManyField(
        "Fotografie",
        blank=True,
        related_name="spatii_imagini_intrari_pronaos_naos",
        verbose_name="Imagini Intrări Pronaos-Naos",
    )

    numar_intrari_pridvor_pronaos = models.IntegerField(null=True, blank=True, verbose_name="Număr Pridvor-Pronaos")
    tamplarie_istorica_pridvor_pronaos = models.BooleanField(verbose_name="Tâmplărie Istorică Naos", default=False)
    descriere_intrari_pridvor_pronaos = models.TextField(
        verbose_name="Descriere Pridvor-Pronaos", null=True, blank=True
    )
    imagini_intrari_pridvor_pronaos = models.ManyToManyField(
        "Fotografie",
        blank=True,
        related_name="spatii_imagini_intrari_pridvor_pronaos",
        verbose_name="Imagini Pridvor-Pronaos",
    )

    numar_intrari_pridvor_naos = models.IntegerField(null=True, blank=True, verbose_name="Număr Intrări Pridvor-Naos")
    tamplarie_istorica_pridvor_naos = models.BooleanField(
        verbose_name="Tâmplărie Istorică la perete Pridvor-Naos", default=False
    )
    descriere_intrari_pridvor_naos = models.TextField(
        verbose_name="Descriere Intrări Pridvor-Naos", null=True, blank=True
    )
    imagini_intrari_pridvor_naos = models.ManyToManyField(
        "Fotografie",
        blank=True,
        related_name="spatii_imagini_intrari_pridvor_naos",
        verbose_name="Imagini Intrări Pridvor-Naos",
    )


class ABCorpGoluriFerestre(models.Model):
    total_numar_ferestre = models.IntegerField(null=True, blank=True, verbose_name="Total Număr Ferestre")

    numar_ferestre_pridvor = models.IntegerField(null=True, blank=True, verbose_name="Număr Ferestre Pridvor")
    tamplarie_istorica_pridvor = models.BooleanField(verbose_name="Tâmplărie Istorică Ferestre Pridvor", default=False)
    descriere_ferestre_pridvor = models.TextField(verbose_name="Descriere Ferestre Pridvor", null=True, blank=True)
    imagini_ferestre_pridvor = models.ManyToManyField(
        "Fotografie",
        blank=True,
        related_name="ferestre_imagini_ferestre_pridvor",
        verbose_name="Imagini Ferestre Pridvor",
    )

    numar_ferestre_pronaos = models.IntegerField(null=True, blank=True, verbose_name="Număr Ferestre Pronaos")
    tamplarie_istorica_pronaos = models.BooleanField(verbose_name="Tâmplărie Istorică Ferestre Pronaos", default=False)
    descriere_ferestre_pronaos = models.TextField(verbose_name="Descriere Ferestre Pronaos", null=True, blank=True)
    imagini_ferestre_pronaos = models.ManyToManyField(
        "Fotografie",
        blank=True,
        related_name="ferestre_imagini_ferestre_pronaos",
        verbose_name="Imagini Ferestre Pronaos",
    )

    numar_ferestre_naos = models.IntegerField(null=True, blank=True, verbose_name="Număr Ferestre Naos")
    tamplarie_istorica_naos = models.BooleanField(verbose_name="Tâmplărie Istorică Ferestre Naos", default=False)
    descriere_ferestre_naos = models.TextField(verbose_name="Descriere Ferestre Naos", null=True, blank=True)
    imagini_ferestre_naos = models.ManyToManyField(
        "Fotografie",
        blank=True,
        related_name="ferestre_imagini_ferestre_naos",
        verbose_name="Imagini Ferestre Naos",
    )

    numar_ferestre_altar = models.IntegerField(null=True, blank=True, verbose_name="Număr Ferestre Altar")
    tamplarie_istorica_altar = models.BooleanField(verbose_name="Tâmplărie Istorică Ferestre Altar", default=False)
    descriere_ferestre_altar = models.TextField(verbose_name="Descriere Ferestre Altar", null=True, blank=True)
    imagini_ferestre_altar = models.ManyToManyField(
        "Fotografie",
        blank=True,
        related_name="ferestre_imagini_ferestre_altar",
        verbose_name="Imagini Ferestre Altar",
    )


class ABCorpGoluriOchiesi(models.Model):
    exista = models.BooleanField(verbose_name="Există", default=False)
    total_numar_ochiesi = models.IntegerField(null=True, blank=True, verbose_name="Total Număr ochieși")

    numar_ochiesi_pronaos = models.IntegerField(null=True, blank=True, verbose_name="Număr Ochieși Pronaos")
    numar_ochiesi_naos = models.IntegerField(null=True, blank=True, verbose_name="Număr Ochieși Naos")
    numar_ochiesi_altar = models.IntegerField(null=True, blank=True, verbose_name="Număr Ochieși Altar")
    descriere_ochiesi = models.TextField(verbose_name="Descriere Ochieși ", null=True, blank=True)
    imagini = models.ManyToManyField(
        "Fotografie",
        blank=True,
        verbose_name="Imagini",
    )


class ABCorpGoluri(models.Model):
    intrari_dinspre_exterior = models.ForeignKey(
        "ABCorpGoluriIntrariDinspreExterior",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Intrări dinspre exterior",
    )
    treceri_intre_spatii = models.ForeignKey(
        "ABCorpGoluriTreceriIntreSpatii",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Treceri între spații",
    )
    ferestre = models.ForeignKey(
        "ABCorpGoluriFerestre",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Ferestre",
    )
    ochiesi = models.ForeignKey(
        "ABCorpGoluriOchiesi",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Ochieși",
    )
    interventii = models.ManyToManyField("Interventie", blank=True, verbose_name="Intervenții")
    stare_conservare = models.ForeignKey(
        "StareConservare",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Stare conservare",
    )


class ExistaObservatiiImagini(models.Model):
    exista = models.BooleanField(verbose_name="Există", default=False)
    observatii = models.TextField(verbose_name="Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True, verbose_name="Imagini")


class ABCorpAlteElementeComponenteAleCorpuluiBisericiiTiranti(models.Model):
    exista = models.BooleanField(verbose_name="Există", default=False)
    numar = models.IntegerField(null=True, blank=True, verbose_name="Număr")
    tip = models.ManyToManyField("fragmente.TipTiranti", blank=True, verbose_name="Tip")
    observatii = models.TextField(verbose_name="Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True, verbose_name="Imagini")


class ABCorpAlteElementeComponenteAleCorpuluiBisericii(models.Model):
    pastoforii = models.ForeignKey(
        "ExistaObservatiiImagini",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Pastoforii",
        related_name="elemente_corp_pastoforii",
    )
    tiranti = models.ForeignKey(
        "ABCorpAlteElementeComponenteAleCorpuluiBisericiiTiranti",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Tiranți",
    )
    solee = models.ForeignKey(
        "ExistaObservatiiImagini",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Solee",
        related_name="elemente_corp_solee",
    )
    console_intermediare = models.ForeignKey(
        "ExistaObservatiiImagini",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Console Intermediare",
        related_name="elemente_corp_console_intermediare",
    )
    cosoroabe = models.ForeignKey(
        "ExistaObservatiiImagini",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Cosoroabe",
        related_name="elemente_corp_cosoroabe",
    )


class ABCorp(models.Model):
    talpi = models.ForeignKey(
        "ABCorpTalpi",
        null=True,
        blank=True,
        verbose_name="Tălpi",
        on_delete=models.SET_NULL,
    )
    pardoseala = models.ForeignKey(
        "ABCorpPardoseala",
        null=True,
        blank=True,
        verbose_name="Pardoseală",
        on_delete=models.SET_NULL,
    )
    pereti_exteriori = models.ForeignKey(
        "ABCorpPeretiExteriori",
        null=True,
        blank=True,
        verbose_name="Pereți Exteriori",
        on_delete=models.SET_NULL,
    )
    perete_naos_altar = models.ForeignKey(
        "ABCorpPereteNaosAltar",
        null=True,
        blank=True,
        verbose_name="Perete Naos-Altar",
        on_delete=models.SET_NULL,
    )
    perete_pronaos_naos = models.ForeignKey(
        "ABCorpPeretePronaosNaos",
        null=True,
        blank=True,
        verbose_name="Perete Pronaos-Naos",
        on_delete=models.SET_NULL,
    )
    goluri = models.ForeignKey(
        "ABCorpGoluri",
        null=True,
        blank=True,
        verbose_name="Goluri",
        on_delete=models.SET_NULL,
    )
    alte_elemente_componente_ale_corpului_bisericii = models.ForeignKey(
        "ABCorpAlteElementeComponenteAleCorpuluiBisericii",
        null=True,
        blank=True,
        verbose_name="Alte elemente componente ale corpului bisericii",
        on_delete=models.SET_NULL,
    )

    interventii_ansamblu_pereti_biserica = models.ManyToManyField(
        "Interventie",
        blank=True,
        verbose_name="Intervenții Ansamblu Pereți Biserică",
    )

    stare_conservare_structura_ansamblu_pereti_biserica = models.ForeignKey(
        "StareConservare",
        related_name="stare_conservare_structura_ansamblu_pereti_biserica",
        null=True,
        blank=True,
        verbose_name="Stare conservare Structură Ansamblu Pereți Biserică",
        on_delete=models.SET_NULL,
    )
    stare_conservare_finisaje_exterioare = models.ForeignKey(
        "StareConservare",
        related_name="stare_conservare_finisaje_exterioare",
        null=True,
        blank=True,
        verbose_name="Stare conservare Finisaje Exterioare Ansamblu Pereți Biserică",
        on_delete=models.SET_NULL,
    )
    stare_conservare_finisaje_interioare = models.ForeignKey(
        "StareConservare",
        related_name="stare_conservare_finisaje_interioare",
        null=True,
        blank=True,
        verbose_name="Stare conservare Finisaje Interioare Ansamblu Pereți Biserică",
        on_delete=models.SET_NULL,
    )


class StructuraBoltaTavan(models.Model):
    tip = models.ForeignKey(
        "fragmente.TipBoltaTavanCupola",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Tip",
    )
    structura_bolta = models.ForeignKey(
        "fragmente.StructuraBolta",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Structură boltă",
    )
    structura_tavan = models.ForeignKey(
        "fragmente.StructuraTavan",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Structură tavan",
    )


class MaterialStructuraBoltaTavan(models.Model):
    tip_material_structura = models.ForeignKey(
        "fragmente.MaterialStructuraBoltaTavanCupola",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Tip material Structură",
    )
    esenta_lemnoasa = models.ManyToManyField("fragmente.EsentaLemnoasa", blank=True, verbose_name="Esența Lemnoasă")
    tip_prelucrare = models.ManyToManyField(
        "fragmente.TipPrelucrareALemnului",
        blank=True,
        verbose_name="Tip Prelucrare a Lemnului",
    )


class RubricaBoltaTavan(models.Model):
    structura_bolta_tavan_peste_pridvor = models.ForeignKey(
        "StructuraBoltaTavan",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Structură Boltă / Tavan peste Pridvor",
    )
    material_structura = models.ForeignKey(
        "MaterialStructuraBoltaTavan",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Material  Structură",
    )

    finisaj = models.ManyToManyField(
        "fragmente.FinisajBoltaTavanCupola",
        blank=True,
        verbose_name="Tip finisaj",
    )
    observatii = models.TextField(verbose_name="Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True, verbose_name="Imagini")


class ABBoltiTavane(models.Model):
    bolta_tavan_peste_pridvor = models.ForeignKey(
        "RubricaBoltaTavan",
        related_name="bolta_tavan_peste_pridvor",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Boltă / Tavan peste Pridvor",
    )
    bolta_tavan_peste_pronaos = models.ForeignKey(
        "RubricaBoltaTavan",
        related_name="bolta_tavan_peste_pronaos",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Boltă / Tavan Peste Pronaos",
    )
    bolta_tavan_peste_naos = models.ForeignKey(
        "RubricaBoltaTavan",
        related_name="bolta_tavan_peste_naos",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Boltă / Tavan peste Naos",
    )

    relatie_bolta_altar_naos = models.ForeignKey(
        "fragmente.RelatieBoltaAltarNaos",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Relație Boltă Altar-Naos",
    )

    bolta_tavan_cupola_altar = models.ForeignKey(
        "RubricaBoltaTavan",
        related_name="bolta_tavan_cupola_altar",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Boltă / Tavan / Cupolă Altar",
    )

    foto_generale_extrados = models.ManyToManyField(
        "Fotografie",
        blank=True,
        related_name="foto_generale_extrados",
        verbose_name="Foto Generale Extrados",
    )
    foto_generale_intrados = models.ManyToManyField(
        "Fotografie",
        blank=True,
        related_name="foto_generale_intrados",
        verbose_name="Foto Generale Intrados",
    )
    interventii_bolti_tavane_cupole = models.ManyToManyField(
        "Interventie",
        blank=True,
        verbose_name="Intervenții Bolți / Tavane / Cupole",
    )
    stare_conservare_structura_bolti_tavane_cupole = models.ForeignKey(
        "StareConservare",
        related_name="stare_conservare_structura_bolti_tavane_cupole",
        null=True,
        blank=True,
        verbose_name="Stare conservare Structură Bolți /Tavane / Cupole",
        on_delete=models.SET_NULL,
    )
    stare_conservare_finisaje_bolti_tavane_cupole = models.ForeignKey(
        "StareConservare",
        related_name="stare_conservare_finisaje_bolti_tavane_cupole",
        null=True,
        blank=True,
        verbose_name="Stare conservare Finisaje Bolți / Tavane / Cupole",
        on_delete=models.SET_NULL,
    )


class ABCorStructura(models.Model):
    tip = models.ManyToManyField("fragmente.TipStructuraCor", blank=True, verbose_name="Tip")
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class ABCorMaterialStructura(models.Model):
    tip = models.ManyToManyField("fragmente.MaterialCor", blank=True)
    esenta_lemnoasa = models.ManyToManyField(
        "fragmente.EsentaLemnoasa",
        blank=True,
        verbose_name="Esența Lemnoasă a Structurii",
    )
    tip_prelucrare = models.ManyToManyField(
        "fragmente.TipPrelucrareALemnului",
        blank=True,
        verbose_name="Tip Prelucrare a Lemnului",
    )
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class ABCor(models.Model):
    exista = models.BooleanField("Există", default=False)
    interventie_ulterioara = models.BooleanField("Intervenție Ulterioară", default=False)

    structura = models.ForeignKey(
        "ABCorStructura",
        related_name="cor",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Structură",
    )
    material_structura = models.ForeignKey(
        "ABCorMaterialStructura",
        related_name="cor_material",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Material Structură",
    )
    finisaj = models.ForeignKey("fragmente.FinisajCor", null=True, blank=True, on_delete=models.SET_NULL)

    observatii = models.TextField(verbose_name="Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)
    interventii = models.ManyToManyField("Interventie", blank=True, verbose_name="Intervenții")
    stare_conservare = models.ForeignKey(
        "StareConservare", on_delete=models.SET_NULL, verbose_name="Stare Conservare", null=True, blank=True
    )


class ABSarpantaCorpBisericaCaracteristici(models.Model):
    tip = models.ManyToManyField("fragmente.TipSarpanta", blank=True, verbose_name="Tip")
    sarpanta_veche = models.BooleanField("Există Șarpantă veche, nefolosită, sub șarpanta actuală", default=False)
    sarpanta_istorica = models.BooleanField("Există Șarpantă istorică", default=False)


class ABSarpantaCorpBisericaStructura(models.Model):
    descriere = models.TextField("Descriere Structură Șarpantă", null=True, blank=True)
    tehnica = models.ManyToManyField(
        "fragmente.TehnicaDeConstructie",
        blank=True,
        verbose_name="Tehnica de construcție a Șarpantei",
    )
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class ABSarpantaCorpBisericaMaterialStructura(models.Model):
    esenta_lemnoasa = models.ManyToManyField(
        "fragmente.EsentaLemnoasa",
        blank=True,
        verbose_name="Esența Lemnoasă a Structurii",
    )
    tip_prelucrare = models.ManyToManyField(
        "fragmente.TipPrelucrareALemnului",
        blank=True,
        verbose_name="Tip Prelucrare a Lemnului",
    )
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class FinisajInvelitoare(models.Model):
    an_montaj = models.IntegerField(null=True, blank=True)
    sursa_an_montaj = models.TextField(null=True, blank=True)
    material = models.ForeignKey(
        "fragmente.MaterialInvelitoare",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    sindrila_lungime = models.IntegerField(null=True, blank=True)
    sindrila_latime_medie = models.IntegerField(null=True, blank=True)
    sindrila_grosime_medie = models.IntegerField(null=True, blank=True)
    sindrila_pasul_latuirii = models.IntegerField(null=True, blank=True)
    sindrila_pasul_baterii = models.IntegerField(null=True, blank=True)
    sindrila_numar_straturi = models.IntegerField(null=True, blank=True)
    sindrila_cu_horj = models.BooleanField(default=False)
    sindrlia_tipul_de_batere = models.ForeignKey(
        "fragmente.TipulDeBatere",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    sindrlia_tipul_prindere = models.ForeignKey(
        "fragmente.TipulDePrindere",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    sindrlia_forma_botului = models.ForeignKey(
        "fragmente.FormaBotului",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    sindrila_cu_tesitura = models.BooleanField(default=False)
    sindrlia_prelucrare = models.ForeignKey(
        "fragmente.TipPrelucrareSindrila",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    sindrlia_esenta_lemnoasa = models.ForeignKey(
        "fragmente.EsentaLemnoasaSindrila",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    observatii = models.TextField(verbose_name="Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class EtapaAnterioareInvelitoareSindrila(models.Model):
    denumire_etapa = models.CharField("Denumire etapă", max_length=100, null=True, blank=True)
    sindrila_pasul_latuirii = models.IntegerField(null=True, blank=True)
    sindrila_numar_straturi = models.IntegerField(null=True, blank=True)
    sindrila_cu_horj = models.BooleanField(default=False)
    sindrlia_tipul_de_batere = models.ForeignKey(
        "fragmente.TipulDeBatere",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    sindrlia_forma_botului = models.ForeignKey(
        "fragmente.FormaBotului",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    sindrila_cu_tesitura = models.BooleanField(default=False)
    sindrlia_esenta_lemnoasa = models.ForeignKey(
        "fragmente.EsentaLemnoasaSindrila",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    observatii = models.TextField(verbose_name="Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class ABSarpantaCorpBiserica(models.Model):
    caracteristici = models.ForeignKey(
        "ABSarpantaCorpBisericaCaracteristici",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Caracteristici",
    )
    structura = models.ForeignKey(
        "ABSarpantaCorpBisericaStructura",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Structură",
    )
    material_structura = models.ForeignKey(
        "ABSarpantaCorpBisericaMaterialStructura",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Material Structură",
    )
    finisaj_invelitoare_corp_biserica = models.ForeignKey(
        "FinisajInvelitoare",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Finisaj - Învelitoare Corp Biserică",
    )

    observatii = models.TextField(verbose_name="Observații", null=True, blank=True)

    imagini_generale_exterior = models.ManyToManyField(
        "Fotografie",
        blank=True,
        verbose_name="Imagini Generale Exterior",
        related_name="corp_biserica_imagini_generale_exterior",
    )
    imagini_generale_interior_pod = models.ManyToManyField(
        "Fotografie",
        blank=True,
        verbose_name="Imagini Generale Interior (Pod)",
        related_name="corp_biserica_imagini_generale_interior_pod",
    )

    interventii_sarpanta_corp_biserica = models.ManyToManyField(
        "Interventie",
        blank=True,
        verbose_name="Intervenții Șarpantă Corp Biserică",
    )

    etape_anterioare_vizibile_ale_invelitorii_de_sindrila = models.ManyToManyField(
        "EtapaAnterioareInvelitoareSindrila",
        blank=True,
        verbose_name="Etape Anterioare Vizibile ale Învelitorii de Șindrilă",
    )

    stare_conservare_invelitoare_sarpanta_corp_biserica = models.ForeignKey(
        "StareConservare",
        related_name="stare_conservare_invelitoare_sarpanta_corp_biserica",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Stare conservare Învelitoare Șarpantă Corp Biserică",
    )
    stare_conservare_structura_sarpanta_corp_biserica = models.ForeignKey(
        "StareConservare",
        related_name="stare_conservare_structura_sarpanta_corp_biserica",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Stare conservare Structură Șarpantă Corp Biserică",
    )


class ABTurnCaracteristiciGalerie(models.Model):
    exista = models.BooleanField("Există", default=False)
    tip = models.ManyToManyField("fragmente.TipGalerieTurn", blank=True)
    numar_arcade_turn_deschis = models.IntegerField("Număr arcade turn deschis", null=True, blank=True)
    descriere = models.TextField(null=True, blank=True)


class ABTurnCaracteristiciClopot(models.Model):
    an = models.IntegerField(null=True, blank=True)
    inscriptie = models.TextField("Inscripție", null=True, blank=True)
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class ABTurnCaracteristici(models.Model):
    numar_turnuri = models.IntegerField("Număr turnuri", null=True, blank=True)
    amplasare = models.ManyToManyField("fragmente.AmplasareTurn", blank=True)
    dimensiune = models.ForeignKey(
        "fragmente.DimensiuneTurn",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    morfologie_coif = models.ForeignKey(
        "fragmente.MorfologieCoif",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    plan = models.ForeignKey("fragmente.PlanTurn", null=True, blank=True, on_delete=models.SET_NULL)
    galerie = models.ForeignKey(
        "ABTurnCaracteristiciGalerie",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    clopote = models.ManyToManyField("ABTurnCaracteristiciClopot", blank=True)


class ABTurnStructura(models.Model):
    descriere = models.TextField("Descriere", null=True, blank=True)
    numar_talpi = models.IntegerField("Număr tălpi", null=True, blank=True)
    asezare = models.ManyToManyField("fragmente.AsezareTalpiTurn", blank=True)
    relatie_talpi = models.ManyToManyField("fragmente.RelatieTalpiTurn", blank=True)
    numar_stalpi = models.IntegerField("Număr stâlpi", null=True, blank=True)
    descriere_coif = models.TextField("Descriere structura coif", null=True, blank=True)
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class ABTurn(models.Model):
    exista = models.BooleanField("Există", default=False)
    caracteristici = models.ForeignKey(
        "ABTurnCaracteristici",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Caracteristici",
    )
    structura = models.ForeignKey(
        "ABTurnStructura",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Structură",
    )
    material_structura = models.ForeignKey(
        "ABSarpantaCorpBisericaMaterialStructura",
        related_name="turn_material_structura",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Material Structură",
    )
    finisaj_inchidere_tambur = models.ForeignKey(
        "FinisajInvelitoare",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Finisaj - Închidere Tambur Turn",
        related_name="turn_finisaj_inchidere_tambur",
    )
    finisaj_inchidere_coif = models.ForeignKey(
        "FinisajInvelitoare",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Finisaj - Închidere Coif Turn",
        related_name="turn_finisaj_inchidere_coif",
    )

    observatii = models.TextField(verbose_name="Observații", null=True, blank=True)

    imagini_generale_exterior = models.ManyToManyField(
        "Fotografie",
        blank=True,
        verbose_name="Imagini Generale Exterior",
        related_name="turn_imagini_generale_exterior",
    )
    imagini_generale_interior_pod = models.ManyToManyField(
        "Fotografie",
        blank=True,
        verbose_name="Imagini Generale Interior (Pod)",
        related_name="turn_imagini_generale_interior_pod",
    )

    interventii_turn = models.ManyToManyField("Interventie", blank=True, verbose_name="Intervenții Turn")

    stare_conservare_structura_turn = models.ForeignKey(
        "StareConservare",
        related_name="turn_stare_conservare_structura_turn",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Stare conservare Structură Turn",
    )
    stare_conservare_finisaje_turn = models.ForeignKey(
        "StareConservare",
        related_name="turn_stare_conservare_finisaje_turn",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Stare conservare Finisaje Turn",
    )


class ABTurleCaracteristici(models.Model):
    numar_turle = models.IntegerField("Număr Turle", null=True, blank=True)
    amplasare = models.ManyToManyField("fragmente.AmplasareTurle", blank=True)
    numar_goluri = models.IntegerField("Număr goluri", null=True, blank=True)
    morfologie_acoperis = models.ForeignKey(
        "fragmente.MorfologieTurle",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Morfologie Acoperiș Turle",
    )


class ABTurleStructura(models.Model):
    descriere = models.TextField("Descriere", null=True, blank=True)
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class ABTurle(models.Model):
    exista = models.BooleanField("Există", default=False)
    caracteristici = models.ForeignKey(
        "ABTurleCaracteristici",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Caracteristici",
    )
    structura = models.ForeignKey(
        "ABTurleStructura",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Structură",
    )
    material_structura = models.ForeignKey(
        "ABSarpantaCorpBisericaMaterialStructura",
        related_name="turle_material_structura",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Material Structură",
    )

    finisaj_inchidere_tambur = models.ForeignKey(
        "FinisajInvelitoare",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Finisaj - Închidere Tambur Turle",
        related_name="turle_finisaj_inchidere_tambur",
    )
    finisaj_inchidere_coif = models.ForeignKey(
        "FinisajInvelitoare",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Finisaj - Închidere Coif Turle",
        related_name="turle_finisaj_inchidere_coif",
    )

    observatii = models.TextField(verbose_name="Observații", null=True, blank=True)

    imagini_generale_exterior = models.ManyToManyField(
        "Fotografie",
        blank=True,
        verbose_name="Imagini Generale Exterior",
        related_name="turle_imagini_generale_exterior",
    )
    imagini_generale_interior = models.ManyToManyField(
        "Fotografie",
        blank=True,
        verbose_name="Imagini Generale Interior",
        related_name="turle_imagini_generale_interior",
    )

    interventii_turle = models.ManyToManyField("Interventie", blank=True, verbose_name="Intervenții Turle")

    stare_conservare_structura_turle = models.ForeignKey(
        "StareConservare",
        related_name="turle_stare_conservare_structura_turle",
        on_delete=models.SET_NULL,
        verbose_name="Stare conservare Structură Turle",
        null=True,
        blank=True,
    )
    stare_conservare_finisaje_turle = models.ForeignKey(
        "StareConservare",
        related_name="turle_stare_conservare_finisaje_turle",
        on_delete=models.SET_NULL,
        verbose_name="Stare conservare Finisaje Turn",
        null=True,
        blank=True,
    )


class ArhitecturaBisericii(models.Model):
    """
    Capitol: Peisaj Biserica
    """

    biserica = models.OneToOneField("Biserica", on_delete=models.CASCADE, related_name="arhitectura_bisericii")

    general = models.ForeignKey(
        "ABGeneral",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="General",
    )
    fundatie_soclu = models.ForeignKey(
        "ABFundatieSoclu",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Fundație / Soclu",
    )
    corp_biserica = models.ForeignKey(
        "ABCorp",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Corp Biserică",
    )
    bolti_tavane = models.ForeignKey(
        "ABBoltiTavane",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Bolți / Tavane",
    )
    cor = models.ForeignKey(
        "ABCor",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Cor",
    )
    sarpanta_corp_biserica = models.ForeignKey(
        "ABSarpantaCorpBiserica",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Șarpantă Corp Biserică",
    )
    turn = models.ForeignKey(
        "ABTurn",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Turn",
    )
    turle = models.ForeignKey(
        "ABTurle",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Turle",
    )

    history = HistoricalRecords()

    class Meta:
        ordering = ["biserica__the_order"]
        verbose_name = "Arhitectura Bisericii"
        verbose_name_plural = "Arhitectura Bisericii"

    def __str__(self):
        return f"Arhitectura Bisericii {self.biserica.nume}"


class CAGeneral(models.Model):
    sinteza = models.TextField("Sinteză descriere", null=True, blank=True)
    sinteza_conservare = models.TextField("Sinteză stare de conservare", null=True, blank=True)
    sinteza_interventii = models.TextField("Sinteză intervenții în timp", null=True, blank=True)

    foto_generale_exterior = models.ManyToManyField("Fotografie", blank=True, related_name="ca_foto_generale_exterior")
    foto_generale_interior = models.ManyToManyField("Fotografie", blank=True, related_name="ca_foto_generale_interior")


class CAIconostasTipologie(models.Model):
    tip = models.ForeignKey(
        "fragmente.TipIconostas",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class CAIconostasMateriale(models.Model):
    materiale = models.ManyToManyField(
        "fragmente.MaterialeIconostas",
        blank=True,
    )
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class CAIconostasPictura(models.Model):
    tehnica = models.ManyToManyField(
        "fragmente.TehnicaPicturiiIconostasului", blank=True, verbose_name="Tehnica Picturii"
    )
    proportie_suprafata = models.ForeignKey(
        "fragmente.ProportiePicturaIconostas",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Proporția de suprafață acoperită",
    )
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class CAIconostasScultptura(models.Model):
    descriere = models.TextField("Descriere", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class CAIconostasComponente(models.Model):
    componente = models.ManyToManyField(
        "fragmente.ComponenteIconostas",
        blank=True,
    )
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class CAIconostas(models.Model):
    tipologie = models.ForeignKey(
        "CAIconostasTipologie",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    materiale = models.ForeignKey(
        "CAIconostasMateriale",
        null=True,
        blank=True,
        verbose_name="Materiale componente",
        on_delete=models.SET_NULL,
    )
    pictura = models.ForeignKey(
        "CAIconostasPictura",
        null=True,
        blank=True,
        verbose_name="Pictură",
        on_delete=models.SET_NULL,
    )
    sculptura = models.ForeignKey(
        "CAIconostasScultptura",
        null=True,
        blank=True,
        verbose_name="Sculptură/alte decorații",
        on_delete=models.SET_NULL,
    )
    componente = models.ForeignKey(
        "CAIconostasComponente",
        null=True,
        blank=True,
        verbose_name="Componente",
        on_delete=models.SET_NULL,
    )
    datare = models.ForeignKey(
        "Datare",
        null=True,
        blank=True,
        verbose_name="Datare",
        on_delete=models.SET_NULL,
    )
    justificare_datare = models.ForeignKey(
        "JustificareDatare",
        null=True,
        blank=True,
        verbose_name="Justificare Datare",
        on_delete=models.SET_NULL,
    )
    interventii = models.ManyToManyField("Interventie", blank=True, verbose_name="Intervenții")
    stare_conservare = models.ForeignKey(
        "StareConservare", on_delete=models.SET_NULL, verbose_name="Stare Conservare", null=True, blank=True
    )


class CAProportieSuprafata(models.Model):
    proportie_suprafata = models.ForeignKey(
        "fragmente.ProportiePicturaMurala",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Proporția de suprafață acoperită/vizibilă",
    )
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class CAMurala(models.Model):
    tehnica = models.ManyToManyField(
        "fragmente.TehnicaPicturiiDecoratiei", blank=True, verbose_name="Tehnica picturii/decorației"
    )
    proportie = models.ForeignKey(
        "fragmente.ProportiePicturaMurala",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Proporția de suprafață acoperită/vizibilă",
    )
    datare = models.ForeignKey(
        "Datare",
        null=True,
        blank=True,
        verbose_name="Datare",
        on_delete=models.SET_NULL,
    )
    justificare_datare = models.ForeignKey(
        "JustificareDatare",
        null=True,
        blank=True,
        verbose_name="Justificare Datare",
        on_delete=models.SET_NULL,
    )
    interventii = models.ManyToManyField("Interventie", blank=True, verbose_name="Intervenții")
    stare_conservare = models.ForeignKey(
        "StareConservare", on_delete=models.SET_NULL, verbose_name="Stare Conservare", null=True, blank=True
    )


class CAElementeSculptateAlteDecoratii(models.Model):
    exista = models.BooleanField("Există", default=False)
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)

    stare_conservare = models.ForeignKey(
        "StareConservare", on_delete=models.SET_NULL, verbose_name="Stare Conservare", null=True, blank=True
    )


class CAObiecteDeCultIstorice(models.Model):
    exista = models.BooleanField("Există", default=False)
    denumire = models.ManyToManyField("fragmente.ObiecteDeCultIstorice", blank=True, verbose_name="Denumire")

    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class CAMobilierIstoric(models.Model):
    exista = models.BooleanField("Există", default=False)
    denumire = models.ManyToManyField("fragmente.MobilierIstoric", blank=True, verbose_name="Denumire")

    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)
    stare_conservare = models.ForeignKey(
        "StareConservare", on_delete=models.SET_NULL, verbose_name="Stare Conservare", null=True, blank=True
    )


class CAPereteNaosPronaos(models.Model):
    exista = models.BooleanField("Există", default=False)
    tehnica = models.ManyToManyField(
        "fragmente.TehnicaPicturiiDecoratiei", blank=True, verbose_name="Tehnica picturii/decorației"
    )
    proportie = models.ForeignKey(
        "CAProportieSuprafata",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Proporția de suprafață acoperită/vizibilă",
    )
    sculptura_alte_decoratii = models.ForeignKey(
        "ExistaObservatiiImagini",
        verbose_name="Sculptură/alte decorații",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    datare = models.ForeignKey(
        "Datare",
        null=True,
        blank=True,
        verbose_name="Datare",
        on_delete=models.SET_NULL,
    )
    justificare_datare = models.ForeignKey(
        "JustificareDatare",
        null=True,
        blank=True,
        verbose_name="Justificare Datare",
        on_delete=models.SET_NULL,
    )
    interventii = models.ManyToManyField("Interventie", blank=True, verbose_name="Intervenții")
    stare_conservare = models.ForeignKey(
        "StareConservare", on_delete=models.SET_NULL, verbose_name="Stare Conservare", null=True, blank=True
    )


class ComponenteArtistice(models.Model):
    """
    Capitol: Componente Artistice Biserica
    """

    biserica = models.OneToOneField("Biserica", on_delete=models.CASCADE, related_name="componente_artistice")
    general = models.ForeignKey("CAGeneral", verbose_name="General", null=True, blank=True, on_delete=models.SET_NULL)
    iconostas = models.ForeignKey(
        "CAIconostas", verbose_name="Iconostas", null=True, blank=True, on_delete=models.SET_NULL
    )
    murala_interioara = models.ForeignKey(
        "CAMurala",
        verbose_name="Pictura/decorația murală interioară",
        null=True,
        blank=True,
        related_name="artistic_murala_interioara",
        on_delete=models.SET_NULL,
    )
    murala_exteroara = models.ForeignKey(
        "CAMurala",
        verbose_name="Pictura/decorația murală exteroară",
        null=True,
        blank=True,
        related_name="artistic_murala_exterioara",
        on_delete=models.SET_NULL,
    )
    elemente_sculptate_alte_decoratii = models.ForeignKey(
        "CAElementeSculptateAlteDecoratii",
        verbose_name="Elemente sculptate / alte decorații",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    icoane_istorice = models.ForeignKey(
        "ExistaObservatiiImagini",
        verbose_name="Icoane Istorice",
        null=True,
        blank=True,
        related_name="artistic_icoane_istorice",
        on_delete=models.SET_NULL,
    )
    obiecte_de_cult_istorice = models.ForeignKey(
        "CAObiecteDeCultIstorice",
        verbose_name="Obiecte de Cult Istorice",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    mobilier_istoric = models.ForeignKey(
        "CAMobilierIstoric", verbose_name="Mobilier Istoric", null=True, blank=True, on_delete=models.SET_NULL
    )
    obiecte_de_cult_instrainate = models.ForeignKey(
        "ExistaObservatiiImagini",
        verbose_name="Obiecte de cult înstrăinate",
        null=True,
        blank=True,
        related_name="artistic_obiecte_instrainate",
        on_delete=models.SET_NULL,
    )
    perete_naos_pronaos = models.ForeignKey(
        "CAPereteNaosPronaos",
        verbose_name="Componente artistice la peretele despărțitor naos-pronaos",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    history = HistoricalRecords()

    class Meta:
        ordering = ["biserica__the_order"]
        verbose_name = "Decriere Componente Artistice"
        verbose_name_plural = "Decriere Componente Artistice"

    def __str__(self):
        return f"Decriere Componente Artistice {self.biserica.nume}"


class RiscuriInstalatii(models.Model):
    exista = models.BooleanField("Există", default=False)
    descriere = models.TextField("Descriere", null=True, blank=True)
    ultima_interventie = models.DateField(null=True, blank=True, verbose_name="Ultima Intervenție / Verificare")
    risc = models.BooleanField("Risc", default=False)
    observatii = models.TextField("Observații", null=True, blank=True)
    imagini = models.ManyToManyField("Fotografie", blank=True)


class InstalatiiEchipamente(models.Model):
    """
    Capitol: Componente Artistice Biserica
    """

    biserica = models.OneToOneField("Biserica", on_delete=models.CASCADE, related_name="instalatii_echipamente")

    instalatii_electrice = models.ForeignKey(
        "RiscuriInstalatii",
        related_name="instalatii_electrice",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Instalații electrice",
    )
    paratraznet = models.ForeignKey(
        "RiscuriInstalatii",
        related_name="paratraznet",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Paratrăznet",
    )
    instalatii_termice = models.ForeignKey(
        "RiscuriInstalatii",
        related_name="instalatii_termice",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Instalații Termice",
    )
    pichet_psi = models.ForeignKey(
        "RiscuriInstalatii",
        related_name="pichet_psi",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Pichet PSI",
    )
    monitorizare_antiefractie_si_vandalism = models.ForeignKey(
        "RiscuriInstalatii",
        related_name="monitorizare_antiefractie_si_vandalism",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Monitorizare Antiefracție și Vandalism",
    )

    history = HistoricalRecords()

    class Meta:
        ordering = ["biserica__the_order"]
        verbose_name = "Instalații și Echipamente"
        verbose_name_plural = "Instalații și Echipamente"

    def __str__(self):
        return f"Instalații și Echipamente {self.biserica.nume}"


class CalificativValoare(models.Model):
    calificativ = models.IntegerField(choices=CLASE_EVALUARE, null=True, blank=True, help_text="Calificativ")
    observatii = models.TextField("Observații", null=True, blank=True)


class Valoare(models.Model):
    """
    Capitol: Valoare Patrimoniu Cultural Biserica
    """

    biserica = models.OneToOneField("Biserica", on_delete=models.CASCADE, related_name="valoare")

    vechime = models.ForeignKey(
        "CalificativValoare",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="vechime",
        verbose_name="Vechime",
    )
    integritate = models.ForeignKey(
        "CalificativValoare",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="integritate",
        verbose_name="Integritate / Autenticitate",
    )
    unicitate = models.ForeignKey(
        "CalificativValoare",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="unicitate",
        verbose_name="Unicitate",
    )
    valoare_memoriala = models.ForeignKey(
        "CalificativValoare",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="valoare_memoriala",
        verbose_name="Valoare Memorial-Simbolică",
    )
    peisaj_cultural = models.ForeignKey(
        "CalificativValoare",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="peisaj_cultural",
        verbose_name="Valoarea Peisajului Cultural",
    )
    sit = models.ForeignKey(
        "CalificativValoare",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="sit",
        verbose_name="Valoarea Sitului",
    )
    arhitecturala = models.ForeignKey(
        "CalificativValoare",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="arhitecturala",
        verbose_name="Valoarea Arhitecturală ",
    )
    mestesug = models.ForeignKey(
        "CalificativValoare",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="mestesug",
        verbose_name="Valoarea Meșteșugului",
    )
    componente_artistice = models.ForeignKey(
        "CalificativValoare",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="componente_artistice",
        verbose_name="Valoarea Componentelor artistice",
    )
    folosinta_actuala = models.ForeignKey(
        "CalificativValoare",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="folosinta_actuala",
        verbose_name="Folosința Actuală",
    )
    relevanta_actuala = models.ForeignKey(
        "CalificativValoare",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="relevanta_actuala",
        verbose_name="Relevanța Actuală pentru Comunitate",
    )
    potential = models.ForeignKey(
        "CalificativValoare",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="potential",
        verbose_name="Potențial",
    )
    bioculturala = models.ForeignKey(
        "CalificativValoare",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bioculturala",
        verbose_name="Valoarea Bioculturală",
    )
    imateriala = models.ForeignKey(
        "CalificativValoare",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="imateriala",
        verbose_name="Valoarea Imaterială",
    )

    history = HistoricalRecords()

    class Meta:
        ordering = ["biserica__the_order"]
        verbose_name_plural = "Valoare Patrimoniu Cultural"

    def __str__(self):
        return f"Valoare patrimoniu cultural {self.biserica.nume}"
