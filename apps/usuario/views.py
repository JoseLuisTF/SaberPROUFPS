from apps.prueba import models
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView

from apps.usuario.models import User
from apps.usuario.forms import EstudianteSignUpForm

class EstudianteSignUpView(CreateView):
    model = User
    form_class = EstudianteSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Estudiante'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

    
class PerfilDetail(DetailView):
    model = User
    template_name = 'profile.html'