from django.forms import ChoiceField, MultipleChoiceField

from core.normalizators import normalize_phone

from django import forms

from django_filters import FilterSet


from .models import Teacher


class TeacherBaseForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherCreateForm(TeacherBaseForm):
    def __init__(self, *args, **kwargs):
        from groups.models import Groups
        super().__init__(*args, **kwargs)
        self.fields["group_field"] = MultipleChoiceField(
            choices=[(gr.id, str(gr)) for gr in Groups.objects.all()],
            label="Groups",
            required=False
        )

    # class Meta:
    #     exclude =

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        return normalize_phone(phone_number)

    @staticmethod
    def normalize_name(value):
        return value.lower().capitalize()

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return self.normalize_name(first_name)

    def clean_second_name(self):
        second_name = self.cleaned_data['second_name']
        return self.normalize_name(second_name)


class TeachersFilter(FilterSet):
    class Meta:
        model = Teacher
        fields = {
            "first_name": ["exact"],
            "second_name": ["exact"],
            "birthday": ["exact"],
            # "group": ["exact"]
        }


class TeacherUpdateForm(TeacherBaseForm):

    class Meta:
        model = Teacher
        fields = "__all__"
        # exclude = ['enroll_date', 'graduate_date']
