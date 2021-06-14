from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy
from datetime import datetime

from apps.prueba.models import Prueba, Matricula, Respuesta, Cuadernillo, Nota
from apps.prueba.forms import PruebaForm, MatriculaForm, ResolverPruebaForm
from apps.bancopreguntas.models import Modulo, Pregunta

# Create your views here.

@method_decorator([login_required], name='dispatch')
class PruebaCreate(CreateView):
    model = Prueba
    form_class = PruebaForm
    template_name = 'prueba/prueba_form.html'
    success_url = reverse_lazy('pruebas_programadas')

    def form_valid(self, form):
        pruebita = form.save()
        modulos = Modulo.objects.all()
        for modulo in modulos:

            preguntas = Pregunta.objects.filter(
                modulo=modulo).order_by('?')[:2]
            for pregunta in preguntas:
                Cuadernillo.objects.create(prueba=pruebita, pregunta=pregunta)
        return super().form_valid(form)

@method_decorator([login_required], name='dispatch')
class PruebaProgramadaList(ListView):
    model = Prueba
    template_name = 'prueba/prueba_list.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['pruebas'] = Prueba.objects.filter(
            realizada=False).order_by('hora_inicio')
        return context

@method_decorator([login_required], name='dispatch')
class PruebaProgramadaDetail(DetailView):
    model = Prueba
    template_name = 'prueba/prueba_details.html'

    def get_context_data(self, **kwargs):
        context = super(PruebaProgramadaDetail,self).get_context_data(**kwargs)
        context['estudiantes'] = Matricula.objects.filter(prueba=self.kwargs.get('pk'))
        return context

@method_decorator([login_required], name='dispatch')
class PruebaUpdate(UpdateView):
    model = Prueba
    form_class = PruebaForm
    template_name = 'prueba/prueba_form.html'
    success_url = reverse_lazy('prueba_programada_detalles')

    def get_success_url(self, **kwargs):

        return reverse_lazy("prueba_programada_detalles", kwargs={'pk': self.object.pk})

@method_decorator([login_required], name='dispatch')
class MatriculaCreate(CreateView):
    model = Matricula
    form_class = MatriculaForm
    template_name = 'prueba/matricula_form.html'
    success_url = reverse_lazy('prueba_programada_detalles')

    def form_valid(self, form):
        form.instance.prueba = Prueba.objects.get(pk=self.kwargs.get('pk'))
        form.instance.hora_inicio = datetime.now()
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('prueba_programada_detalles', kwargs={'pk': self.object.prueba.pk})

@method_decorator([login_required], name='dispatch')
class RespuestaCreate(CreateView):
    model = Respuesta
    form_class = ResolverPruebaForm
    template_name = 'prueba/respuesta_form.html'
    success_url = reverse_lazy('home')

@login_required
def resolverPrueba(request, pk):    

    matricula = get_object_or_404(Matricula, pk=pk)
    cuadernillos = Cuadernillo.objects.filter(prueba=matricula.prueba.pk)
    cantidad = Cuadernillo.objects.filter(prueba=matricula.prueba.pk).count()
    if request.method == 'POST':
        contador = 0
        Matricula.objects.filter(pk=matricula.pk).update(activa=False)
        Prueba.objects.filter(pk=matricula.prueba.pk).update(realizada=True)
        for cuadernillo in cuadernillos:


            if cuadernillo.pregunta.opcionRespuesta == request.POST.get(str(cuadernillo.pregunta.pk)):
                print('pase una vez')
                contador=contador+1
                print(contador)
                Respuesta.objects.create(pregunta=cuadernillo.pregunta, respuesta=request.POST.get(str(cuadernillo.pregunta.pk)),matricula=matricula, correcta = True)
            else:
                Respuesta.objects.create(pregunta=cuadernillo.pregunta, respuesta=request.POST.get(str(cuadernillo.pregunta.pk)),matricula=matricula, correcta=False)

        porcentaje = ((contador/cantidad)*100)
        Nota.objects.create(correcta=contador,matricula=matricula, cantidad = cantidad, porcentaje=porcentaje)
        return redirect('prueba_fin')

 
    return render(request, 'prueba/presentar_prueba.html',{'cuadernillos':cuadernillos})


@method_decorator([login_required], name='dispatch')
class PruebasActivasEstudiante(ListView):
    model = Matricula
    template_name = 'prueba/activas_estudiante.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(estudiante = self.kwargs['pk'], activa=True)

@method_decorator([login_required], name='dispatch')
class PruebasProgramadasEstudiante(ListView):
    model = Matricula
    template_name = 'prueba/programadas_estudiante.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(estudiante = self.kwargs['pk'], activa=False, prueba__realizada=False)

@method_decorator([login_required], name='dispatch')
class PruebasRealizadasEstudiante(ListView):
    model = Matricula
    template_name = 'prueba/realizadas_estudiante.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(estudiante = self.kwargs['pk'], activa=False, prueba__realizada=True)

@method_decorator([login_required], name='dispatch')
class NotaDetail(TemplateView):
    model = Nota
    template_name = 'prueba/nota_detalles.html'

    def get_context_data(self, **kwargs):
        context = {}
        context ['nota'] = Nota.objects.get(matricula=self.kwargs['pk'])
        context ['matricula'] = Matricula.objects.get(pk=self.kwargs['pk'])
        context ['respuestas'] = Respuesta.objects.filter(matricula=self.kwargs['pk'])
        return context 

@method_decorator([login_required], name='dispatch')
class PruebaFin(TemplateView):
    template_name = 'prueba/prueba_fin.html'

@method_decorator([login_required], name='dispatch')
class PruebasCalificadas(TemplateView):
    template_name = 'prueba/pruebas_calificadas.html'

    def get_context_data(self):
        context = {}
        context['pruebas'] = Prueba.objects.filter(realizada=True)
        print(context)
        return context

@method_decorator([login_required], name='dispatch')
class NotaList(ListView):
    model = Nota
    template_name = 'prueba/nota_listado.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['prueba'] = Prueba.objects.get(pk=self.kwargs['pk'])
        context['notas'] = Nota.objects.filter(matricula__prueba=self.kwargs['pk'])
        return context
