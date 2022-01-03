from django import forms

from django_filters import FilterSet

from .models import Course


class CoursesFilter(FilterSet):
    class Meta:
        model = Course
        fields = {
            'course_name': ['exact'],
            'start_date': ['exact'],
            'group': ['exact'],
        }
        widgets = {'start_date': forms.DateInput(attrs={'type': 'date'})}


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ('start_date',)


class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ('start_date',)
