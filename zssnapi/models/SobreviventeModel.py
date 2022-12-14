from math import fabs
from django.db import models

class SobreviventeModel(models.Model):

    class Meta:
        
        db_table = 'sobrevivente'

    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1)
    latitude = models.FloatField()
    longitude = models.FloatField()
    estaInfectado = models.BooleanField(default=False)
    countAlertInfected = models.IntegerField(default=0)

    def __str__(self):
        return self.nome