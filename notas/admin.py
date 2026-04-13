from django.contrib import admin
from .models import Nota

@admin.register(Nota)

class NotaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'contenido', 'creado', 'usuario')
    list_filter = ('creado', 'usuario')
    search_fields = ('titulo', 'contenido')
    ordering = ('-creado',)