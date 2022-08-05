from rest_framework import serializers
from zssnapi.models import InventarioModel
from zssnapi.serializers.ItemSerializer import ItemSerializer
from zssnapi.serializers.SobreviventeSerializer import SobreviventeSerializer

class InventarioSerializer(serializers.ModelSerializer):

    item = ItemSerializer()
    sobrevivente = serializers.StringRelatedField()

    class Meta:

        model = InventarioModel
        exclude = ['id']