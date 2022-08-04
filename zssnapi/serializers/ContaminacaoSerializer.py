from rest_framework import serializers
from zssnapi.models import ContaminacaoModel

class ContaminacaoSerializer(serializers.ModelSerializer):

    class Meta:

        model = ContaminacaoModel
        fields = '__all__'