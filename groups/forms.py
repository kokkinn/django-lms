from django import forms

from groups.models import Groups


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ['name', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }
