from rest_framework import serializers
from zssnapi.models import InventarioModel
from zssnapi.serializers.ItemSerializer import ItemSerializer

class InventarioSerializer(serializers.ModelSerializer):

    class Meta:

        model = InventarioModel
        exclude = ['id']

    def to_representation(self, instance):

        return {
            'item': ItemSerializer(instance.item).data,
            'quantidade': instance.quantidade
        }