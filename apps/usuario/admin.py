from django.contrib import admin

from apps.usuario.models import ProgramaAcademico, Estudiante

admin.site.register(ProgramaAcademico)
admin.site.register(Estudiante)
