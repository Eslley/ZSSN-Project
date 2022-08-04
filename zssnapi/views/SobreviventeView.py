import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from zssnapi.models import SobreviventeModel
from zssnapi.serializers import SobreviventeSerializer

@api_view(['GET'])
def sobreviventesList(request):
    sobreviventes = SobreviventeModel.objects.all()
    serializer = SobreviventeSerializer(sobreviventes, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def sobreviventeDetail(request, pk):
    sobreviventes = SobreviventeModel.objects.get(id=pk)
    serializer = SobreviventeSerializer(sobreviventes, many=False)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def alertaInfectado(request, pk):
    sobrevivente = SobreviventeModel.objects.get(id=pk)
    
    if sobrevivente.estaInfectado:
        return Response(sobrevivente.nome + " já está infectado", status=status.HTTP_200_OK)
    else:
        sobrevivente.countAlertInfected += 1
        if sobrevivente.countAlertInfected == 3:
            sobrevivente.estaInfectado = True
            sobrevivente.save(update_fields=['estaInfectado', 'countAlertInfected'])
        else:
            sobrevivente.save(update_fields=['countAlertInfected'])
    
        return Response("O alerta de infecção foi recebido", status=status.HTTP_200_OK)

@api_view(['POST'])
def sobreviventeCreate(request):
    serializer = SobreviventeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def sobreviventeDelete(request, pk):
    sobrevivente = SobreviventeModel.objects.get(id=pk)
    sobrevivente.delete()

    return Response("Sobrevivente Deletado", status=status.HTTP_200_OK)

@api_view(['PUT'])
def sobreviventeUpdate(request, pk):
    sobrevivente = SobreviventeModel.objects.get(id=pk)
    serializer = SobreviventeSerializer(instance=sobrevivente, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def sobreviventeUpdateLocalization(request, pk):
    sobrevivente = SobreviventeModel.objects.get(id=pk)
    
    sobrevivente.latitude = request.data.get('latitude')

    sobrevivente.longitude = request.data.get('longitude')

    sobrevivente.save(update_fields=['latitude', 'longitude'])

    return Response("Localização Atualizada", status=status.HTTP_200_OK)