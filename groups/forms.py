from django import forms
from django.forms import ChoiceField

from django_filters import FilterSet

from groups.models import Groups


class GroupBaseForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = "__all__"


class GroupsFilter(FilterSet):
    class Meta:
        model = Groups
        fields = [
            'name',
            'start_date',
            'teachers',
            "headman"
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'})
        }


class GroupCreateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        exclude = ["headman"]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
        }


class GroupUpdateForm(GroupBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["headman_field"] = ChoiceField(
            choices=[(st.id, str(st)) for st in self.instance.students.all()],
            label="Headman",
            required=False
        )

    class Meta(GroupBaseForm.Meta):
        exclude = ["start_date", "headman"]
