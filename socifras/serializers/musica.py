from rest_framework.serializers import ModelSerializer, SlugRelatedField
from socifras.models import Musica

from uploader.models import Image
from uploader.serializers import ImageSerializer
class MusicaSerializer(ModelSerializer):

    capa = ImageSerializer(required=False)
    class Meta:
        model = Musica
        fields = "__all__"

class MusicaDetailSerializer(ModelSerializer):

    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = Musica
        fields = "__all__"
        depth = 1
    