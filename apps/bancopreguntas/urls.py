from django.urls import path
from . import views

from apps.bancopreguntas.views import PreguntaCreate, ModuloList, ModuloDetail, PreguntaUpdate, PreguntaDelete


urlpatterns = [
    path('crear/', PreguntaCreate.as_view(), name='pregunta_crear'),
    path('listarModulos/', ModuloList.as_view(), name='modulos_listar'),
    path('verPreguntas/<pk>/', ModuloDetail.as_view(), name='modulo_detalles'),
    path('PreguntaEditar/<pk>/', PreguntaUpdate.as_view(), name='pregunta_editar'),
    path('eliminar/<pk>/', PreguntaDelete.as_view(), name='pregunta_eliminar'),


]