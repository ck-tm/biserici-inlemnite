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
        


class PeisagisticaSit(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Peisagistică Sit"
        


class ElementAnsambluConstruit(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Elemente Ansamblu Construit"
        


class ElementImportant(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Elemente Importante"
        


class Planimetrie(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Planimetrii"
        


class Material(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Materiale"
        


class DimensiuneTurn(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Dimensiuni Turn"
        


class TipTurn(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipuri Turn"
        


class DecorTurn(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Decoruri Turn"
        


class PlanTurn(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Planuri Turn"
        


class AmplasareTurn(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Amplasări Turn"
        


class GalerieTurn(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Galerii Turn"
        


class TipSarpanta(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipuri Sarpanta"
        


class FinisajExterior(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Finisaj Exterior"
        


class TipBatereSindrila(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipuri Batere Sindrila"
        


class TipPrindereSindrila(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipuri Prindere Sindrila"
        


class TipBotSindrila(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipuri Bot Sindrila"
        


class TipPrelucrareSindrila(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipuri Prelucrare Sindrila"
        


class EsentaLemnoasa(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Esenta Lemnoasa"
        


class ElementeBiserica(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Elemente Biserica"
        


class MaterialFinisajPardoseli(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Material Finisaj Pardoseli"
        


class MaterialFinisajPeretiInteriori(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Material Finisaj Pereti Interiori"
        


class Finisaj(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Finisaj"
        


class TipFundatie(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipuri Fundatie"
        


class TipStructuraCheotoare(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipuri Structură Cheotoare"
        


class TipStructuraCatei(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipuri Structură Căței"
        


class LocalizarePictura(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Localizări Pictură"
        


class TehnicaPictura(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tehnici Pictura"
        


class FinisajIconostas(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Finisaje Iconostas"
        


class TipIconostas(models.Model):
    nume = models.CharField(max_length=150)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Tipuri Iconostas"
        