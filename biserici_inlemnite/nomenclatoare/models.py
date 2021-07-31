from django.db import models
from simple_history.models import HistoricalRecords



class Judet(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=50)
    cod = models.CharField(max_length=2)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Județe"

    def __str__(self):
        return self.nume


class Localitate(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=50)
    judet = models.ForeignKey('Judet', on_delete=models.CASCADE)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Localități"

    def __str__(self):
        return self.nume



class FunctiuneBiserica(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Funcțiuni Biserică"

    def __str__(self):
        return self.nume


class StatutBiserica(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()
    
    class Meta:
        verbose_name_plural = "Statuturi Biserică"
        

    def __str__(self):
        return self.nume


class CultBiserica(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()
    
    class Meta:
        verbose_name_plural = "Culturi Biserică"
        

    def __str__(self):
        return self.nume


class UtilizareBiserica(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()
    
    class Meta:
        verbose_name_plural = "Utilizări Biserică"
        

    def __str__(self):
        return self.nume


class SingularitateBiserica(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()
    
    class Meta:
        verbose_name_plural = "Singularități Biserică"
        

    def __str__(self):
        return self.nume


class ProprietateBiserica(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()
    
    class Meta:
        verbose_name_plural = "Proprietăți Biserică"
        

    def __str__(self):
        return self.nume


class MutareBiserica(models.Model):
    """
    Description: Model Description
    """
    istoric = models.ForeignKey('biserici.Istoric', on_delete=models.CASCADE)
    localitate = models.ForeignKey('Localitate', null=True, blank=True, on_delete=models.SET_NULL)
    latitudine = models.FloatField(null=True, blank=True)
    longitudine = models.FloatField(null=True, blank=True)
    history = HistoricalRecords()
    
    class Meta:
        verbose_name_plural = 'Mutări Biserică'
        


class SursaDatare(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()
    
    class Meta:
        verbose_name_plural = 'Surse Datări'
        

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
    history = HistoricalRecords()
    
    class Meta:
        verbose_name_plural = 'Studii dendocronologice'
        

    def __str__(self):
        return f"{self.nume} - {self.autor} ({self.an})"

class Persoana(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()
    
    class Meta:
        verbose_name_plural = 'Persoane'
        

    def __str__(self):
        return self.nume


class Eveniment(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)
    history = HistoricalRecords()
    
    class Meta:
        verbose_name_plural = 'Evenimente'
        

    def __str__(self):
        return self.nume


class CtitorBiserica(models.Model):
    """
    Description: Model Description
    """
    persoana = models.ForeignKey('Persoana', on_delete=models.CASCADE)
    istoric = models.ForeignKey('biserici.Istoric', on_delete=models.SET_NULL, null=True, blank=True)
    detalii = models.TextField()
    sursa = models.TextField()
    history = HistoricalRecords()
    
    class Meta:
        verbose_name_plural = 'titori'
        

    def __str__(self):
        return self.nume

class ZugravBiserica(models.Model):
    """
    Description: Model Description
    """
    persoana = models.ForeignKey('Persoana', on_delete=models.CASCADE)
    istoric = models.ForeignKey('biserici.Istoric', on_delete=models.SET_NULL, null=True, blank=True)
    detalii = models.TextField()
    sursa = models.TextField()
    history = HistoricalRecords()
    
    class Meta:
        verbose_name_plural = 'ugravi'
        

    def __str__(self):
        return self.nume

class MesterBiserica(models.Model):
    """
    Description: Model Description
    """
    persoana = models.ForeignKey('Persoana', on_delete=models.CASCADE)
    istoric = models.ForeignKey('biserici.Istoric', on_delete=models.SET_NULL, null=True, blank=True)
    detalii = models.TextField()
    sursa = models.TextField()
    history = HistoricalRecords()
    
    class Meta:
        verbose_name_plural = 'eșteri'
        

    def __str__(self):
        return self.nume

class PersonalitateBiserica(models.Model):
    """
    Description: Model Description
    """
    persoana = models.ForeignKey('Persoana', on_delete=models.CASCADE)
    istoric = models.ForeignKey('biserici.Istoric', on_delete=models.SET_NULL, null=True, blank=True)
    detalii = models.TextField()
    sursa = models.TextField()
    history = HistoricalRecords()
    
    class Meta:
        verbose_name_plural = 'Personalități Biserică'
        

    def __str__(self):
        return self.nume


class EvenimentBiserica(models.Model):
    """
    Description: Model Description
    """
    eveniment = models.ForeignKey('Eveniment', on_delete=models.CASCADE)
    istoric = models.ForeignKey('biserici.Istoric', null=True, blank=True, on_delete=models.SET_NULL)
    detalii = models.TextField()
    sursa = models.TextField()
    history = HistoricalRecords()
    
    class Meta:
        verbose_name_plural = 'venimente Istorice'
        

    def __str__(self):
        return self.nume


class Studiu(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=150)
    fisier = models.FileField()
    history = HistoricalRecords()
    
    class Meta:
        verbose_name_plural = 'Studii'
        

    def __str__(self):
        return self.nume


class Secol(models.Model):
    """
    Description: Model Description
    """
    nume = models.CharField(max_length=6)
    history = HistoricalRecords()
    
    class Meta:
        verbose_name_plural = 'Secole'
        

    def __str__(self):
        return self.nume



class StudiuIstoric(models.Model):
    """
    Description: Model Description
    """
    istoric = models.ForeignKey('biserici.Istoric', on_delete=models.CASCADE)
    nume = models.CharField(max_length=150)
    fisier = models.FileField()
    drepturi_de_autor = models.TextField()
    history = HistoricalRecords()
    
    class Meta:
        verbose_name_plural = 'tudii Istorice'
        

    def __str__(self):
        return self.studiu.nume



class AmplasamentBiserica(models.Model):
    """
    Capitol: Amplasament Biserica
    """

    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Amplasamente Biserică"
        

    def __str__(self):
        return self.nume

class TopografieBiserica(models.Model):
    """
    Capitol: Topografie Biserica
    """

    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Topografii Biserică"
        

    def __str__(self):
        return self.nume

class RelatieCimitir(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Relație Cimitir"

    def __str__(self):
        return self.nume


class PeisagisticaSit(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Peisagistică Sit"

    def __str__(self):
        return self.nume


class ElementAnsambluConstruit(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Elemente Ansamblu Construit"

    def __str__(self):
        return self.nume


class ElementImportant(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Elemente Importante"

    def __str__(self):
        return self.nume


class Planimetrie(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Planimetrii"

    def __str__(self):
        return self.nume


class Material(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Materiale"

    def __str__(self):
        return self.nume


class DimensiuneTurn(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Dimensiuni Turn"

    def __str__(self):
        return self.nume


class TipTurn(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipuri Turn"

    def __str__(self):
        return self.nume


class DecorTurn(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Decoruri Turn"

    def __str__(self):
        return self.nume


class PlanTurn(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Planuri Turn"

    def __str__(self):
        return self.nume


class AmplasareTurn(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Amplasări Turn"

    def __str__(self):
        return self.nume


class GalerieTurn(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Galerii Turn"

    def __str__(self):
        return self.nume


class TipSarpanta(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipuri Sarpanta"

    def __str__(self):
        return self.nume


class FinisajExterior(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Finisaj Exterior"

    def __str__(self):
        return self.nume


class TipBatereSindrila(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipuri Batere Sindrila"

    def __str__(self):
        return self.nume


class TipPrindereSindrila(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipuri Prindere Sindrila"

    def __str__(self):
        return self.nume


class TipBotSindrila(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipuri Bot Sindrila"

    def __str__(self):
        return self.nume


class TipPrelucrareSindrila(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipuri Prelucrare Sindrila"

    def __str__(self):
        return self.nume


class EsentaLemnoasa(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Esenta Lemnoasa"

    def __str__(self):
        return self.nume


class ElementBiserica(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Elemente Biserica"

    def __str__(self):
        return self.nume


class MaterialFinisajPardoseli(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Material Finisaj Pardoseli"

    def __str__(self):
        return self.nume


class MaterialFinisajPeretiInteriori(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Material Finisaj Pereti Interiori"

    def __str__(self):
        return self.nume


class Finisaj(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Finisaj"

    def __str__(self):
        return self.nume


class TipFundatie(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipuri Fundatie"

    def __str__(self):
        return self.nume


class TipStructuraCheotoare(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipuri Structură Cheotoare"

    def __str__(self):
        return self.nume


class TipStructuraCatei(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipuri Structură Căței"

    def __str__(self):
        return self.nume


class LocalizarePictura(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Localizări Pictură"

    def __str__(self):
        return self.nume


class TehnicaPictura(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tehnici Pictura"

    def __str__(self):
        return self.nume



class SuportPictura(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Suport Pictură"

    def __str__(self):
        return self.nume


class FinisajIconostas(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Finisaje Iconostas"

    def __str__(self):
        return self.nume


class RegistruIconostas(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Registre Iconostas"

    def __str__(self):
        return self.nume


class TipIconostas(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipuri Iconostas"

    def __str__(self):
        return self.nume


class TipUsiIconostas(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipuri Uși Iconostas"

    def __str__(self):
        return self.nume


class DetaliuPodTurn(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Detalii podul turnului"

    def __str__(self):
        return self.nume



class AsezareTalpaTurn(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Așezări talpă turn"

    def __str__(self):
        return self.nume


class RelatieTalpaTurn(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Relații talpă turn"

    def __str__(self):
        return self.nume




class BoltaPesteAltar(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Bolți peste altar"

    def __str__(self):
        return self.nume


class TipBoltaPesteAltar(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipuri boltă peste altar"

    def __str__(self):
        return self.nume


class TipBoltaPronaos(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipuri boltă pronaos/naos"

    def __str__(self):
        return self.nume

class Mobilier( models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Mobilier"

    def __str__(self):
        return self.nume


class ObiectCult( models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Obiecte Cult"

    def __str__(self):
        return self.nume

