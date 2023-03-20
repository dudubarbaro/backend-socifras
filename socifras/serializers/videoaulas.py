from rest_framework.serializers import ModelSerializer

from socifras.models import VideoAulas

class VideoAulasSerializer(ModelSerializer):
    class Meta:
        model = VideoAulas
        fields = "_all_"