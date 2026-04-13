from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Nota

def esta_en_grupo(request, grupo):
    return request.user.groups.filter(name=grupo).exists()

# Create your views here.
@login_required
def ver_notas(request):    
    if esta_en_grupo(request, 'editor'):
        notas = Nota.objects.all()
        return render(request, 'notas/ver_notas.html', {'notas': notas})
    else:
        notas = Nota.objects.filter(usuario=request.user)
        return render(request, 'notas/ver_notas.html', {'notas': notas})

@login_required
def buscar_nota_por_titulo(request):
    titulo = request.GET.get('titulo')
    notas = Nota.objects.filter(usuario=request.user, titulo__icontains=titulo)
    return render(request, 'notas/ver_notas.html', {'notas': notas})



@login_required
def crear_nota(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        contenido = request.POST['contenido']
        nota = Nota(titulo=titulo,
         contenido=contenido, 
         usuario=request.user
        )
        nota.save()
        return redirect('ver_notas')
    return render(request, 'notas/crear_nota.html')

@login_required
def editar_nota(request, id):
    nota = get_object_or_404(Nota, id=id, usuario=request.user)
    if request.method == 'POST':
        titulo = request.POST['titulo']
        contenido = request.POST['contenido']
        nota.titulo = titulo
        nota.contenido = contenido
        nota.save()
        return redirect('ver_notas')
    return render(request, 'notas/crear_nota.html', {
        'editar': True,
        'titulo': nota.titulo,
        'contenido': nota.contenido,
    })

@login_required
def eliminar_nota(request, id):
    nota = get_object_or_404(Nota, id=id, usuario=request.user)
    nota.delete()
    return redirect('ver_notas')