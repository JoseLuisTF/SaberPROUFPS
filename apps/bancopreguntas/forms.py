from django import forms
from apps.bancopreguntas.models import Pregunta

class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = [
            'modulo',
            'enunciado',
            'opcion1',
            'opcion2',
            'opcion3',
            'opcionRespuesta'
        ]
        labels = {
            'modulo': 'Modulo',
            'enunciado': 'Enunciado',
            'opcion1': 'Opcion 1',
            'opcion2': 'Opcion 2',
            'opcion3': 'Opcion 3',
            'opcionRespuesta': 'Opcion Respuesta',
        }
        widgets = {
            'modulo': forms.Select(attrs={'class': 'form-control'}),
            'enunciado': forms.Textarea(attrs={'class': 'form-control','rows': 2}),
            'opcion1': forms.TextInput(attrs={'class': 'form-control'}),
            'opcion2': forms.TextInput(attrs={'class': 'form-control'}),
            'opcion3': forms.TextInput(attrs={'class': 'form-control'}),
            'opcionRespuesta': forms.TextInput(attrs={'class': 'form-control'}),
        }