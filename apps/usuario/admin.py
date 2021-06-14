from django.contrib import admin
from apps.usuario.models import ProgramaAcademico, User, Estudiante, Administrativo

admin.site.register(ProgramaAcademico)
admin.site.register(User)
admin.site.register(Estudiante)
admin.site.register(Administrativo)