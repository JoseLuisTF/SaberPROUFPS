from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime


from apps.usuario.models import ProgramaAcademico, Estudiante
from apps.bancopreguntas.models import Pregunta


class Prueba(models.Model):
    id_prueba = models.AutoField(primary_key=True)
    hora_inicio = models.DateTimeField()
    programa_academico = models.ForeignKey(
        ProgramaAcademico, on_delete=CASCADE)
    realizada = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.programa_academico, self.hora_inicio)


class Matricula(models.Model):
    id_matricula = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=CASCADE)
    prueba = models.ForeignKey(Prueba, on_delete=CASCADE)
    hora_inicio = models.DateTimeField()
    activa = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.prueba, self.estudiante)


class Respuesta(models.Model):
    id_respuesta = models.AutoField(primary_key=True)
    pregunta = models.ForeignKey(Pregunta, on_delete=CASCADE)
    respuesta = models.CharField(max_length=80)
    matricula = models.ForeignKey(Matricula, on_delete=CASCADE)
    correcta = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.pregunta, self.matricula)


class Nota(models.Model):
    id_nota = models.AutoField(primary_key=True)
    correcta = models.IntegerField()
    cantidad = models.IntegerField()
    matricula = models.ForeignKey(Matricula, on_delete=CASCADE)
    porcentaje = models.IntegerField()

    def __str__(self):
        return 'Respuestas correctas: {} - {}'.format(self.correcta, self.matricula)


class Cuadernillo(models.Model):
    id_cuadernillo = models.AutoField(primary_key=True)
    prueba = models.ForeignKey(Prueba, on_delete=CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.prueba, self.pregunta)
