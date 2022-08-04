import json
from rest_framework.views import APIView
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

    body_unicode = request.body.decode('utf-8') 	
    data = json.loads(body_unicode) 	

    sobrevivente.latitude = data['latitude']

    sobrevivente.longitude = data['longitude']

    sobrevivente.save(update_fields=['latitude', 'longitude'])

    return Response("Localização Atualizada", status=status.HTTP_200_OK)