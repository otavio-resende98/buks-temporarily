from django import forms
from django.core.validators import MinLengthValidator
from .models import User
from django.core.exceptions import ValidationError 

# Formulário utilizado para realizar o login no sistema e validação dos dados.
class Login_Form(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput, validators=[MinLengthValidator(8, message="Sua senha deve conter no mínimo 8 caracteres.")])

    # Função que realiza o tratamento e exibição de erro caso um usuário
    # inexistente no sistema tente fazer login.
    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('Nome de usuário inexistente no sistema!')
        
        return username

    # Função que realiza o tratamento e exibição de erro caso um usuário digite
    # a senha incorreta no sistema.
    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
            if not user.check_password(password):
                raise forms.ValidationError('A senha inserida está incorreta')
        except User.DoesNotExist:
            user = None

        return password
    