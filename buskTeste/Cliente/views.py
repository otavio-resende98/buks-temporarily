from django.shortcuts import render, redirect
from .forms import Cadastro_Cliente

# Create your views here.

def register_client(request):
    
    data = {}
    form = Cadastro_Cliente(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core:home')

    data['form'] = form

    return render(request, 'Cliente/register_client.html', data)