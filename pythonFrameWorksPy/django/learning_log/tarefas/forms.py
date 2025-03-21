from django import forms
from .models import TarefaModel

class TarefaForm(forms.ModelForm):
    class Meta:
        model = TarefaModel
        fields = ['name', 'description', 'completed']
        widgets= {
            'name': forms.TextInput(attrs={'class': 'nameInput', 'placeholder': 'Nome Tarefa'}),
            'description': forms.Textarea(attrs={'class': 'descriptionInput', 'placeholder': 'Descrição Tarefa'}),
            'completed': forms.CheckboxInput(attrs={'class': 'completedInput'})
        }