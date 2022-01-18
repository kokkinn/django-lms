import datetime
import random

from faker import Faker

from core.models import Person

from dateutil.relativedelta import relativedelta

from django.db import models


class Students(Person):
    enroll_date = models.DateField(default=datetime.date.today)

    graduate_date = models.DateField(default=datetime.date.today)

    group = models.ForeignKey(
        "groups.Groups",
        on_delete=models.SET_NULL,
        null=True,
        related_name="students"
    )

    def __str__(self):
        return f"{self.first_name} {self.second_name} {self.age} {self.phone_number}"

    def save(self, *args, **kwargs):
        self.age = relativedelta(datetime.date.today(), self.birthday).years
        if self.group:
            self.enroll_date = self.group.start_date
            self.graduate_date = self.enroll_date + datetime.timedelta(days=120)
        super().save(*args, **kwargs)

    @classmethod
    def _generate(cls):
        student = super()._generate()

        from groups.models import Groups
        group = random.choice(list(Groups.objects.all()))

        student.enroll_date = group.start_date
        student.graduate_date = student.enroll_date + datetime.timedelta(days=120)
        student.group = group
        student.save()
