from django import forms
from .models import *

class TableForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = [
            'name',
            'number',
        ]
