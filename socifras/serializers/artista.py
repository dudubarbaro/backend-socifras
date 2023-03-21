from rest_framework.serializers import ModelSerializer
from socifras.models import Artista

class ArtistaSerializer(ModelSerializer):
    class Meta:
        model = Artista
        fields = "_all_"