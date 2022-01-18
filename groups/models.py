import datetime
import random
import string
from random import choice

from django.db import models
from faker import Faker


class Groups(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField(default=datetime.date.today)

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

    @classmethod
    def _generate(cls):
        from students.models import Students
        from teachers.models import Teacher
        f = Faker()
        letter = choice(string.ascii_uppercase)
        number = (list(range(1, 100)))
        students = list(Students.objects.filter(headman_group=None))
        teachers = list(Teacher.objects.all())
        obj = cls(
            name=random.choice(letter) + str(random.choice(number)),
            start_date=f.date_between_dates(datetime.date(2018, 1, 1), datetime.date(2022, 1, 1)),

            # headman=random.choice(students)
            # teachers=random.choices(teachers, k=3)
        )
        obj.save()

        return obj

    @classmethod
    def generate(cls, cnt):
        from students.models import Students
        if not Students.objects.all() or not Students.objects.filter(headman_group=None):
            # raise AttributeError("There are no students at all or there is no such students who is not a headman")
            pass
        # else:

        for _ in range(cnt):
            cls._generate()
