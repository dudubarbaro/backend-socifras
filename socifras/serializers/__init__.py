from rest_framework.serializers import ModelSerializer

from socifras.models import Musica, Artista, Genero, VideoAulas

from .artista import ArtistaSerializer
from .genero import GeneroSerializer
from .musica import MusicaDetailSerializer
from .videoaulas import VideoAulasSerializer
from .musica import MusicaSerializer