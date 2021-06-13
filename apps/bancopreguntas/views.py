from apps.prueba import models
from typing import List
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy

from apps.bancopreguntas.models import Modulo, Pregunta
from apps.bancopreguntas.forms import PreguntaForm


class PreguntaCreate(CreateView):
    model = Pregunta
    form_class = PreguntaForm
    template_name = 'bancopreguntas/pregunta_form.html'
    success_url = reverse_lazy('modulos_listar')

    def get_success_url(self, **kwargs):

        return reverse_lazy("modulo_detalles", kwargs={'pk': self.object.modulo.pk})


class ModuloList(ListView):
    model = Modulo
    template_name = 'bancopreguntas/modulo_list.html'


class ModuloDetail(DetailView):
    model = Modulo
    template_name = 'bancopreguntas/modulo_details.html'

    def get_context_data(self, **kwargs):
        context = super(ModuloDetail, self).get_context_data(**kwargs)
        context['preguntas'] = Pregunta.objects.filter(
            modulo=self.kwargs.get('pk'))
        context['modulos'] = Modulo.objects.filter(
            id_modulo=self.kwargs.get('pk'))
        return context


class PreguntaUpdate(UpdateView):
    model = Pregunta
    form_class = PreguntaForm
    template_name = 'bancopreguntas/pregunta_form.html'
    success_url = reverse_lazy('modulo_detalles')

    def get_success_url(self, **kwargs):

        return reverse_lazy("modulo_detalles", kwargs={'pk': self.object.modulo.pk})


class PreguntaDelete(DeleteView):
    model = Pregunta
    template_name = 'bancopreguntas/pregunta_delete.html'
    success_url = reverse_lazy('modulo_detalles')

    def get_success_url(self, **kwargs):

        return reverse_lazy("modulo_detalles", kwargs={'pk': self.object.modulo.pk})

