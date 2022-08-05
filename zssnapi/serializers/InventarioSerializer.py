from rest_framework import serializers
from zssnapi.models import InventarioModel
from zssnapi.models.SobreviventeModel import SobreviventeModel
from zssnapi.serializers.ItemSerializer import ItemSerializer
from zssnapi.serializers.SobreviventeSerializer import SobreviventeSerializer

class InventarioSerializer(serializers.ModelSerializer):

    class Meta:

        model = InventarioModel
        exclude = ['id']

    def to_representation(self, instance):
        return {
            'sobrevivente': SobreviventeSerializer(instance.sobrevivente).data['nome'],
            'item': ItemSerializer(instance.item).data
        }