from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from zssnapi.models import ItemModel
from zssnapi.serializers import ItemSerializer

@api_view(['GET'])
def itensList(request):
    itens = ItemModel.objects.all()
    serializer = ItemSerializer(itens, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def itemCreate(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def itemDelete(request, pk):
    try:
        item = ItemModel.objects.get(id=pk)
        item.delete()

        return Response({'message': 'Item Deletado'}, status=status.HTTP_200_OK)
    except ItemModel.DoesNotExist:
        return Response({'message': 'Item não encontrado'}, status=status.HTTP_404_NOT_FOUND)