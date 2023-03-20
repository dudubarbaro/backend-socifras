from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(null= True, blank= True)
    site = models.URLField(null= True, blank= True)

    def _str_(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Artistas"