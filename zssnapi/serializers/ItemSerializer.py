from rest_framework import serializers
from zssnapi.models import ItemModel

class ItemSerializer(serializers.ModelSerializer):

    class Meta:

        model = ItemModel
        fields = '__all__'

    def validate_pontos(self, value):

        if value <= 0:
             raise serializers.ValidationError('Quantidade de pontos é menor que 1')

        return value