from rest_framework.serializers import ModelSerializer
from socifras.models import Musica

class MusicaSerializer(ModelSerializer):
    class Meta:
        model = Musica
        fields = "__all__"

class MusicaDetailSerializer(ModelSerializer):
    class Meta:
        model = Musica
        fields = "__all__"
        depth = 1
