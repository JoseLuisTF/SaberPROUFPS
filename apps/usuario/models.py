from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

class ProgramaAcademico (models.Model):
    id_pa = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return '{}'.format(self.nombre)

class User(AbstractUser):
    is_estudiante = models.BooleanField(default=False)
    is_director = models.BooleanField(default=False)
    is_editor = models.BooleanField(default=False)


class Estudiante(models.Model):
    user = models.OneToOneField(User,on_delete=CASCADE,primary_key=True)
    programa_academico = models.ForeignKey(ProgramaAcademico, on_delete=CASCADE, null=True)

    def __str__(self):
        return '{} {} - {}'.format(self.user.first_name,self.user.last_name, self.user.username)

class Usuario(models.Model):
    user = models.OneToOneField(User,on_delete=CASCADE,primary_key=True)

class Administrativo(models.Model):
    user = models.OneToOneField(User,on_delete=CASCADE,primary_key=True)
    programa_academico = models.ForeignKey(ProgramaAcademico, on_delete=CASCADE)

    def __str__(self):
        return '{} {} - {}'.format(self.user.first_name,self.user.last_name, self.user.username)