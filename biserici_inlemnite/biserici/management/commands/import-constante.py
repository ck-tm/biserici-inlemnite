from django.core.management.base import BaseCommand
from django.db.models import Count
from django.contrib.auth.models import Group
import csv
from pprint import pprint
from nomenclatoare import models
from datetime import datetime


FUNCTIUNI = [
    "Biserică de parohie",
    "Mânăstire",
    "Schit",
    "Capelă",
    "Muzeu",
]

JUDETE = {
    "AB": "Alba",
    "AG": "Argeș",
    "AR": "Arad",
    "BC": "Bacău",
    "BH": "Bihor",
    "BN": "Bistrița-Năsăud",
    "BR": "Brăila",
    "BV": "Brașov",
    "BT": "Botoșani",
    "BZ": "Buzău",
    "CJ": "Cluj",
    "CL": "Călărași",
    "CS": "Caraș-Severin",
    "CT": "Constanța",
    "CV": "Covasna",
    "DB": "Dâmbovița",
    "DJ": "Dolj",
    "GJ": "Gorj",
    "GL": "Galați",
    "GR": "Giurgiu",
    "HD": "Hunedoara",
    "HR": "Harghita",
    "IL": "Ialomița",
    "IS": "Iași",
    "MH": "Mehedinți",
    "MM": "Maramureș",
    "MS": "Mureș",
    "NT": "Neamț",
    "OT": "Olt",
    "PH": "Prahova",
    "SB": "Sibiu",
    "SJ": "Sălaj",
    "SM": "Satu-MARE",
    "SV": "Suceava",
    "TL": "Tulcea",
    "TM": "Timiș",
    "TR": "Teleorman",
    "VL": "Vâlcea",
    "VN": "Vrancea",
    "VS": "Vaslui",
    "IF": "Ilfov",
    "B": "București"
}

IDENTIFICARE_STATUT = [
    'Clasat UNESCO (importanță mondială)',
    'Clasat Categoria A (importanță națională)',
    'Clasat Categoria B (importanță regională)',
    'Neclasat',
    'În curs de clasare',
    'În curs de declasare',
    'Decalasat parțial',
]

IDENTIFICARE_CULT = [
    "Biserica Ortodoxă Română",
    "Biserica Română Unită cu Roma, Greco-Catolică",
    "Biserica Romano-Catolică",
    "Biserica Reformată din România",
    "Episcopia Ortodoxă Sârbă de Timişoara",
    "Arhiepiscopia Bisericii Armene",
    "Biserica Ortodoxă de Rit Vechi din România",
    "Biserica Evanghelică C.A. din România",
    "Biserica Evanghelică Lutherană din România",
    "Biserica Unitariană Maghiară",
    "Cultul Creștin Baptist- Uniunea Bisericilor Creştine Baptiste din România",
    "Biserica Creştină După Evanghelie din România",
    "Biserica Evanghelică Română",
    "Cultul Creștin Penticostal – Biserica lui Dumnezeu Apostolică din România",
    "Biserica Adventistă de Ziua a Şaptea din România",
    "Federaţia Comunităţilor Evreieşti din România- Cultul Mozaic",
    "Cultul Musulman",
    "Organizaţia Religioasă “Martorii lui Iehova”",
]

IDENTIFICARE_UTILIZARE = [
    'Folosită permanent (săptămânal)',
    'Folosită permanent (prin rotație)',
    'Folosită ocazional',
    'Nefolosită',
]


IDENTIFICARE_SINGULARITATE = (
    'Singura biserică de același rit din localitate',
    'Dublată',
)

IDENTIFICARE_PROPRIETATE = [
    "Proprietate privată a persoanelor juridice",
    "Proprietate din domeniul public al Statului/unităților adm-teritoriale/ins. de stat",
    "Proprietate din domeniul privat al Statului/unităților adm-teritoriale/ins. de stat",
    "Proprietate privată a persoanelor fizice",
]


SURSA_DATARE = [
    "Pisanie tradusă",
    "Studiu dendrocronologic",

]

SECOL = [
    "I",
    "II",
    "III",
    "IV",
    "V",
    "VI",
    "VII",
    "VIII",
    "IX",
    "X",
    "XI",
    "XII",
    "XIII",
    "XIV",
    "XV",
    "XVI",
    "XVII",
    "XVII",
    "XIX",
    "XX",
]

AMPLASAMENT = [
    "În cadrul așezării",
    "În afara așezării"
]

TOPOGRAFIE = [
    "La nivel cu așezarea",
    "La înălțime",

]

RELATIE_CIMITIR = [
    "În cadrul cimitirului",
    "În altă locație",
]

PEISAGISTICA_SIT = [
    "Cimitir dens",
    "Cimitir livadă",
    "Cimitir fâneață",
    "Livadă",
    "Fâneață",
    "Aliniamente de arbori",
    "Pădure",
    "Țesut urban",
]

ELEMENT_ANSAMBLU_CONSTRUIT = [
    "Turn clopotniță exterior",
    "Poartă acces în incintă",
]

ELEMENT_IMPORTANT = [
    "Troiță",
    "Monumente funerare",
    "Fântână",
    "Arbore de strajă",
]

PLANIMETRIE = [
    "1.1.1",
    "1.1.2",
    "1.1.3",
    "1.1.4",
    "1.1.5",
    "1.2.1",
    "1.2.2",
    "1.2.3",
    "1.2.4",
    "1.3.1",
    "1.3.2",
    "1.3.3",
    "1.3.4",
    "1.4.2",
    "1.4.3",
    "1.4.4",
    "1.5.2",
    "1.6.2",
    "1.6.3",
    "1.6.4",
    "1.7.2",
    "1.7.3",
    "2.1.2",
    "2.1.3",
    "2.1.4",
    "2.1.6",
    "2.1.7",
    "2.2.2",
    "2.2.3",
    "2.2.4",
    "2.3.2",
    "2.3.3",
    "2.3.4",
    "2.3.5",
    "2.3.6",
    "2.3.7",
    "2.4.2",
    "2.4.4",
    "2.4.8",
    "2.5.3",
    "2.6.1",
    "2.6.2",
    "2.6.3",
    "2.6.4",
    "2.7.4",
    "2.8.4",
    "3.1.2",
    "3.1.4",
    "3.2.2",
    "3.2.4",
    "4.1.1",
    "4.1.2",
    "4.2.2",
    "4.3.2",
    "5.1.4",
    "5.2.4",
    "5.3.4",
    "5.4.4",
    "5.5.4",
]

MATERIAL = [
    "Lemn",
    "Piatră",
    "Zidărie",
    "Mixt",



]

DIMENSIUNE_TURN = [
    "Scund",
    "Normal (raportul dintre înălțimea bisericii și lungimea ei este mai mic decât 1)",
    "Înalt (raportul dintre înălțimea bisericii și lungimea ei este mai mare decât 1)",
    "Turn supraînălțat (coiful)",
    "Turn supraînălțat (pătratul turnului)",

]


TIP_TURN = [
    "Turn ascuțit (gotic)",
    "Turn baroc",
]

DECOR_TURN = [
    "Turn ascuțit (gotic)",
    "Turn baroc",
]

PLAN_TURN = [
    "pătrat",
    "dreptunghiular",
    "hexagonal",
    "rotund",
    "romb",
]

AMPLASARE_TURN = [
    "peste pronaos",
    "peste pridvor",
]

GALERIE_TURN = [
    "deschisă",
    "închisă",
    "închisă cu orificii",
    "galerie dublă",
    "galerie ieșită în exterior",
]


TIP_SARPANTA = [
    "Șarpantă generală",
    "Șarpantă cu poale",
    "Șarpantă cu timpan / timpane pe latura vestică",
    "Șarpantă restrânsă peste altar racordată",
    "Șarpantă restrânsă peste altar cu timpan",
    "Șarpantă barocă",
]

FINISAJ_EXTERIOR = [
    "Structura din lemn",
    "Tencuială + zugraveală",
    "Tencuială + pictură ",
    "Draniță / Șiță / Șindrilă",
    "Scândură verticală",
    "Scândură orizontală",
    "Țiglă",
    "Tablă",
]

TIP_BATERE_SINDRILA = [
    "în linie dreaptă alăturate",
    "în linie dreaptă cu suprapunere laterală",
    "solzi alăturați",
    "solzi suprapuși lateral",
]

TIP_PRINDERE_SINDRILA = [
    "cuie normale",
    "cuie de fierar",
    "cule de lemn",
]

TIP_BOT_SINDRILA = [
    "dreaptă",
    "cu vârf (în unghi)",
    "cu vârf retezat",
    "bot de rață",
    "coadă de rândunică",
    "în trepte",
]

TIP_PRELUCRARE_SINDRILA = [
    "mauală",
    "mecanizată",
]

ESENTA_LEMNOASA = [
    "rășinos (molid / brad)",
    "stejar",
    "fag",
]

ELEMENTE_BISERICA = [
    "portic",
    "pronaos",
    "naos",
    "solee",
    "altar"
]


MATERIAL_FINISAJ_PARDOSELI = [
    "Podele lemn",
    "Pământ (lutuire)",
    "Piatră",
    "Mixt",
]

MATERIAL_FINISAJ_PERETI_INTERIORI = [
    "Structura din lemn",
    "Scândură",
    "Pictură direct pe bârnele de lemn",
    "Pictură pe scândură",
    "Tencuială + zugraveală",
    "Mixt",
]

FINISAJ = [
    "Pictate integral",
    "Pictate parțial",
    "Tencuite și zugravite",
    "Lemn natur",
    "Altele",
]

TIP_FUNDATIE = [
    "Așezată pe un soclu zidit de piatră",
    "Așezată pe pietre izolate",
    "Așezată pe fundație de beton armat",
    "Așezată pe fundație de cărămidă",
]

TIP_STRUCTURA_CHEOTOARE = [
    "Coadă de rândunică",
    "Unghi drept",
    "Cu crestături multiple",
    "Cu dinte",
]

TIP_STRUCTURA_CATEI = [
    "Umplutură cu groși",
    "Umplutură cu scândură bătută",
    "Nuiele",
]

LOCALIZARE_PICTURA = [
    "Integral ",
    "Parțial ",
    "Nepictat",
]

TEHNICA_PICTURA = [
    "distemper",
    "tempera",
    "vopsele pe bază de ulei",
]

FINISAJ_ICONOSTAS = [
    "Pictat",
    "Pictat parțial",
    "Icoane vechi aplicate",
    "Icoane împărătești",
    "Sculptat",
    "Nepictat",
]

TIP_ICONOSTAS = [
    "Tâmplă",
    "Fruntar",
    "Fruntar sub tâmplă",
]




class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting import..")
        for cod, nume in JUDETE.items():
            print(f"Import JUDETE: {nume}")
            models.Judet.objects.get_or_create(
                nume=nume,
                cod=cod)
            Group.objects.get_or_create(name=nume)
        for nume in FUNCTIUNI:
            print(f"Import FUNCTIUNI: {nume}")
            models.FunctiuneBiserica.objects.get_or_create(
                nume=nume)

        for nume in IDENTIFICARE_CULT:
            print(f"Import IDENTIFICARE_CULT: {nume}")
            models.CultBiserica.objects.get_or_create(
                nume=nume)

        for nume in IDENTIFICARE_UTILIZARE:
            print(f"Import IDENTIFICARE_UTILIZARE: {nume}")
            models.UtilizareBiserica.objects.get_or_create(
                nume=nume)

        for nume in IDENTIFICARE_SINGULARITATE:
            print(f"Import IDENTIFICARE_SINGULARITATE: {nume}")
            models.SingularitateBiserica.objects.get_or_create(
                nume=nume)

        for nume in IDENTIFICARE_STATUT:
            print(f"Import IDENTIFICARE_STATUT: {nume}")
            models.StatutBiserica.objects.get_or_create(
                nume=nume)

        for nume in IDENTIFICARE_PROPRIETATE:
            print(f"Import IDENTIFICARE_PROPRIETATE: {nume}")
            models.ProprietateBiserica.objects.get_or_create(
                nume=nume)

        for nume in SURSA_DATARE:
            print(f"Import SURSA_DATARE: {nume}")
            models.SursaDatare.objects.get_or_create(
                nume=nume)

        for nume in SECOL:
            print(f"Import SECOL: {nume}")
            models.Secol.objects.get_or_create(
                nume=nume)

        for nume in AMPLASAMENT:
            print(f"Import AMPLASAMENT: {nume}")
            models.AmplasamentBiserica.objects.get_or_create(
                nume=nume)

        for nume in TOPOGRAFIE:
            print(f"Import TOPOGRAFIE: {nume}")
            models.TopografieBiserica.objects.get_or_create(
                nume=nume)


        for nume in RELATIE_CIMITIR:
            print(f"Import RELATIE_CIMITIR: {nume} ")
            models.RelatieCimitir.objects.get_or_create(
                nume=nume)
        for nume in PEISAGISTICA_SIT:
            print(f"Import PEISAGISTICA_SIT: {nume} ")
            models.PeisagisticaSit.objects.get_or_create(
                nume=nume)
        for nume in ELEMENT_ANSAMBLU_CONSTRUIT:
            print(f"Import ELEMENT_ANSAMBLU_CONSTRUIT: {nume} ")
            models.ElementAnsambluConstruit.objects.get_or_create(
                nume=nume)
        for nume in ELEMENT_IMPORTANT:
            print(f"Import ELEMENT_IMPORTANT: {nume} ")
            models.ElementImportant.objects.get_or_create(
                nume=nume)
        for nume in PLANIMETRIE:
            print(f"Import PLANIMETRIE: {nume} ")
            models.Planimetrie.objects.get_or_create(
                nume=nume)
        for nume in MATERIAL:
            print(f"Import MATERIAL: {nume} ")
            models.Material.objects.get_or_create(
                nume=nume)
        for nume in DIMENSIUNE_TURN:
            print(f"Import DIMENSIUNE_TURN: {nume} ")
            models.DimensiuneTurn.objects.get_or_create(
                nume=nume)
        for nume in TIP_TURN:
            print(f"Import TIP_TURN: {nume} ")
            models.TipTurn.objects.get_or_create(
                nume=nume)
        for nume in DECOR_TURN:
            print(f"Import DECOR_TURN: {nume} ")
            models.DecorTurn.objects.get_or_create(
                nume=nume)
        for nume in PLAN_TURN:
            print(f"Import PLAN_TURN: {nume} ")
            models.PlanTurn.objects.get_or_create(
                nume=nume)
        for nume in AMPLASARE_TURN:
            print(f"Import AMPLASARE_TURN: {nume} ")
            models.AmplasareTurn.objects.get_or_create(
                nume=nume)
        for nume in GALERIE_TURN:
            print(f"Import GALERIE_TURN: {nume} ")
            models.GalerieTurn.objects.get_or_create(
                nume=nume)
        for nume in TIP_SARPANTA:
            print(f"Import TIP_SARPANTA: {nume} ")
            models.TipSarpanta.objects.get_or_create(
                nume=nume)
        for nume in FINISAJ_EXTERIOR:
            print(f"Import FINISAJ_EXTERIOR: {nume} ")
            models.FinisajExterior.objects.get_or_create(
                nume=nume)
        for nume in TIP_BATERE_SINDRILA:
            print(f"Import TIP_BATERE_SINDRILA: {nume} ")
            models.TipBatereSindrila.objects.get_or_create(
                nume=nume)
        for nume in TIP_PRINDERE_SINDRILA:
            print(f"Import TIP_PRINDERE_SINDRILA: {nume} ")
            models.TipPrindereSindrila.objects.get_or_create(
                nume=nume)
        for nume in TIP_BOT_SINDRILA:
            print(f"Import TIP_BOT_SINDRILA: {nume} ")
            models.TipBotSindrila.objects.get_or_create(
                nume=nume)
        for nume in TIP_PRELUCRARE_SINDRILA:
            print(f"Import TIP_PRELUCRARE_SINDRILA: {nume} ")
            models.TipPrelucrareSindrila.objects.get_or_create(
                nume=nume)
        for nume in ESENTA_LEMNOASA:
            print(f"Import ESENTA_LEMNOASA: {nume} ")
            models.EsentaLemnoasa.objects.get_or_create(
                nume=nume)
        for nume in ELEMENTE_BISERICA:
            print(f"Import ELEMENTE_BISERICA: {nume} ")
            models.ElementeBiserica.objects.get_or_create(
                nume=nume)
        for nume in MATERIAL_FINISAJ_PARDOSELI:
            print(f"Import MATERIAL_FINISAJ_PARDOSELI: {nume} ")
            models.MaterialFinisajPardoseli.objects.get_or_create(
                nume=nume)
        for nume in MATERIAL_FINISAJ_PERETI_INTERIORI:
            print(f"Import MATERIAL_FINISAJ_PERETI_INTERIORI: {nume} ")
            models.MaterialFinisajPeretiInteriori.objects.get_or_create(
                nume=nume)
        for nume in FINISAJ:
            print(f"Import FINISAJ: {nume} ")
            models.Finisaj.objects.get_or_create(
                nume=nume)
        for nume in TIP_FUNDATIE:
            print(f"Import TIP_FUNDATIE: {nume} ")
            models.TipFundatie.objects.get_or_create(
                nume=nume)
        for nume in TIP_STRUCTURA_CHEOTOARE:
            print(f"Import TIP_STRUCTURA_CHEOTOARE: {nume} ")
            models.TipStructuraCheotoare.objects.get_or_create(
                nume=nume)
        for nume in TIP_STRUCTURA_CATEI:
            print(f"Import TIP_STRUCTURA_CATEI: {nume} ")
            models.TipStructuraCatei.objects.get_or_create(
                nume=nume)
        for nume in LOCALIZARE_PICTURA:
            print(f"Import LOCALIZARE_PICTURA: {nume} ")
            models.LocalizarePictura.objects.get_or_create(
                nume=nume)
        for nume in TEHNICA_PICTURA:
            print(f"Import TEHNICA_PICTURA: {nume} ")
            models.TehnicaPictura.objects.get_or_create(
                nume=nume)
        for nume in FINISAJ_ICONOSTAS:
            print(f"Import FINISAJ_ICONOSTAS: {nume} ")
            models.FinisajIconostas.objects.get_or_create(
                nume=nume)
        for nume in TIP_ICONOSTAS:
            print(f"Import TIP_ICONOSTAS: {nume} ")
            models.TipIconostas.objects.get_or_create(
                nume=nume)