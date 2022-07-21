from django.db import models
from django.contrib import admin
from simple_history.models import HistoricalRecords


class GenericAdmin(admin.ModelAdmin):
    pass


class Judet(models.Model):
    nume = models.CharField(max_length=50)
    cod = models.CharField(max_length=2)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Județe"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class Comuna(models.Model):
    nume = models.CharField(max_length=50)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Comune"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class Localitate(models.Model):
    nume = models.CharField(max_length=50)
    judet = models.ForeignKey("Judet", on_delete=models.CASCADE)
    comuna = models.ForeignKey("Comuna", on_delete=models.CASCADE, null=True, blank=True)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Localități"
        ordering = ["nume"]

    def __str__(self):
        if self.comuna:
            return f"{self.nume}, com. {self.comuna.nume}"
        return self.nume


class CategorieObiectiv(models.Model):
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Categorie Obiectiv"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class Statut(models.Model):
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Statut"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class Hram(models.Model):
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Hram"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class Cult(models.Model):
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Cult"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class FrecventaUtilizarii(models.Model):
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Frecvența Utilizării"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class Singularitate(models.Model):
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Singularitate"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipArtera(models.Model):
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip arteră"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipRegimProprietate(models.Model):
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipul Regimului de Proprietate"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipFormaRelief(models.Model):
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipul Formei de Relief"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipReperHidrografic(models.Model):
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipul Reperului Hidrografic"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipZoneNaturale(models.Model):
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Zone Naturale (Arii Protejate)"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class Bibliografie(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Bibliografie"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class JustificareDatare(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Justificare Datare"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipPisanie(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip pisanie"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class Secol(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Secole"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipCadruPeisaj(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Cadru Peisaj"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipLoc(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Loc"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipRelatieCuCimitirul(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Relatie Cu Cimitirul"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class NotaStareConservare(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Nota Stare Conservare"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipDegradare(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Degradare"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipRisc(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Risc"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class InterventiiNecesare(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Interventii Necesare"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipElementArhitectural(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Element Arhitectural"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipElementDePeisaj(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Element De Peisaj"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class SpatiiBiserica(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Spatii Biserica"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipStructuraFundatie(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Structură Fundatie"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class MaterialeStructuraFundatieSoclu(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Materiale Structură Fundație Soclu"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipStructuraSoclu(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Structură Soclu"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class FinisajeSoclu(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Finisaje Soclu"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipAsezareTalpi(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Așezare Talpi"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipAsezareTalpiTransversaleFataDeCeleLongitudinale(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Așezare Tălpi Transversale Fata De Cele Longitudinale"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipImbinareDeColtTalpi(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Imbinare De Colt Talpi"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class EsentaLemnoasa(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Esenta Lemnoasa"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipPrelucrareALemnului(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Prelucrare A Lemnului"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipStructuraMaterialePardoseala(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Structură Materiale Pardoseala"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class FinisajePardoseala(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Finisaje Pardoseala"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipStructuraPeretiExteriori(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Structură Pereti Exteriori"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipStructuraCheotoare(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Structură Cheotoare"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipStructuraCatei(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Structură Catei"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipConsole(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Console"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipMaterialStructuraPereti(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Material Structură Pereti"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipFinisajExteriorPereti(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Finisaj Exterior Pereti"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipFinisajInteriorPereti(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Finisaj Interior Pereti"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipStructuraPeretiInteriori(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Structură Pereti Interiori"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipMaterialPeretiInteriori(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Material Pereti Interiori"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipFinisajPeretiInteriori(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Finisaj Pereti Interiori"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipGoluriPeretePronaosNaos(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Goluri Perete Pronaos Naos"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipTiranti(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Tiranti"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipBoltaTavanCupola(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Bolta Tavan Cupola"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class StructuraBolta(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Structura Bolta"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class StructuraTavan(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Structura Tavan"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class FinisajBoltaTavanCupola(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Finisaj Bolta Tavan Cupola"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class StructuraBoltaTavan(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Structura Bolta Tavan"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class MaterialStructuraBoltaTavanCupola(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Material Structură Bolta Tavan Cupola"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class RelatieBoltaAltarNaos(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Relatie Bolta Altar Naos"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class StructuraCupola(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Structura Cupola"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipStructuraCor(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Structură Cor"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class MaterialCor(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Material Cor"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class FinisajCor(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Finisaj Cor"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipSarpanta(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Sarpanta"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TehnicaDeConstructie(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tehnica De Constructie"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class MaterialInvelitoare(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Material Invelitoare"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipulDeBatere(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipul De Batere"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipulDePrindere(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipul De Prindere"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class FormaBotului(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Forma Botului"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipPrelucrareSindrila(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Prelucrare Sindrila"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class EsentaLemnoasaSindrila(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Esenta Lemnoasa Sindrila"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipDegradareFinisajeBoltiTavaneCupole(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Degradare Finisaje Bolti Tavane Cupole"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class AmplasareTurn(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Amplasare Turn"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class DimensiuneTurn(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Dimensiune Turn"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class MorfologieCoif(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Morfologie Coif"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class PlanTurn(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Plan Turn"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipGalerieTurn(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Galerie Turn"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class AsezareTalpiTurn(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Asezare Tălpi Turn"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class RelatieTalpiTurn(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Relatie Tălpi Turn"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class AmplasareTurle(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Amplasare Turle"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class MorfologieTurle(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Morfologie Turle"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipIconostas(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Iconostas"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class MaterialeIconostas(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Materiale Iconostas"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TehnicaPicturiiIconostasului(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tehnica Picturii Iconostasului"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class ProportiePicturaIconostas(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Proporție Pictură Iconostas"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class ElementeComponenteIconostas(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Elemente Componente Iconostas"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TehnicaPicturiiDecoratiei(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tehnica Picturii Decorației"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class ProportiaDeSuprafataAcoperitaVizibila(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Proportia De Suprafata Acoperita Vizibila"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class JustificareDatarePicturaDecoratieMuralaExterioara(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Justificare Datare Pictură Decorație Murală Exterioară"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class NotaStareElementeSculptateDecoratii(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Nota Stare Elemente Sculptate Decorații"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class IcoaneMobileDinBiserica(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Icoane Mobile Din Biserică"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class ObiecteDeCultIstorice(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Obiecte De Cult Istorice"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class MobilierIstoric(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Mobilier Istoric"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class NotaStareMobilier(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Nota Stare Mobilier"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TehnicaPicturiiDecoratieiMurale(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tehnica Picturii Decorației Murale"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class JustificareDatarePicturaDecoratieMuralaPereteDespartitor(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Justificare Datare Pictură Decorație Murală Perete Despărțitor"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


class TipDegradarePicturaDecoratieMuralaPereteDespartitor(models.Model):
    nume = models.CharField(max_length=300)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tip Degradare Pictură Decorație Murală Perete Despărțitor"
        ordering = ["nume"]

    def __str__(self):
        return self.nume


admin.site.register(Judet, GenericAdmin)
admin.site.register(Comuna, GenericAdmin)
admin.site.register(Localitate, GenericAdmin)
admin.site.register(CategorieObiectiv, GenericAdmin)
admin.site.register(Statut, GenericAdmin)
admin.site.register(Hram, GenericAdmin)
admin.site.register(Cult, GenericAdmin)
admin.site.register(FrecventaUtilizarii, GenericAdmin)
admin.site.register(Singularitate, GenericAdmin)
admin.site.register(TipArtera, GenericAdmin)
admin.site.register(TipRegimProprietate, GenericAdmin)
admin.site.register(TipFormaRelief, GenericAdmin)
admin.site.register(TipReperHidrografic, GenericAdmin)
admin.site.register(TipZoneNaturale, GenericAdmin)
admin.site.register(Bibliografie, GenericAdmin)
admin.site.register(JustificareDatare, GenericAdmin)
admin.site.register(TipPisanie, GenericAdmin)
admin.site.register(Secol, GenericAdmin)
admin.site.register(TipCadruPeisaj, GenericAdmin)
admin.site.register(TipLoc, GenericAdmin)
admin.site.register(TipRelatieCuCimitirul, GenericAdmin)
admin.site.register(NotaStareConservare, GenericAdmin)
admin.site.register(TipDegradare, GenericAdmin)
admin.site.register(TipRisc, GenericAdmin)
admin.site.register(InterventiiNecesare, GenericAdmin)
admin.site.register(TipElementArhitectural, GenericAdmin)
admin.site.register(TipElementDePeisaj, GenericAdmin)
admin.site.register(SpatiiBiserica, GenericAdmin)
admin.site.register(TipStructuraFundatie, GenericAdmin)
admin.site.register(MaterialeStructuraFundatieSoclu, GenericAdmin)
admin.site.register(TipStructuraSoclu, GenericAdmin)
admin.site.register(FinisajeSoclu, GenericAdmin)
admin.site.register(TipAsezareTalpi, GenericAdmin)
admin.site.register(TipAsezareTalpiTransversaleFataDeCeleLongitudinale, GenericAdmin)
admin.site.register(TipImbinareDeColtTalpi, GenericAdmin)
admin.site.register(EsentaLemnoasa, GenericAdmin)
admin.site.register(TipPrelucrareALemnului, GenericAdmin)
admin.site.register(TipStructuraMaterialePardoseala, GenericAdmin)
admin.site.register(FinisajePardoseala, GenericAdmin)
admin.site.register(TipStructuraPeretiExteriori, GenericAdmin)
admin.site.register(TipStructuraCheotoare, GenericAdmin)
admin.site.register(TipStructuraCatei, GenericAdmin)
admin.site.register(TipConsole, GenericAdmin)
admin.site.register(TipMaterialStructuraPereti, GenericAdmin)
admin.site.register(TipFinisajExteriorPereti, GenericAdmin)
admin.site.register(TipFinisajInteriorPereti, GenericAdmin)
admin.site.register(TipStructuraPeretiInteriori, GenericAdmin)
admin.site.register(TipMaterialPeretiInteriori, GenericAdmin)
admin.site.register(TipFinisajPeretiInteriori, GenericAdmin)
admin.site.register(TipGoluriPeretePronaosNaos, GenericAdmin)
admin.site.register(TipTiranti, GenericAdmin)
admin.site.register(TipBoltaTavanCupola, GenericAdmin)
admin.site.register(StructuraBolta, GenericAdmin)
admin.site.register(StructuraTavan, GenericAdmin)
admin.site.register(FinisajBoltaTavanCupola, GenericAdmin)
admin.site.register(StructuraBoltaTavan, GenericAdmin)
admin.site.register(MaterialStructuraBoltaTavanCupola, GenericAdmin)
admin.site.register(RelatieBoltaAltarNaos, GenericAdmin)
admin.site.register(StructuraCupola, GenericAdmin)
admin.site.register(TipStructuraCor, GenericAdmin)
admin.site.register(MaterialCor, GenericAdmin)
admin.site.register(FinisajCor, GenericAdmin)
admin.site.register(TipSarpanta, GenericAdmin)
admin.site.register(TehnicaDeConstructie, GenericAdmin)
admin.site.register(MaterialInvelitoare, GenericAdmin)
admin.site.register(TipulDeBatere, GenericAdmin)
admin.site.register(TipulDePrindere, GenericAdmin)
admin.site.register(FormaBotului, GenericAdmin)
admin.site.register(TipPrelucrareSindrila, GenericAdmin)
admin.site.register(EsentaLemnoasaSindrila, GenericAdmin)
admin.site.register(TipDegradareFinisajeBoltiTavaneCupole, GenericAdmin)
admin.site.register(AmplasareTurn, GenericAdmin)
admin.site.register(DimensiuneTurn, GenericAdmin)
admin.site.register(MorfologieCoif, GenericAdmin)
admin.site.register(PlanTurn, GenericAdmin)
admin.site.register(TipGalerieTurn, GenericAdmin)
admin.site.register(AsezareTalpiTurn, GenericAdmin)
admin.site.register(RelatieTalpiTurn, GenericAdmin)
admin.site.register(AmplasareTurle, GenericAdmin)
admin.site.register(MorfologieTurle, GenericAdmin)
admin.site.register(TipIconostas, GenericAdmin)
admin.site.register(MaterialeIconostas, GenericAdmin)
admin.site.register(TehnicaPicturiiIconostasului, GenericAdmin)
admin.site.register(ProportiePicturaIconostas, GenericAdmin)
admin.site.register(ElementeComponenteIconostas, GenericAdmin)
admin.site.register(TehnicaPicturiiDecoratiei, GenericAdmin)
admin.site.register(ProportiaDeSuprafataAcoperitaVizibila, GenericAdmin)
admin.site.register(JustificareDatarePicturaDecoratieMuralaExterioara, GenericAdmin)
admin.site.register(NotaStareElementeSculptateDecoratii, GenericAdmin)
admin.site.register(IcoaneMobileDinBiserica, GenericAdmin)
admin.site.register(ObiecteDeCultIstorice, GenericAdmin)
admin.site.register(MobilierIstoric, GenericAdmin)
admin.site.register(NotaStareMobilier, GenericAdmin)
admin.site.register(TehnicaPicturiiDecoratieiMurale, GenericAdmin)
admin.site.register(JustificareDatarePicturaDecoratieMuralaPereteDespartitor, GenericAdmin)
admin.site.register(TipDegradarePicturaDecoratieMuralaPereteDespartitor, GenericAdmin)
