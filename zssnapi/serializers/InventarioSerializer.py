from rest_framework import serializers
from zssnapi.models import InventarioModel

class InventarioSerializer(serializers.ModelSerializer):

    class Meta:

        model = InventarioModel
        fields = '__all__'