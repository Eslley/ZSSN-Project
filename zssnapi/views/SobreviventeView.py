import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from zssnapi.models import SobreviventeModel, ContaminacaoModel
from zssnapi.serializers import SobreviventeSerializer
from zssnapi.serializers.ContaminacaoSerializer import ContaminacaoSerializer
from zssnapi.serializers.InventarioSerializer import InventarioSerializer

@api_view(['GET'])
def sobreviventesList(request):
    sobreviventes = SobreviventeModel.objects.all()
    serializer = SobreviventeSerializer(sobreviventes, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def sobreviventeDetail(request, pk):
    try:
        sobreviventes = SobreviventeModel.objects.get(id=pk)
        serializer = SobreviventeSerializer(sobreviventes, many=False)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    except SobreviventeModel.DoesNotExist:
        return Response({'message': 'Sobrevivente não encontrado'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def alertaInfectado(request, info, cont):
    try:
        if info == cont:
            return Response({'message': 'O informante nao pode ser o mesmo sobrevivente do relato'}, status=status.HTTP_200_OK)

        sobrevivente = SobreviventeModel.objects.get(id=cont)
        
        contaminacao = ContaminacaoModel.objects.filter(informante=info, infectado=cont)

        if sobrevivente.estaInfectado:
            return Response(sobrevivente.nome + " já está infectado(a)", status=status.HTTP_200_OK)
        else:
            if contaminacao.count():
                return Response({'message': 'Alerta sobre ' + sobrevivente.nome + ' já registrado'}, status=status.HTTP_200_OK)
            else:
                serializer = ContaminacaoSerializer(data={"informante": info, "infectado": cont})

                if serializer.is_valid():
                    serializer.save()

            sobrevivente.countAlertInfected += 1
            if sobrevivente.countAlertInfected == 3:
                sobrevivente.estaInfectado = True
                sobrevivente.save(update_fields=['estaInfectado', 'countAlertInfected'])
            else:
                sobrevivente.save(update_fields=['countAlertInfected'])
        
            return Response({'message': 'O alerta de infecção foi recebido'}, status=status.HTTP_200_OK)
    except SobreviventeModel.DoesNotExist:
        return Response({'message': 'Sobrevivente não encontrado'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def sobreviventeCreate(request):

    if request.data.get('inventario') == None:
        return Response({'message': 'É necessário declarar os itens do inventário'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        serializer = SobreviventeSerializer(data=request.data)
        if serializer.is_valid():
            s = serializer.save()

            inventario = request.data.get('inventario')

            for i in inventario:
                serializerI = InventarioSerializer(data={
                    "sobrevivente": s.id,
                    "item": i.get('id'),
                    "quantidade": i.get('quantidade')
                })

                if serializerI.is_valid():
                    serializerI.save()
        
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def sobreviventeDelete(request, pk):
    try:
        sobrevivente = SobreviventeModel.objects.get(id=pk)
        sobrevivente.delete()

        return Response({'message': 'Sobrevivente Deletado'}, status=status.HTTP_200_OK)
    except SobreviventeModel.DoesNotExist:
        return Response({'message': 'Sobrevivente não encontrado'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def sobreviventeUpdate(request, pk):
    try:
        sobrevivente = SobreviventeModel.objects.get(id=pk)
        serializer = SobreviventeSerializer(instance=sobrevivente, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    except SobreviventeModel.DoesNotExist:
        return Response({'message': 'Sobrevivente não encontrado'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def sobreviventeUpdateLocalization(request, pk):
    try:
        sobrevivente = SobreviventeModel.objects.get(id=pk)
        
        sobrevivente.latitude = request.data.get('latitude')

        sobrevivente.longitude = request.data.get('longitude')

        sobrevivente.save(update_fields=['latitude', 'longitude'])

        return Response({'message': 'Localização Atualizada'}, status=status.HTTP_200_OK)
    except SobreviventeModel.DoesNotExist:
        return Response({'message': 'Sobrevivente não encontrado'}, status=status.HTTP_404_NOT_FOUND)