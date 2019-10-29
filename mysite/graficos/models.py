from django.db import models
from django.forms import ModelForm, ValidationError
# Create your models here.

class Grafico(models.Model):
    tipo = models.CharField(max_length=50, null=False)
    dadosx = models.CharField(max_length=1000, null=False, choices=[('l','linha'),('b','barra')])
    dadosy = models.CharField(max_length=1000, null=False)

class FormularioDoGrafico(ModelForm):
    class Meta:
        model = Grafico
        fields = ['dadosx', 'dadosy', 'tipo']
        labels = {
            'tipo': 'Tipo',
            'dadosx': "Valores de x",
            'dadosy': "Valores de y"
        }
