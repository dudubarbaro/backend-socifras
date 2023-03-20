from rest_framework.viewsets import ModelViewSet
from socifras.models import Genero
from socifras.serializers import GeneroSerializer

class GeneroViewSet(ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
