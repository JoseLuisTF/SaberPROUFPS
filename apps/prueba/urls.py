from django.urls import path
from . import views

from apps.prueba.views import PruebasCalificadas, NotaList, PruebaFin, NotaDetail, PruebasRealizadasEstudiante, PruebasProgramadasEstudiante, PruebasActivasEstudiante, MatriculaCreate, PruebaCreate, PruebaProgramadaList, PruebaProgramadaDetail, PruebaUpdate


urlpatterns = [
    path('crearPrueba/', PruebaCreate.as_view(), name='prueba_crear'),
    path('pruebasProgramadas/', PruebaProgramadaList.as_view(),name='pruebas_programadas'),
    path('pruebaProgramadaDetalles/<pk>/', PruebaProgramadaDetail.as_view(),name='prueba_programada_detalles'),
    path('pruebaProgramadaEditar/<pk>/', PruebaUpdate.as_view(),name='prueba_programada_actualizar'),
    path('matriculaCrear/<pk>/', MatriculaCreate.as_view(), name='matricula_crear'),
    path('resolverPrueba/<pk>/', views.resolverPrueba, name='resolver_prueba'),
    path('pruebasActivas/<pk>/', PruebasActivasEstudiante.as_view(), name='pruebas_activas_estudiante'),
    path('pruebasProgramadas/<pk>/', PruebasProgramadasEstudiante.as_view(), name='pruebas_programadas_estudiante'),
    path('pruebasRealizadas/<pk>/', PruebasRealizadasEstudiante.as_view(), name='pruebas_realizadas_estudiante'),
    path('pruebaResultado/<pk>/', NotaDetail.as_view(), name='prueba_resultado'),
    path('pruebaFin/', PruebaFin.as_view(), name='prueba_fin'),
    path('pruebasCalificadas/', PruebasCalificadas.as_view(), name='pruebas_calificadas'),
    path('verCalificaciones/<pk>/', NotaList.as_view(), name='notas_listar'),


]
