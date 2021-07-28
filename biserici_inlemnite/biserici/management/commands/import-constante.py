from django.core.management.base import BaseCommand
from django.db.models import Count
from django.contrib.auth.models import Group
import csv
from pprint import pprint
from biserici import models
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