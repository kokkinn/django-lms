import random

from django.db import models

from core.models import Person
# from groups.models import Groups

# from teachers.validators import phone_number_validator


class Teacher(Person):
    specialization = models.CharField(max_length=70)

    # phone_number = models.CharField(
    #     max_length=13,
    #     blank=True,
    #     null=True,
    #     validators=[phone_number_validator]
    # )
    salary = models.PositiveIntegerField(default=1500)

    # group = models.ForeignKey(
    #     "groups.Groups",
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     related_name='teachers'
    # )

    @classmethod
    def _generate(cls):
        teacher = super()._generate()
        teacher.salary = random.randint(10000, 99999)
        teacher.save()


