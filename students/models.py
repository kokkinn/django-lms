import datetime
import random

from core.models import Person

from dateutil.relativedelta import relativedelta

from django.db import models

from groups.models import Groups


class Students(Person):
    # phone_number = models.CharField(max_length=13, validators=[phone_number_validator])

    enroll_date = models.DateField(default=datetime.date.today)

    graduate_date = models.DateField(default=datetime.date.today)

    group = models.ForeignKey(
        Groups,
        on_delete=models.SET_NULL,
        null=True,
        related_name="students"
    )

    def __str__(self):
        return f"{self.first_name} {self.second_name} {self.age} {self.phone_number}"

    def save(self, *args, **kwargs):
        self.age = relativedelta(datetime.date.today(), self.birthday).years
        super().save(*args, **kwargs)

    @classmethod
    def _generate(cls):
        student = super()._generate()
        student.phone_number = random.randint(1000000, 9999999)
        student.save()
