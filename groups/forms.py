from django import forms
from django_filters import FilterSet

from groups.models import Groups


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ['name', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }


class GroupsFilter(FilterSet):
    class Meta:
        model = Groups
        fields = {
            'name': ['exact', 'icontains'],
            'start_date': ['year__gt'],
            'end_date': ['lt', 'gt'],
            # 'teacher_name': ['exact', 'icontains'],
        }
