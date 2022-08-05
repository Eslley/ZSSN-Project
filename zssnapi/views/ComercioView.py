from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from zssnapi.models.InventarioModel import InventarioModel
from zssnapi.models.SobreviventeModel import SobreviventeModel
from zssnapi.serializers.ComercioSerializer import ComercioSerializer
from django.db import transaction
 
@api_view(['POST'])
def negociar(request):
    serializer = ComercioSerializer(data=request.data)

    if serializer.is_valid():

        sId1 = serializer.data.get('sobrevivente1').get('sobrevivente')
        sId2 = serializer.data.get('sobrevivente2').get('sobrevivente')

        itens1 = serializer.data.get('sobrevivente1').get('itens')
        itens2 = serializer.data.get('sobrevivente2').get('itens')

        inventario1 = InventarioModel.objects.filter(sobrevivente=sId1)
        inventario2 = InventarioModel.objects.filter(sobrevivente=sId2)
        
        #descontar itens inventario do sobrevivente1
        # for item in itens1:
        #     inventario1.filter(item=item.get('id'), quantidade__gt=item.get('quantidade'))
        #     if inventario1.count():
        #         print("Tem " + inventario1.item + " qtd " + inventario1.quantidade)
        #         if inventario1.quantidade == item.get('quantidade'):
        #             print("remove")
        #             #inventario1.delete()
        #         else:
        #             print("subtrai")
    else:
        return Response(serializer.errors, status=status.HTTP_200_OK)

    return Response(serializer.data, status=status.HTTP_200_OK)
   
    