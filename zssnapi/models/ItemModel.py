from django.db import models

class ItemModel(models.Model):

    class Meta:
        
        db_table = 'item'

    nome = models.CharField(max_length=255)
    pontos = models.IntegerField()