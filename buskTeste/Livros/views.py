from django.shortcuts import render, redirect
from .forms import Cadastro_Livro, Alterar_Livro, Consultar_Livro
from django.contrib.auth.decorators import login_required
import decimal
from .models import Livro
import time

# Create your views here.


@login_required
def register_book(request):

    data = {}

    form = Cadastro_Livro(request.POST or None, request.FILES or None)
    if form.is_valid():
        request.session['validRegisterBook'] = "sim"
        form.save()
        return render(request, 'Livros/register_book.html', data)
    else:
        request.session['validRegisterBook'] = "nao"
        data['form'] = form
        return render(request, 'Livros/register_book.html', data)


@login_required
def update_book_form(request, pk):

    data = {}

    livros = Livro.objects.get(pk=pk)
    form = Alterar_Livro(request.POST or None,
                         request.FILES or None, instance=livros)

    if form.is_valid():
        request.session['validUpdateBook'] = 'sim'
        request.session['validUpdateBookCont'] = 1
        form.save()
        return redirect('Livros:update_book')

    request.session['validUpdateBook'] = "nao"
    data['form'] = form

    return render(request, 'Livros/update_book_form.html', data)


@login_required
def update_book(request):

    data = {}

    try:
        if request.session['validUpdateBookCont'] == 0:
            request.session['validUpdateBook'] = "nao"
    except:
        None

    if request.method == "POST":
        name_book = request.POST['search_book']
        if name_book != "":
            livros = Livro.objects.filter(titulo=name_book)
            quant_livros = Livro.objects.filter(titulo=name_book).count()
            if quant_livros == 0:
                return render(request, 'Livros/update_book.html', data)
            else:
                data['Livros'] = livros
                return render(request, 'Livros/update_book.html', data)

    data['Livros'] = Livro.objects.all()

    try:
        request.session['validUpdateBookCont'] = 0
    except:
        None

    return render(request, 'Livros/update_book.html', data)


@login_required
def read_book(request):

    data = {}

    if request.method == "POST":
        name_book = request.POST['search_book']
        if name_book != "":
            livros = Livro.objects.filter(titulo=name_book)
            quant_livros = Livro.objects.filter(titulo=name_book).count()
            if quant_livros == 0:
                return render(request, 'Livros/update_book.html', data)
            else:
                data['Livros'] = livros
                return render(request, 'Livros/update_book.html', data)

    data['Livros'] = Livro.objects.all()

    return render(request, 'Livros/read_book.html', data)


@login_required
def delete_book(request):

    data = {}

    if request.method == "POST":
        name_book = request.POST['search_book']
        if name_book != "":
            livros = Livro.objects.filter(titulo=name_book)
            quant_livros = Livro.objects.filter(titulo=name_book).count()
            if quant_livros == 0:
                return render(request, 'Livros/update_book.html', data)
            else:
                data['Livros'] = livros
                return render(request, 'Livros/update_book.html', data)

    data['Livros'] = Livro.objects.all()

    return render(request, 'Livros/delete_book.html', data)


@login_required
def delete_book_confirm(request, pk):

    livro = Livro.objects.get(pk=pk)
    livro.delete()

    return redirect('Livros:delete_book')


@login_required
def read_book_form(request, pk):

    data = {}

    livros = Livro.objects.get(pk=pk)
    form = Consultar_Livro(request.POST or None,
                           request.FILES or None, instance=livros)

    data['Livro'] = livros
    data['form'] = form
    return render(request, 'Livros/read_book_form.html', data)
