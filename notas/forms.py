from django import forms
from .models import Nota

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['titulo', 'contenido']

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        if len(titulo) < 3:
            raise forms.ValidationError('El titulo debe tener al menos 3 caracteres')
        return titulo