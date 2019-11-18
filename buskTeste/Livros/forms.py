from django.forms import ModelForm
from .models import Livro
from django import forms


class Cadastro_Livro(ModelForm):

    class Meta:
        model = Livro
        fields = '__all__'
        widgets = {
            'capa': forms.FileInput()
        }


class Alterar_Livro(ModelForm):

    class Meta:
        model = Livro
        fields = '__all__'
        widgets = {
            'capa': forms.FileInput()
        }


class Consultar_Livro(ModelForm):

    class Meta:
        model = Livro
        fields = '__all__'
        widgets = {
            'capa': forms.FileInput()
        }
