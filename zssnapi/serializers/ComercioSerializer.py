from rest_framework import serializers
from zssnapi.models.SobreviventeModel import SobreviventeModel

class ComercioSerializer(serializers.Serializer):
    sobrevivente1 = serializers.DictField(required=True)
    sobrevivente2 = serializers.DictField(required=True)

    def validate_sobrevivente1(self, value):

        if not 'sobrevivente' in value:
            raise serializers.ValidationError('Falta id do sobrevivente')

        if not 'itens' in value or len(value['itens']) == 0:
            raise serializers.ValidationError('Itens vazios')

        return value

    def validate_sobrevivente2(self, value):

        if not 'sobrevivente' in value:
            raise serializers.ValidationError('Falta id do sobrevivente')

        if not 'itens' in value or len(value['itens']) == 0:
            raise serializers.ValidationError('Itens vazios')

        return value

    def validate(self, data):
        
        countPoints1 = 0
        countPoints2 = 0

        for itens in data['sobrevivente1']['itens']:
            countPoints1 += itens["pontos"] * itens["quantidade"]
        
        for itens in data['sobrevivente2']['itens']:
            countPoints2 += itens["pontos"] * itens["quantidade"]

        if countPoints1 != countPoints2:
            raise serializers.ValidationError('Quantidade de pontos diferente')

        isInfectado1 = SobreviventeModel.objects.get(id=data['sobrevivente1']['sobrevivente']).estaInfectado
        isInfectado2 = SobreviventeModel.objects.get(id=data['sobrevivente2']['sobrevivente']).estaInfectado

        print(isInfectado1)
        print(isInfectado2)
        
        if isInfectado1 or isInfectado2:
            raise serializers.ValidationError('Sobrevivente infectado, a troca não é possível')

        return data
