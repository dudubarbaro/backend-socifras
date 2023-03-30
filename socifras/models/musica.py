from django.db import models
from socifras.models.genero import Genero
from socifras.models.artista import Artista
from socifras.models.videoaulas import VideoAulas
class Musica(models.Model):
    nome = models.CharField(max_length=255)
    generos = models.CharField(max_length=20)
    videoaula = models.URLField(null= True, blank= True)
    artistas = models.CharField(max_length=255)
    

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