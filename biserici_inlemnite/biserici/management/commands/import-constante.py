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
    "Tablă",
    "Fier"
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

ASEZARE_TALPA_TURN = [
    "tălpile turnului intră în corpul bisericii",
    "tălpile turnului se așează pe butea bisericii",
]
RELATIE_TALPA_TURN = [
    "cele paralele cu axul bisericii deasupra",
    "cele perpendiculare pe axul bisericii deasupra",
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

ELEMENT_BISERICA = [
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

SUPORT_PICTURA = [
    "lemn",
    "pânză",
    "tencuială",
]

TEHNICA_PICTURA = [
    "tempera slabă",
    "tempera",
    "ulei de in",
    # "alseco",
    # "fresco",
    # "vopsele pe bază de ulei",
]

FINISAJ_ICONOSTAS = [
    "Pictat",
    "Pictat parțial",
    "Icoane vechi aplicate",
    "Icoane împărătești",
    "Sculptat",
    "Nepictat",
]




TIPURI_USI = [
    "împărătești",
    "diaconești"
]


REGISTRU_ICONOSTAS = [
    "poale",
    "icoanelor împărătești",
    "prăznicale",
    "apostoli",
    "prooroci",
    "crucea cu molenii",
]

TIP_ICONOSTAS = [
    "Tâmplă",
    "Fruntar",
    "Fruntar sub tâmplă",
]

DETALIU_POD_TURN = [
    "timpanul",
    "balconul",
    "clopotul",
    "șarpanta turnului",
    "marcaje dulgherești",
    "îmbinări",
]

TIP_BOLTA_PRONAOS = [
    "Boltă semicilindrică",
    "Boltă poligonală în secțiune",
    "Cupolă",
    "Intersecții de bolți",
    "Fără",

]

BOLTA_PESTE_ALTAR = [
    "În prelungirea bolții peste naos",
    "Retrasă față de bolta naosului",
    "Fără",
]

TIP_BOLTA_PESTE_ALTAR = [
    "Lunetă",
    "Semicilindrică",
    "Semicalotă sferică",
    "Calotă sferică",
]

MOBILIER = [
    "strane",
    "scaun", 
    "arhieresc",
    "tetrapoade",
    "bănucuțe",
    "cuiere",
    "anvone",
    "cafas",
    "cor",
    "pangar",
    "cutia milei"
    "tetrapod"
]

OBIECTE_CULT = [
    "epitaf",
    "ripidă",
    "cruce",
    "candelă",
    "chivot",
    "sfeșnic",
    "candelabru",
    "potir",
    "textile"
]

POZITIONARE_TURLE = [
    "deasupra pronaosului",
    "deasupra naosului",
    "pe absidiole",
]

FORMA_SARPANTE_TURLE = [
    "barocă",
    "coif simplu cu pantă frântă",

]


TIP_TIRANTI = [
    "tirant istoric din lemn",
    "element metalic ulterior",
    "element lemn ulterior",
]


MATERIAL_INVELITOARE_TURLE = [
    "scândură",
    "lambriu",
    "șindrilă",
    "tencuială",

]

HRAMURI = [
    "Sfântul Andrei‎",
    "Sfânta Ana‎",
    "Sfântul Anton de Padova‎",
    "Sfânta Barbara‎",
    "Sfântul Bartolomeu‎",
    "Buna Vestire‎",
    "Sfântul Clement‎",
    "Sfânta Cruce‎",
    "Sfântul Dumitru‎",
    "Sfântul Egidiu‎",
    "Sfântul Francisc de Assisi‎",
    "Sfântul Francisc Xavier‎",
    "Sfântul Gheorghe‎",
    "Sfântul Iacob‎",
    "Sfântul Ilarie‎",
    "Sfântul Ilie‎",
    "Sfânta Inimă a lui Isus‎",
    "Sfântul Ioan Botezătorul‎",
    "Sfântul Ioan Evanghelistul‎",
    "Sfântul Ioan Nepomuk‎",
    "Sfântul Iosif‎",
    "Înălțarea Domnului‎",
    "Învierea Domnului‎",
    "Sfântul Kilian‎",
    "Sfântul Ladislau‎",
    "Sfântul Laurențiu‎",
    "Sfântul Lazăr‎",
    "Sfântul Martin‎",
    "Sfânta Maria‎",
    "Sfânta Maria Magdalena‎",
    "Sfântul Mauriciu‎",
    "Sfântul Mihail‎",
    "Sfântul Nicolae‎",
    "Sfântul Petru‎",
    "Sfântul Pavel‎",
    "Sfântul Servatius‎",
    "Toți Sfinții‎",
    "Trei Ierarhi‎",
    "Sfânta Treime‎",
    "Sfântul Vasile‎",
    "Sfântul Virgil‎",
]


MATERIALE_STRUCTURA_BOLTA = [
    "metal", 
    "lambriu", 
    "blăni", 
    "scândură", 
    "scândură pe arce", 

]


TIP_SISTEM_STRUCTURAL = [
    "În cheotoare",
    "În căței",
    "Mixt",
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
            try:
                models.FunctiuneBiserica.objects.get_or_create(
                    nume=nume)
            except:
                pass

        for nume in IDENTIFICARE_CULT:
            print(f"Import IDENTIFICARE_CULT: {nume}")
            try:
                models.CultBiserica.objects.get_or_create(
                    nume=nume)
            except:
                pass

        for nume in IDENTIFICARE_UTILIZARE:
            print(f"Import IDENTIFICARE_UTILIZARE: {nume}")
            try:
                models.UtilizareBiserica.objects.get_or_create(
                    nume=nume)
            except:
                pass

        for nume in IDENTIFICARE_SINGULARITATE:
            print(f"Import IDENTIFICARE_SINGULARITATE: {nume}")
            try:
                models.SingularitateBiserica.objects.get_or_create(
                    nume=nume)
            except:
                pass

        for nume in IDENTIFICARE_STATUT:
            print(f"Import IDENTIFICARE_STATUT: {nume}")
            try:
                models.StatutBiserica.objects.get_or_create(
                    nume=nume)
            except:
                pass

        for nume in IDENTIFICARE_PROPRIETATE:
            print(f"Import IDENTIFICARE_PROPRIETATE: {nume}")
            try:
                models.ProprietateBiserica.objects.get_or_create(
                    nume=nume)
            except:
                pass

        for nume in SURSA_DATARE:
            print(f"Import SURSA_DATARE: {nume}")
            try:
                models.SursaDatare.objects.get_or_create(
                    nume=nume)
            except:
                pass

        for nume in SECOL:
            print(f"Import SECOL: {nume}")
            try:
                models.Secol.objects.get_or_create(
                    nume=nume)
            except:
                pass

        for nume in AMPLASAMENT:
            print(f"Import AMPLASAMENT: {nume}")
            try:
                models.AmplasamentBiserica.objects.get_or_create(
                    nume=nume)
            except:
                pass

        for nume in TOPOGRAFIE:
            print(f"Import TOPOGRAFIE: {nume}")
            try:
                models.TopografieBiserica.objects.get_or_create(
                    nume=nume)
            except:
                pass


        for nume in RELATIE_CIMITIR:
            print(f"Import RELATIE_CIMITIR: {nume} ")
            try:
                models.RelatieCimitir.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in PEISAGISTICA_SIT:
            print(f"Import PEISAGISTICA_SIT: {nume} ")
            try:
                models.PeisagisticaSit.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in ELEMENT_ANSAMBLU_CONSTRUIT:
            print(f"Import ELEMENT_ANSAMBLU_CONSTRUIT: {nume} ")
            try:
                models.ElementAnsambluConstruit.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in ELEMENT_IMPORTANT:
            print(f"Import ELEMENT_IMPORTANT: {nume} ")
            try:
                models.ElementImportant.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in PLANIMETRIE:
            print(f"Import PLANIMETRIE: {nume} ")
            try:
                models.Planimetrie.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in MATERIAL:
            print(f"Import MATERIAL: {nume} ")
            try:
                models.Material.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in DIMENSIUNE_TURN:
            print(f"Import DIMENSIUNE_TURN: {nume} ")
            try:
                models.DimensiuneTurn.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in TIP_TURN:
            print(f"Import TIP_TURN: {nume} ")
            try:
                models.TipTurn.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in DECOR_TURN:
            print(f"Import DECOR_TURN: {nume} ")
            try:
                models.DecorTurn.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in PLAN_TURN:
            print(f"Import PLAN_TURN: {nume} ")
            try:
                models.PlanTurn.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in AMPLASARE_TURN:
            print(f"Import AMPLASARE_TURN: {nume} ")
            try:
                models.AmplasareTurn.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in GALERIE_TURN:
            print(f"Import GALERIE_TURN: {nume} ")
            try:
                models.GalerieTurn.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in TIP_SARPANTA:
            print(f"Import TIP_SARPANTA: {nume} ")
            try:
                models.TipSarpanta.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in FINISAJ_EXTERIOR:
            print(f"Import FINISAJ_EXTERIOR: {nume} ")
            try:
                models.FinisajExterior.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in TIP_BATERE_SINDRILA:
            print(f"Import TIP_BATERE_SINDRILA: {nume} ")
            try:
                models.TipBatereSindrila.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in TIP_PRINDERE_SINDRILA:
            print(f"Import TIP_PRINDERE_SINDRILA: {nume} ")
            try:
                models.TipPrindereSindrila.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in TIP_BOT_SINDRILA:
            print(f"Import TIP_BOT_SINDRILA: {nume} ")
            try:
                models.TipBotSindrila.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in TIP_PRELUCRARE_SINDRILA:
            print(f"Import TIP_PRELUCRARE_SINDRILA: {nume} ")
            try:
                models.TipPrelucrareSindrila.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in ESENTA_LEMNOASA:
            print(f"Import ESENTA_LEMNOASA: {nume} ")
            try:
                models.EsentaLemnoasa.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in ELEMENT_BISERICA:
            print(f"Import ELEMENT_BISERICA: {nume} ")
            try:
                models.ElementBiserica.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in MATERIAL_FINISAJ_PARDOSELI:
            print(f"Import MATERIAL_FINISAJ_PARDOSELI: {nume} ")
            try:
                models.MaterialFinisajPardoseli.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in MATERIAL_FINISAJ_PERETI_INTERIORI:
            print(f"Import MATERIAL_FINISAJ_PERETI_INTERIORI: {nume} ")
            try:
                models.MaterialFinisajPeretiInteriori.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in FINISAJ:
            print(f"Import FINISAJ: {nume} ")
            try:
                models.Finisaj.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in TIP_FUNDATIE:
            print(f"Import TIP_FUNDATIE: {nume} ")
            try:
                models.TipFundatie.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in TIP_STRUCTURA_CHEOTOARE:
            print(f"Import TIP_STRUCTURA_CHEOTOARE: {nume} ")
            try:
                models.TipStructuraCheotoare.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in TIP_STRUCTURA_CATEI:
            print(f"Import TIP_STRUCTURA_CATEI: {nume} ")
            try:
                models.TipStructuraCatei.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in LOCALIZARE_PICTURA:
            print(f"Import LOCALIZARE_PICTURA: {nume} ")
            try:
                models.LocalizarePictura.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in TEHNICA_PICTURA:
            print(f"Import TEHNICA_PICTURA: {nume} ")
            try:
                models.TehnicaPictura.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in SUPORT_PICTURA:
            print(f"Import SUPORT_PICTURA: {nume} ")
            try:
                models.SuportPictura.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in FINISAJ_ICONOSTAS:
            print(f"Import FINISAJ_ICONOSTAS: {nume} ")
            try:
                models.FinisajIconostas.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in TIP_ICONOSTAS:
            print(f"Import TIP_ICONOSTAS: {nume} ")
            try:
                models.TipIconostas.objects.get_or_create(
                    nume=nume)
            except:
                pass


        for nume in TIPURI_USI:
            print(f"Import TIPURI_USI: {nume} ")
            try:
                models.TipUsiIconostas.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in REGISTRU_ICONOSTAS:
            print(f"Import REGISTRU_ICONOSTAS: {nume} ")
            try:
                models.RegistruIconostas.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in DETALIU_POD_TURN:
            print(f"Import DETALIU_POD_TURN: {nume} ")
            try:
                models.DetaliuPodTurn.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in ASEZARE_TALPA_TURN:
            print(f"Import ASEZARE_TALPA_TURN: {nume} ")
            try:
                models.AsezareTalpaTurn.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in RELATIE_TALPA_TURN:
            print(f"Import RELATIE_TALPA_TURN: {nume} ")
            try:
                models.RelatieTalpaTurn.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in BOLTA_PESTE_ALTAR:
            print(f"Import BOLTA_PESTE_ALTAR: {nume} ")
            try:
                models.BoltaPesteAltar.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in TIP_BOLTA_PESTE_ALTAR:
            print(f"Import TIP_BOLTA_PESTE_ALTAR: {nume} ")
            try:
                models.TipBoltaPesteAltar.objects.get_or_create(
                    nume=nume)
            except:
                pass
        for nume in TIP_BOLTA_PRONAOS:
            print(f"Import TIP_BOLTA_PRONAOS: {nume} ")
            try:
                models.TipBoltaPronaos.objects.get_or_create(
                    nume=nume)
            except:
                pass

        for nume in MOBILIER:
            print(f"Import MOBILIER: {nume} ")
            try:
                models.Mobilier.objects.get_or_create(
                    nume=nume)
            except:
                pass

        for nume in OBIECTE_CULT:
            print(f"Import OBIECTE_CULT: {nume} ")
            try:
                models.ObiectCult.objects.get_or_create(
                    nume=nume)
            except:
                pass

        for nume in POZITIONARE_TURLE:
            print(f"Import POZITIONARE_TURLE: {nume} ")
            try:
                models.PozitionareTurle.objects.get_or_create(
                    nume=nume)
            except:
                pass

        for nume in FORMA_SARPANTE_TURLE:
            print(f"Import FORMA_SARPANTE_TURLE: {nume} ")
            try:
                models.FormaSarpanteTurle.objects.get_or_create(
                    nume=nume)
            except:
                pass


        for nume in TIP_TIRANTI:
            print(f"Import TIP_TIRANTI: {nume} ")
            try:
                models.TipTiranti.objects.get_or_create(
                    nume=nume)
            except:
                pass

        for nume in MATERIAL_INVELITOARE_TURLE:
            print(f"Import MATERIAL_INVELITOARE_TURLE: {nume} ")
            try:
                models.MaterialInvelitoareTurle.objects.get_or_create(
                    nume=nume)
            except:
                pass

        for nume in HRAMURI:
            print(f"Import HRAMURI: {nume} ")
            try:
                models.Hram.objects.get_or_create(
                    nume=nume)
            except:
                pass

        for nume in MATERIALE_STRUCTURA_BOLTA:
            print(f"Import MATERIALE_STRUCTURA_BOLTA: {nume} ")
            try:
                models.MaterialeStructuraBolta.objects.get_or_create(
                    nume=nume)
            except:
                pass

        for nume in TIP_SISTEM_STRUCTURAL:
            print(f"Import TIP_SISTEM_STRUCTURAL: {nume} ")
            try:
                models.TipSistemStructural.objects.get_or_create(
                    nume=nume)
            except:
                pass

