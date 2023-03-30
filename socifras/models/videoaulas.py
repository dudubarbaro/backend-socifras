from django.db import models
class VideoAulas(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)

    def _str_(self):
        return self.nome
