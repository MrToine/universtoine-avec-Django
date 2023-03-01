from django.db import models

class Informations(models.Model):
    name = models.CharField("Titre de la maintenance", max_length=255, default="Maintenance en cours")
    content = models.TextField("Contenu de la maintenance")
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return "Contenu de la maintenance"
    
    