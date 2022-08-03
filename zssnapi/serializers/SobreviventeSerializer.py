from rest_framework import serializers
from zssnapi.models import SobreviventeModel

class SobreviventeSerializer(serializers.ModelSerializer):

    class Meta:

        model = SobreviventeModel
        fields = '__all__'