from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from zssnapi.models import InventarioModel
from zssnapi.serializers import InventarioSerializer

class InventarioList(APIView):

    def get(self, request):
        inventarios = InventarioModel.objects.all()
        serializer = InventarioSerializer(inventarios, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):

        data = {
            'sobrevivente': request.data.get('sobrevivente'), 
            'item': request.data.get('item'),
            'quantidade': request.data.get('quantidade')
        }
        serializer = InventarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)