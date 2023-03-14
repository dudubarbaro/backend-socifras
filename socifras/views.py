from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from socifras.models import Musica, Artista, Genero, VideoAulas
from socifras.serializers import MusicaSerializer, ArtistaSerializer, MusicaDetailSerializer, GeneroSerializer, VideoAulasSerializer

class MusicaViewSet(ModelViewSet):
    queryset = Musica.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return MusicaDetailSerializer
        return MusicaSerializer

class ArtistaViewSet(ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

class GeneroViewSet(ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class VideoAulasViewSet(ModelViewSet):
    queryset = VideoAulas.objects.all()
    serializer_class = VideoAulasSerializer