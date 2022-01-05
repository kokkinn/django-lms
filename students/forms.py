from core.normalizators import normalize_phone

from django import forms

from django_filters import FilterSet

from .models import Students


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

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


class StudentsFilter(FilterSet):
    class Meta:
        model = Students
        fields = {
            "age": ["lt", "gt"],
            "first_name": ["exact"],
            "second_name": ["exact", 'startswith'],
            "group": ['exact']
        }


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"
        exclude = ['enroll_date', 'graduate_date']
