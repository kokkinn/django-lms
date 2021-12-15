from django import forms

from core.normalizators import normalize_phone
from .models import Groups


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ['name', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }



