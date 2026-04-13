from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Nota
from .forms import NotaForm
from django.contrib import messages

def esta_en_grupo(request, grupo):
    return request.user.groups.filter(name=grupo).exists()



#Uso de ejemplo para class Based Views
#esta en vez de usar el decorador @login_required
#se usa el mixin LoginRequiredMixin para que el usuario este logueado
class VerNotasView(LoginRequiredMixin, ListView):
    model = Nota
    template_name = 'notas/ver_notas.html'
    context_object_name = 'notas'

    def get_queryset(self):
        if esta_en_grupo(self.request, 'editor'):
            return Nota.objects.all()
        else:
            return Nota.objects.filter(usuario=self.request.user)

@login_required
def buscar_nota_por_titulo(request):
    titulo = request.GET.get('titulo')
    notas = Nota.objects.filter(usuario=request.user, titulo__icontains=titulo)
    return render(request, 'notas/ver_notas.html', {'notas': notas})



@login_required
def crear_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.usuario = request.user
            nota.save()
            messages.success(request, 'Nota creada correctamente')
            return redirect('notas:ver_notas')
    else:
        form = NotaForm()
    return render(request, 'notas/crear_nota.html', {'form': form})

@login_required
def editar_nota(request, id):
    if esta_en_grupo(request, 'editor'):
        nota = get_object_or_404(Nota, id=id)
    else:
        nota = get_object_or_404(Nota, id=id, usuario=request.user)
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nota actualizada correctamente')
            return redirect('notas:ver_notas')
    else:
        form = NotaForm(instance=nota)
    return render(request, 'notas/crear_nota.html', {'form': form, 'editar': True})

@login_required
def eliminar_nota(request, id):
    if esta_en_grupo(request, 'editor'):
        nota = get_object_or_404(Nota, id=id)
    else:
        nota = get_object_or_404(Nota, id=id, usuario=request.user)
    nota.delete()
    messages.success(request, 'Nota eliminada correctamente')
    return redirect('notas:ver_notas')