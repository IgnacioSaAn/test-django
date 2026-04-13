from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LoginForm
from django.contrib import messages
# Create your views here.

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cuentas:login')
    else:
        form = RegistroForm()
    return render(request, 'cuentas/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('notas:ver_notas')
        else:
            messages.error(request, 'Error al iniciar sesión')
    else:
        form = LoginForm(request)
    return render(request, 'cuentas/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('cuentas:login')

def ver_perfil(request):
    return render(request, 'cuentas/perfil.html')
