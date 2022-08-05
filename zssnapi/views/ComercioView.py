from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from zssnapi.models.InventarioModel import InventarioModel
from zssnapi.models.ItemModel import ItemModel
from zssnapi.models.SobreviventeModel import SobreviventeModel
from zssnapi.serializers.ComercioSerializer import ComercioSerializer
from django.db import transaction
from django.db.models import F
 
@api_view(['POST'])
def negociar(request):
    serializer = ComercioSerializer(data=request.data)

    if serializer.is_valid():

        sId1 = serializer.data.get('sobrevivente1').get('sobrevivente')
        sId2 = serializer.data.get('sobrevivente2').get('sobrevivente')

        itens1 = serializer.data.get('sobrevivente1').get('itens')
        itens2 = serializer.data.get('sobrevivente2').get('itens')
        
        trocar(sId1, sId2, itens1)

        trocar(sId2, sId1, itens2)
    else:
        return Response(serializer.errors, status=status.HTTP_200_OK)

    return Response({'message': 'Troca realizada com sucesso'}, status=status.HTTP_200_OK)

def trocar(sId1, sId2, itens):
    for item in itens:
        inventario1 = InventarioModel.objects.filter(sobrevivente=sId1, item=item.get('id'), quantidade__gte=item.get('quantidade'))
        if inventario1.count():
            data = inventario1.values()[0]
            if data['quantidade'] == item.get('quantidade'):
                inventario1.delete()
            else:
                inventario1.update(quantidade=F('quantidade') - item.get('quantidade'))
            
            inventario2 = InventarioModel.objects.filter(sobrevivente=sId2, item=item.get('id'))
            if inventario2.count():
                qtd = inventario2.values()[0]['quantidade']
                inventario2.update(quantidade=qtd+item.get('quantidade'))
            else:
                InventarioModel.objects.create(sobrevivente=SobreviventeModel.objects.get(pk=sId2), item=ItemModel.objects.get(pk=item.get('id')), quantidade=item.get('quantidade'))

        else:
            return Response({'message': 'Item oferecido não está no inventário do sobrevivente'}, status=status.HTTP_200_OK)
