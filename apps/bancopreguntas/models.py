from django.db import models
from django.db.models.deletion import CASCADE


class Competencia (models.Model):
    id_competencia = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return '{}'.format(self.nombre)

class Modulo (models.Model):
    id_modulo = models.AutoField(primary_key=True)
    competencia = models.ForeignKey(Competencia, on_delete=CASCADE)
    nombre = models.CharField(max_length=40)

    def __str__(self):
            return '{}: {}'.format(self.competencia, self.nombre)

class Pregunta (models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    modulo = models.ForeignKey(Modulo, on_delete=CASCADE)
    enunciado = models.TextField()
    opcion1 = models.CharField(max_length=80)
    opcion2 = models.CharField(max_length=80)
    opcion3 = models.CharField(max_length=80)
    opcionRespuesta = models.CharField(max_length=80)

    def __str__(self):
            return 'Pregunta: {} Modulo: {}'.format(self.id_pregunta, self.modulo)
    

