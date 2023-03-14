from rest_framework.serializers import ModelSerializer

from socifras.models import Musica, Artista, Genero, VideoAulas

class MusicaSerializer(ModelSerializer):
    class Meta:
        model = Musica
        fields = "__all__"

class MusicaDetailSerializer(ModelSerializer):
    class Meta:
        model = Musica
        fields = "__all__"
        depth = 1

class ArtistaSerializer(ModelSerializer):
    class Meta:
        model = Artista
        fields = "_all_"

class GeneroSerializer(ModelSerializer):
    class Meta:
        model = Genero
        fields = "_all_"

class VideoAulasSerializer(ModelSerializer):
    class Meta:
        model = VideoAulas
        fields = "_all_"