from django import forms
from .models import Livros, Categoria

class CadastroLivro(forms.ModelForm):
    class Meta:
        model = Livros
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].widget = forms.HiddenInput()

class CategoriaLivro(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].widget = forms.HiddenInput()