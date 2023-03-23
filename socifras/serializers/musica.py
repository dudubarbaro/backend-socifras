from rest_framework.serializers import ModelSerializer, SlugRelatedField
from socifras.models import Musica
from uploader.models import Image
from uploader.serializers import ImageSerializer
class MusicaSerializer(ModelSerializer):
    class Meta:
        model = Musica
        fields = "__all__"
        depth = 1
        capa_attachment_key = SlugRelatedField(
            source="capa",
            queryset=Image.objects.all(),
            slug_field="attachment_key",
            required=False,
            write_only=True,
        )
        capa = ImageSerializer(required=False, read_only=True)

class MusicaDetailSerializer(ModelSerializer):
    class Meta:
        model = Musica
        fields = "__all__"
        depth = 1
        capa = ImageSerializer(required=False)