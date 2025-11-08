# Ejercicio 21: form validation clean_titulo
from django import forms
from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','cuerpo']
    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo','')
        if len(titulo) < 5:
            raise forms.ValidationError('El título debe tener al menos 5 caracteres')
        return titulo
