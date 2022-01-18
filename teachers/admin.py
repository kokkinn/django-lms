from django.contrib import admin

from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        "first_name", "second_name", 'phone_number', "specialization", "salary"
    ]

    fields = list_display


admin.site.register(Teacher, TeacherAdmin)
