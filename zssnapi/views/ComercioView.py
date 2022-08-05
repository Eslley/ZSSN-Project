from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from zssnapi.serializers.ComercioSerializer import ComercioSerializer

@api_view(['POST'])
def negociar(request):
    serializer = ComercioSerializer(data=request.data)

    if serializer.is_valid():
        print(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data, status=status.HTTP_200_OK)
   
    