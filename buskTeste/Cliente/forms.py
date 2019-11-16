from django.forms import ModelForm
from django import forms
from .models import Cliente

class DateInput(forms.DateInput):
    input_type = 'date'

class Cadastro_Cliente(ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'data_nasc': DateInput()
        }
    