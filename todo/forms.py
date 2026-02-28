from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o título da tarefa'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a descrição',
                'rows': 3
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
        }