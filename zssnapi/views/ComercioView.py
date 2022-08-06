from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from zssnapi.models.InventarioModel import InventarioModel
from zssnapi.models.ItemModel import ItemModel
from zssnapi.models.SobreviventeModel import SobreviventeModel
from zssnapi.serializers.ComercioSerializer import ComercioSerializer
from django.db import transaction
from django.db.models import F
from django.core.exceptions import EmptyResultSet
 
@api_view(['POST'])
def negociar(request):
    serializer = ComercioSerializer(data=request.data)

    if serializer.is_valid():

        sId1 = serializer.data.get('sobrevivente1').get('sobrevivente')
        sId2 = serializer.data.get('sobrevivente2').get('sobrevivente')

        itens1 = serializer.data.get('sobrevivente1').get('itens')
        itens2 = serializer.data.get('sobrevivente2').get('itens')
        
        transaction.set_autocommit(False)
        try:
            retirarItens(sId1, itens1)
            retirarItens(sId2, itens2)

            adicionarItens(sId1, itens2)
            adicionarItens(sId2, itens1)
        except EmptyResultSet:
            transaction.rollback()
            return Response({'message': 'Item oferecido não está no inventário do sobrevivente'}, status=status.HTTP_200_OK)
        except:
            transaction.rollback()
        else:
            transaction.commit()
            return Response({'message': 'Troca realizada com sucesso'}, status=status.HTTP_200_OK)
        finally:
            transaction.set_autocommit(True)

    else:
        return Response(serializer.errors, status=status.HTTP_200_OK)

    

def retirarItens(sId, itens):
    for item in itens:
        inventario = InventarioModel.objects.filter(sobrevivente=sId, item=item.get('id'), quantidade__gte=item.get('quantidade'))
        if inventario.count():
            data = inventario.values()[0]
            if data['quantidade'] == item.get('quantidade'):
                inventario.delete()
            else:
                inventario.update(quantidade=F('quantidade') - item.get('quantidade'))

        else:
            raise EmptyResultSet()
    
    return True

def adicionarItens(sId, itens):
    for item in itens:
        inventario = InventarioModel.objects.filter(sobrevivente=sId, item=item.get('id'))
        if inventario.count():
            qtd = inventario.values()[0]['quantidade']
            inventario.update(quantidade=qtd+item.get('quantidade'))
        else:
            InventarioModel.objects.create(sobrevivente=SobreviventeModel.objects.get(pk=sId), item=ItemModel.objects.get(pk=item.get('id')), quantidade=item.get('quantidade'))