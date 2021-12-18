from core.normalizators import normalize_phone

from django import forms

from .models import Teacher


class TeacherCreateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'second_name', 'age', 'specialization', 'phone_number']

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