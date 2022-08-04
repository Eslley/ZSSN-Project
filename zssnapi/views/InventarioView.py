from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from zssnapi.models import InventarioModel
from zssnapi.serializers import InventarioSerializer

@api_view(['GET'])
def inventariosList(request):
    inventarios = InventarioModel.objects.all()
    serializer = InventarioSerializer(inventarios, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def inventarioDetail(request, fk):
    inventarios = InventarioModel.objects.filter(sobrevivente=fk).values('item', 'quantidade')
    
    return Response(inventarios, status=status.HTTP_200_OK)

@api_view(['POST'])
def inventarioCreate(request):
    serializer = InventarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        