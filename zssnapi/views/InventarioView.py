from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from zssnapi.models import InventarioModel
from zssnapi.models.SobreviventeModel import SobreviventeModel
from zssnapi.serializers.InventarioSerializer import InventarioSerializer

@api_view(['GET'])
def inventariosList(request):
    try:

        sobreviventes = SobreviventeModel.objects.all().values('id', 'nome')
        data = inventarioSobrevivente(sobreviventes)

        return Response({'inventarios': data}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'message': e}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def inventarioDetail(request, fk):
    try:
        sobrevivente = SobreviventeModel.objects.get(id=fk)
        if sobrevivente.estaInfectado:
            return Response({'message': 'Não é possível acessar inventário, sobrevivente infectado'}, status=status.HTTP_403_FORBIDDEN)
        else:
            inventarios = InventarioModel.objects.filter(sobrevivente=fk)
            serializer = InventarioSerializer(inventarios, many=True)

            return Response({'sobreviventeId': fk, 'sobrevivente': sobrevivente.nome, 'itens': serializer.data}, status=status.HTTP_200_OK)
    except SobreviventeModel.DoesNotExist:
        return Response({'message': 'Sobrevivente não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
def inventarioSobrevivente(sobreviventes):
    data = []

    for s in sobreviventes:
        inventarios = InventarioModel.objects.filter(sobrevivente=s['id'])
        serializer = InventarioSerializer(inventarios, many=True)

        data.append(
            {
                'sobreviventeId': s['id'],
                'sobrevivente': s['nome'],
                'itens': serializer.data
            }
        )

    return data