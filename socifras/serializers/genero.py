from rest_framework.serializers import ModelSerializer
from socifras.models import Genero

class GeneroSerializer(ModelSerializer):
    class Meta:
        model = Genero
        fields = "_all_"