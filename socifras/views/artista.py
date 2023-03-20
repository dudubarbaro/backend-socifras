from rest_framework.viewsets import ModelViewSet
from socifras.models import Artista
from socifras.serializers import ArtistaSerializer

class ArtistaViewSet(ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer