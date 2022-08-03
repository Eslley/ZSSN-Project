from django.db import models

from . import SobreviventeModel

from . import ItemModel

class InventarioModel(models.Model):

    class Meta:
        
        db_table = 'inventario'

    sobrevivente = models.ForeignKey(SobreviventeModel, on_delete=models.CASCADE)
    item = models.ForeignKey(ItemModel, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    