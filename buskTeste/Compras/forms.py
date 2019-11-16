from django.forms import ModelForm
from django import forms
from .models import Compras

class DateInput(forms.DateInput):
    input_type = 'date'

class Cadastrar_Compra(ModelForm):

    class Meta:
        model = Compras
        fields = '__all__'
        # widgets = {
        #     'data': DateInput()
        # }   