from rest_framework.viewsets import ModelViewSet
from socifras.models import VideoAulas
from socifras.serializers import VideoAulasSerializer

class VideoAulasViewSet(ModelViewSet):
    queryset = VideoAulas.objects.all()
    serializer_class = VideoAulasSerializer