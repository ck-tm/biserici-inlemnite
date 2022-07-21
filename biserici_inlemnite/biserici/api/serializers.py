from django.utils import timezone
from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework_guardian.serializers import ObjectPermissionsAssignmentMixin
from drf_writable_nested.serializers import WritableNestedModelSerializer

from guardian.shortcuts import get_objects_for_user, assign_perm, remove_perm
from guardian.core import ObjectPermissionChecker
from biserici import models
from pprint import pprint


class DatareSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.Datare
        fields = "__all__"


class JustificareDatareSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.JustificareDatare
        fields = "__all__"


class InterventieSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.Interventie
        fields = "__all__"


class StareConservareSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.StareConservare
        fields = "__all__"


class FotografieSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.Fotografie
        exclude = ["id"]


class IstoricPersoanaSerializer(WritableNestedModelSerializer):
    foto = FotografieSerializer(many=True)

    class Meta:
        model = models.IstoricPersoana
        exclude = ["id"]


class IstoricScurtIstoricSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.IstoricScurtIstoric
        fields = "__all__"


class IstoricPisanieSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.IstoricPisanie
        fields = "__all__"


class IstoricEvenimentSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.IstoricEveniment
        fields = "__all__"


class IstoricMutareSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.IstoricMutare
        fields = "__all__"


class IstoricSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.Istoric
        exclude = ["biserica"]


class IdentificareFrecventaUtilizariiSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.IdentificareFrecventaUtilizarii
        fields = "__all__"


class IdentificareSingularitateSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.IdentificareSingularitate
        fields = "__all__"


class IdentificareSerializer(WritableNestedModelSerializer):
    frecventa_utilizarii = IdentificareFrecventaUtilizariiSerializer()
    singularitate = IdentificareSingularitateSerializer()

    class Meta:
        model = models.Identificare
        exclude = ["biserica"]


class LocalizareUnitatiTeritorialeSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.LocalizareUnitatiTeritoriale
        fields = "__all__"


class LocalizareAdresaCoordonateGPSSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.LocalizareAdresaCoordonateGPS
        fields = "__all__"


class LocalizareAdresaSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.LocalizareAdresa
        fields = "__all__"


class LocalizareReferinteCadastraleSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.LocalizareReferinteCadastrale
        fields = "__all__"


class LocalizareRegimulDeProprietateSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.LocalizareRegimulDeProprietate
        fields = "__all__"


class LocalizareSerializer(WritableNestedModelSerializer):
    unitati_teritoriale = LocalizareUnitatiTeritorialeSerializer()
    adresa = LocalizareAdresaSerializer()
    referinte_cadastrale = LocalizareReferinteCadastraleSerializer()
    regim_proprietate = LocalizareRegimulDeProprietateSerializer()

    class Meta:
        model = models.Localizare
        exclude = ["biserica"]


class RepereGeograficeFormaReliefSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.RepereGeograficeFormaRelief
        fields = "__all__"


class RepereGeograficeReperHidrograficSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.RepereGeograficeReperHidrografic
        fields = "__all__"


class RepereGeograficeZoneNaturaleSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.RepereGeograficeZoneNaturale
        fields = "__all__"


class RepereGeograficeSerializer(WritableNestedModelSerializer):
    forma_relief = RepereGeograficeFormaReliefSerializer()
    reper_hidrografic = RepereGeograficeReperHidrograficSerializer()
    zone_naturale = RepereGeograficeZoneNaturaleSerializer()

    class Meta:
        model = models.RepereGeografice
        exclude = ["biserica"]


class IstoricSerializer(WritableNestedModelSerializer):
    scurt_istoric = IstoricScurtIstoricSerializer()
    pisanie = IstoricPisanieSerializer()
    ctitori = IstoricPersoanaSerializer(many=True)
    mesteri = IstoricPersoanaSerializer(many=True)
    zugravi = IstoricPersoanaSerializer(many=True)
    personalitati = IstoricPersoanaSerializer(many=True)
    evenimente = IstoricEvenimentSerializer(many=True)
    mutari = IstoricMutareSerializer(many=True)

    class Meta:
        model = models.Istoric
        exclude = ["biserica"]


class PeisajPeisajCulturalCadruSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.PeisajPeisajCulturalCadru
        fields = "__all__"


class PeisajPeisajCulturalPatrimoniuImaterialSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.PeisajPeisajCulturalPatrimoniuImaterial
        fields = "__all__"


class PeisajPeisajCulturalSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.PeisajPeisajCultural
        fields = "__all__"


class PeisajAmplasamentLocSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.PeisajAmplasamentLoc
        fields = "__all__"


class PeisajAmplasamentToponimSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.PeisajAmplasamentToponim
        fields = "__all__"


class PeisajAmplasamentRelatiaCuCimitirulSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.PeisajAmplasamentRelatiaCuCimitirul
        fields = "__all__"


class PeisajAmplasamentSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.PeisajAmplasament
        fields = "__all__"


class PeisajAnsambluConstruitElementArhitecturalSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.PeisajAnsambluConstruitElementArhitectural
        fields = "__all__"


class PeisajAnsambluConstruitElementPeisajSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.PeisajAnsambluConstruitElementPeisaj
        fields = "__all__"


class PeisajAnsambluConstruitSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.PeisajAnsambluConstruit
        fields = "__all__"


class PeisajSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.Peisaj
        exclude = ["biserica"]


class ABGeneralPlanimetriaBisericiiSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABGeneralPlanimetriaBisericii
        fields = "__all__"


class ABGeneralSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABGeneral
        fields = "__all__"


class ABFundatieSocluFundatieStructuraSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABFundatieSocluFundatieStructura
        fields = "__all__"


class ABFundatieSocluFundatieMaterialeSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABFundatieSocluFundatieMateriale
        fields = "__all__"


class ABFundatieSocluFundatieSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABFundatieSocluFundatie
        fields = "__all__"


class ABFundatieSocluSocluStructuraSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABFundatieSocluSocluStructura
        fields = "__all__"


class ABFundatieSocluSocluMaterialeSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABFundatieSocluSocluMateriale
        fields = "__all__"


class ABFundatieSocluSocluFinisajeSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABFundatieSocluSocluFinisaje
        fields = "__all__"


class ABFundatieSocluSocluSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABFundatieSocluSoclu
        fields = "__all__"


class ABFundatieSocluSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABFundatieSoclu
        fields = "__all__"


class ABCorpTalpiMaterialSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorpTalpiMaterial
        fields = "__all__"


class ABCorpTalpiSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorpTalpi
        fields = "__all__"


class ABCorpPardosealaStructuraPardosealaSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorpPardosealaStructuraPardoseala
        fields = "__all__"


class ABCorpPardosealaFinisajeSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorpPardosealaFinisaje
        fields = "__all__"


class ABCorpPardosealaSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorpPardoseala
        fields = "__all__"


class StructuraPeretiInterioriSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.StructuraPeretiInteriori
        fields = "__all__"


class ABCorpPeretiExterioriStructuraChetoareSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorpPeretiExterioriStructuraChetoare
        fields = "__all__"


class ABCorpPeretiExterioriStructuraCateiSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorpPeretiExterioriStructuraCatei
        fields = "__all__"


class ABCorpPeretiExterioriStructuraFurciSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorpPeretiExterioriStructuraFurci
        fields = "__all__"


class ABCorpPeretiExterioriSistemStructuralMixtSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorpPeretiExterioriSistemStructuralMixt
        fields = "__all__"


class ABCorpPeretiExterioriConsoleSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorpPeretiExterioriConsole
        fields = "__all__"


class MaterialStructuraPeretiSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.MaterialStructuraPereti
        fields = "__all__"


class ABCorpPeretiExterioriFinisajeExterioareSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorpPeretiExterioriFinisajeExterioare
        fields = "__all__"


class FinisajInteriorSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.FinisajInterior
        fields = "__all__"


class ABCorpPeretiExterioriSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorpPeretiExteriori
        fields = "__all__"


class MaterialStructuraPeretiInterioriSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.MaterialStructuraPeretiInteriori
        fields = "__all__"


class ABCorpPereteNaosAltarSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorpPereteNaosAltar
        fields = "__all__"


class ABCorpPeretePronaosNaosSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorpPeretePronaosNaos
        fields = "__all__"


class ABCorpGoluriIntrariDinspreExteriorSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorpGoluriIntrariDinspreExterior
        fields = "__all__"


class ABCorpGoluriTreceriIntreSpatiiSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorpGoluriTreceriIntreSpatii
        fields = "__all__"


class ABCorpGoluriFerestreSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorpGoluriFerestre
        fields = "__all__"


class ABCorpGoluriOchiesiSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorpGoluriOchiesi
        fields = "__all__"


class ABCorpGoluriSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorpGoluri
        fields = "__all__"


class ExistaObservatiiImaginiSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ExistaObservatiiImagini
        fields = "__all__"


class ABCorpAlteElementeComponenteAleCorpuluiBisericiiTirantiSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorpAlteElementeComponenteAleCorpuluiBisericiiTiranti
        fields = "__all__"


class ABCorpAlteElementeComponenteAleCorpuluiBisericiiSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorpAlteElementeComponenteAleCorpuluiBisericii
        fields = "__all__"


class ABCorpSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorp
        fields = "__all__"


class StructuraBoltaTavanSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.StructuraBoltaTavan
        fields = "__all__"


class MaterialStructuraBoltaTavanSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.MaterialStructuraBoltaTavan
        fields = "__all__"


class RubricaBoltaTavanSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.RubricaBoltaTavan
        fields = "__all__"


class ABBoltiTavaneSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABBoltiTavane
        fields = "__all__"


class ABCorStructuraSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorStructura
        fields = "__all__"


class ABCorMaterialStructuraSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCorMaterialStructura
        fields = "__all__"


class ABCorSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABCor
        fields = "__all__"


class ABSarpantaCorpBisericaCaracteristiciSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABSarpantaCorpBisericaCaracteristici
        fields = "__all__"


class ABSarpantaCorpBisericaStructuraSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABSarpantaCorpBisericaStructura
        fields = "__all__"


class ABSarpantaCorpBisericaMaterialStructuraSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABSarpantaCorpBisericaMaterialStructura
        fields = "__all__"


class FinisajInvelitoareSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.FinisajInvelitoare
        fields = "__all__"


class EtapaAnterioareInvelitoareSindrilaSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.EtapaAnterioareInvelitoareSindrila
        fields = "__all__"


class ABSarpantaCorpBisericaSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABSarpantaCorpBiserica
        fields = "__all__"


class ABTurnCaracteristiciGalerieSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABTurnCaracteristiciGalerie
        fields = "__all__"


class ABTurnCaracteristiciClopotSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABTurnCaracteristiciClopot
        fields = "__all__"


class ABTurnCaracteristiciSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABTurnCaracteristici
        fields = "__all__"


class ABTurnStructuraSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABTurnStructura
        fields = "__all__"


class ABTurnSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABTurn
        fields = "__all__"


class ABTurleCaracteristiciSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABTurleCaracteristici
        fields = "__all__"


class ABTurleStructuraSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABTurleStructura
        fields = "__all__"


class ABTurleSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ABTurle
        fields = "__all__"


class ArhitecturaBisericiiSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ArhitecturaBisericii
        exclude = ["biserica"]


class CAGeneralSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.CAGeneral
        fields = "__all__"


class CAIconostasTipologieSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.CAIconostasTipologie
        fields = "__all__"


class CAIconostasMaterialeSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.CAIconostasMateriale
        fields = "__all__"


class CAIconostasPicturaSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.CAIconostasPictura
        fields = "__all__"


class CAIconostasScultpturaSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.CAIconostasScultptura
        fields = "__all__"


class CAIconostasComponenteSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.CAIconostasComponente
        fields = "__all__"


class CAIconostasSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.CAIconostas
        fields = "__all__"


class CAProportieSuprafataSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.CAProportieSuprafata
        fields = "__all__"


class CAMuralaSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.CAMurala
        fields = "__all__"


class CAElementeSculptateAlteDecoratiiSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.CAElementeSculptateAlteDecoratii
        fields = "__all__"


class CAObiecteDeCultIstoriceSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.CAObiecteDeCultIstorice
        fields = "__all__"


class CAMobilierIstoricSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.CAMobilierIstoric
        fields = "__all__"


class CAPereteNaosPronaosSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.CAPereteNaosPronaos
        fields = "__all__"


class ComponenteArtisticeSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ComponenteArtistice
        exclude = ["biserica"]


class RiscuriInstalatiiSerializer(WritableNestedModelSerializer):
    imagini = FotografieSerializer(many=True)

    class Meta:
        model = models.RiscuriInstalatii
        fields = "__all__"


class InstalatiiEchipamenteSerializer(WritableNestedModelSerializer):
    instalatii_electrice = RiscuriInstalatiiSerializer()
    paratraznet = RiscuriInstalatiiSerializer()
    instalatii_termice = RiscuriInstalatiiSerializer()
    pichet_psi = RiscuriInstalatiiSerializer()
    monitorizare_antiefractie_si_vandalism = RiscuriInstalatiiSerializer()

    class Meta:
        model = models.InstalatiiEchipamente
        exclude = ["biserica"]


class CalificativValoareSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.CalificativValoare
        fields = "__all__"


class ValoareSerializer(WritableNestedModelSerializer):
    vechime = CalificativValoareSerializer()
    integritate = CalificativValoareSerializer()
    unicitate = CalificativValoareSerializer()
    valoare_memoriala = CalificativValoareSerializer()
    peisaj_cultural = CalificativValoareSerializer()
    sit = CalificativValoareSerializer()
    arhitecturala = CalificativValoareSerializer()
    mestesug = CalificativValoareSerializer()
    componente_artistice = CalificativValoareSerializer()
    folosinta_actuala = CalificativValoareSerializer()
    relevanta_actuala = CalificativValoareSerializer()
    potential = CalificativValoareSerializer()
    bioculturala = CalificativValoareSerializer()
    imateriala = CalificativValoareSerializer()

    class Meta:
        model = models.Valoare
        exclude = ["biserica"]


class BisericaSerializer(ObjectPermissionsAssignmentMixin, WritableNestedModelSerializer):
    identificare = IdentificareSerializer()
    localizare = LocalizareSerializer()
    repere_geografice = RepereGeograficeSerializer()
    istoric = IstoricSerializer()
    peisaj = PeisajSerializer()
    arhitectura_bisericii = ArhitecturaBisericiiSerializer()
    componente_artistice = ComponenteArtisticeSerializer()
    instalatii_echipamente = InstalatiiEchipamenteSerializer()
    valoare = ValoareSerializer()

    class Meta:
        model = models.Biserica
        fields = ["nume"]
        fields = [
            "pk",
            "nume",
            "identificare",
            "localizare",
            "repere_geografice",
            "istoric",
            "peisaj",
            "arhitectura_bisericii",
            "componente_artistice",
            "instalatii_echipamente",
            "valoare",
        ]

    def get_permissions_map(self, created):
        current_user = self.context["request"].user
        instance = self.instance
        grup_judet = None

        # if instance.descriere.judet:
        #     judet_biserica = instance.descriere.judet.nume
        #     grup_judet, _ = Group.objects.get_or_create(name=judet_biserica)

        return {
            "view_biserica": [current_user, grup_judet],
            "change_biserica": [current_user, grup_judet],
            "delete_biserica": [],
        }


class BisericaListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:biserici-detail")
    # capitole = serializers.SerializerMethodField()

    class Meta:
        model = models.Biserica
        fields = ["nume", "pk", "url"]
        # fields = ["nume", "pk", "url", "capitole"]
