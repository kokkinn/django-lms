from django import forms

from django_filters import FilterSet

from groups.models import Groups


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Groups
        # fields = ['name', 'start_date', 'end_date']
        fields = "__all__"
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }


class GroupsFilter(FilterSet):
    class Meta:
        model = Groups
        fields = [
            'name',
            'start_date',
            'end_date',
            'teachers',
            'students'
        ]


class GroupUpdateForm(GroupsFilter):
    class Meta(GroupsFilter.Meta):
        fields = "__all__"
        # exclude = ['start_date']
