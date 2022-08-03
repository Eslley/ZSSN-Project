from rest_framework import serializers
from zssnapi.models import ItemModel

class ItemSerializer(serializers.ModelSerializer):

    class Meta:

        model = ItemModel
        fields = '__all__'