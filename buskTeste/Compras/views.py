from django.shortcuts import render, redirect
from .forms import Cadastrar_Compra

# Create your views here.

def register_purchase(request):

    data = {}
    form = Cadastrar_Compra(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core:home')

    data['form'] = form
    return render(request, 'Compras/register_purchase.html', data)