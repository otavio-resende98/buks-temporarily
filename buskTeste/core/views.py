from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

# Função utilizada para carregar uma tela contendo a página
# inicial do sistema, e suas funcionalidades.
@login_required
def home(request):
    # request.session.flush()
    return render(request, 'core/home.html')