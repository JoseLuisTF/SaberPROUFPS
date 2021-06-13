from django import forms
from tempus_dominus.widgets import DateTimePicker


from apps.prueba.models import Matricula, Prueba, Respuesta


class PruebaForm(forms.ModelForm):
    class Meta:
        model = Prueba
        fields = [
            'hora_inicio',
            'programa_academico',
        ]
        labels = {
            'hora_inicio': 'Fecha y Hora de inicio',
            'programa_academico': 'Programa Academico',
        }
        widgets = {
            'hora_inicio': DateTimePicker(),
            'programa_academico': forms.Select(attrs={'class': 'form-control'}),
        }


class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = [
            'estudiante',
        ]
        labels = {
            'estudiante': 'Estudiante',
        }
        widgets = {
            'estudiante': forms.Select(attrs={'class': 'form-control'}),
        }


class ResolverPruebaForm(forms.ModelForm):



    class Meta:
        model = Respuesta
        fields = ('respuesta', )
