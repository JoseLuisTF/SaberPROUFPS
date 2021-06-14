from django.contrib import admin
from apps.prueba.models import Prueba, Matricula, Respuesta, Nota, Cuadernillo

admin.site.register(Prueba)
admin.site.register(Matricula)
admin.site.register(Respuesta)
admin.site.register(Nota)
admin.site.register(Cuadernillo)