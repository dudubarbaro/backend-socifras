from django.db import models
from socifras.models.genero import Genero
from socifras.models.artista import Artista
from socifras.models.videoaulas import VideoAulas
class Musica(models.Model):
    titulo = models.CharField(max_length=255)
    tom = models.CharField(max_length=10)
    videoaula = models.URLField(null= True, blank= True)

    generos = models.ForeignKey(
        Genero, on_delete=models.PROTECT, related_name="musicas"
    )
    videoaulas = models.ForeignKey(
        VideoAulas, on_delete=models.PROTECT, related_name="musicas"
    )
    artistas = models.ManyToManyField(
        Artista, related_name="musicas"
    )
    

    def _str_(self):
        return f"{self.titulo} ({self.artista})"