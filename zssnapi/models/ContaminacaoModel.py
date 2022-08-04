from django.db import models
from zssnapi.models import SobreviventeModel

class ContaminacaoModel(models.Model):

    class Meta:
        
        db_table = 'contaminacao'

    informante = models.ForeignKey(SobreviventeModel, related_name='informante', on_delete=models.CASCADE)
    infectado = models.ForeignKey(SobreviventeModel, related_name='infectado', on_delete=models.CASCADE)
    createAt = models.DateField(auto_now_add=True)