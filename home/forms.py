from django import forms
from .models import tessiu

class registroTessiu(forms.ModelForm):
    class Meta:
        model = tessiu
        fields=[
            'name',
            'temperature',
            'color',
            'inflammation'
        ]
        labels = {
            'name':'Nombre',
            'temperature':'Temperatura',
            'color':'Color',
            'inflammation':'Inflamacion',
        }
        