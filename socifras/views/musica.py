from rest_framework.viewsets import ModelViewSet
from socifras.models import Musica
from socifras.serializers import MusicaSerializer, MusicaDetailSerializer

class MusicaViewSet(ModelViewSet):
    queryset = Musica.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return MusicaDetailSerializer
        return MusicaSerializer
