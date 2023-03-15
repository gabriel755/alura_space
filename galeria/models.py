from django.db import models

class fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    desc = models.TextField(null=False, blank=False)
    image = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return f"Fotografia [nome=(self.nome)]"
    