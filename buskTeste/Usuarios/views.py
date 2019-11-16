from django.shortcuts import render, redirect
from .forms import Login_Form
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.

def login(request):
    try:
        username = request.session['username']
        return redirect('core:home')
    except:
        data = {}
        form = Login_Form(request.POST or None)
        if form.is_valid():
            info = form.cleaned_data
            user = authenticate(username=info['username'], password=info['password'])
            if user is not None:
                auth_login(request, user)
                request.session['username'] = user.username
                return redirect('core:home')
        else:
            data['form'] = form
            return render(request, 'Usuarios/login.html', data)



