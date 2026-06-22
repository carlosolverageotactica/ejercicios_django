from django.db import models
import datetime
from django.utils import timezone

class Pregunta(models.Model):
    pregunta_texto = models.CharField(max_length=200)
    publica_fecha = models.DateTimeField("fecha publicada")

    def __str__(self):
        return self.pregunta_texto

    def fue_publicada_recientemente(self):
        return self.publica_fecha >= timezone.now() - datetime.timedelta(days=1)

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion_texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.opcion_texto
