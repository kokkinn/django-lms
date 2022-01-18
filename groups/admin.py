from django.contrib import admin
from .models import Groups

from students.models import Students
from teachers.models import Teacher


class StudentsInlineTable(admin.TabularInline):
    model = Students
    fields = [
        "first_name", "second_name", "birthday", "phone_number"
    ]

    extra = 0
    # readonly_fields = fields
    # show_change_link = True


class TeachersInlineTable(admin.TabularInline):
    model = Groups.teachers.through

    # fields = [
    #     "first_name", "second_name", 'phone_number', "specialization", "salary"
    # ]

    # extra = 0
    # readonly_fields = fields
    # show_change_link = True


class GroupsAdmin(admin.ModelAdmin):
    list_display = [
        "name", "start_date", 'headman',
    ]

    fields = [
        "name", "start_date", 'headman', "teachers",
    ]

    inlines = [StudentsInlineTable, TeachersInlineTable]


admin.site.register(Groups, GroupsAdmin)
