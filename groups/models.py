import datetime

from django.db import models

# from students.models import Students
# from teachers.models import Teacher


class Groups(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(null=True, blank=True)

    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    headman = models.OneToOneField(
        "students.Students",
        on_delete=models.SET_NULL,
        null=True,
        related_name="headman_group"
    )

    teachers = models.ManyToManyField(
        to="teachers.Teacher",
        related_name='groups'
    )

    def __str__(self):
        return f"{self.name} {self.start_date}"
