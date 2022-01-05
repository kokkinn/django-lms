from django import forms
from django.forms import ChoiceField

from django_filters import FilterSet

from groups.models import Groups


class GroupBaseForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = "__all__"


class GroupCreateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        exclude = ["start_date", "headman"]


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


# class GroupUpdateForm(GroupsFilter):
#     class Meta(GroupsFilter.Meta):
#         fields = "__all__"
#         # exclude = ['start_date']

class GroupUpdateForm(GroupBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["headman_field"] = ChoiceField(
            choices=[(st.id, str(st)) for st in self.instance.students.all()],
            label="Headman",
            required=False
        )

    class Meta(GroupBaseForm.Meta):
        # fields = "__all__"
        exclude = ["start_date", "headman"]
