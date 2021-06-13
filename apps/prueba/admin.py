from django.contrib import admin

from apps.prueba.models import Respuesta, Prueba, Matricula, Nota

admin.site.register(Respuesta)
admin.site.register(Prueba)
admin.site.register(Matricula)
admin.site.register(Nota)