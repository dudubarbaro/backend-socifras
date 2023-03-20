from django.db import models

class Genero(models.Model):
    descricao = models.CharField(max_length=100)

    def _str_(self):
        return self.nome
    
class VideoAulas(models.Model):
    descricao = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)

    def _str_(self):
        return self.nome
    
class Artista(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(null= True, blank= True)
    site = models.URLField(null= True, blank= True)

    def _str_(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Artistas"

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











# Create your models here.
