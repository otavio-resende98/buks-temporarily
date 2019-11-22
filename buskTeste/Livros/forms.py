from django.forms import ModelForm
from .models import Livro
from django import forms

# Formulário utilizado para cadastrar um livro no sistema.
class Cadastro_Livro(ModelForm):

    def __init__(self, *args, **kwargs):
        super(Cadastro_Livro, self).__init__(*args, **kwargs)
        self.fields['preco_compra'].localize = True
        self.fields['preco_compra'].widget.is_localized = True
        self.fields['preco_venda'].localize = True
        self.fields['preco_venda'].widget.is_localized = True

    class Meta:
        model = Livro
        fields = '__all__'
        widgets = {
            'capa': forms.FileInput()
        }

# Formulário utilizado para atualizar um livro já cadastrado no sistema.
class Alterar_Livro(ModelForm):

    def __init__(self, *args, **kwargs):
        super(Alterar_Livro, self).__init__(*args, **kwargs)
        self.fields['preco_compra'].localize = True
        self.fields['preco_compra'].widget.is_localized = True
        self.fields['preco_venda'].localize = True
        self.fields['preco_venda'].widget.is_localized = True

    class Meta:
        model = Livro
        fields = '__all__'
        widgets = {
            'capa': forms.FileInput()
        }

# Formulário para consultar os dados de um livro já cadastrado no sistema.
class Consultar_Livro(ModelForm):

    def __init__(self, *args, **kwargs):
        super(Consultar_Livro, self).__init__(*args, **kwargs)
        self.fields['preco_compra'].localize = True
        self.fields['preco_compra'].widget.is_localized = True
        self.fields['preco_venda'].localize = True
        self.fields['preco_venda'].widget.is_localized = True

    class Meta:
        model = Livro
        fields = '__all__'
        widgets = {
            'capa': forms.FileInput()
        }
