from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from zssnapi.models import SobreviventeModel
from zssnapi.serializers import SobreviventeSerializer

class SobreviventeList(APIView):

    def get(self, request):
        sobreviventes = SobreviventeModel.objects.all()
        serializer = SobreviventeSerializer(sobreviventes, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):

        data = {
            'nome': request.data.get('nome'),
            'idade': request.data.get('idade'),
            'sexo': request.data.get('sexo'), 
            'latitude': request.data.get('latitude'), 
            'longitude': request.data.get('longitude'), 
            'sexo': request.data.get('sexo'), 
        }
        serializer = SobreviventeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
