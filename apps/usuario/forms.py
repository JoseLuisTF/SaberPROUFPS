from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.usuario.models import Estudiante, ProgramaAcademico, User
from django.db import transaction
from django.shortcuts import get_object_or_404



class EstudianteSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name',
                  'email')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_estudiante = True
        user.save()
        cod = user.username[0:3]
        pa= get_object_or_404(ProgramaAcademico, pk=str(cod))
        estudiante = Estudiante.objects.create(user=user, programa_academico=pa)
        print(estudiante.programa_academico)
        return user
        