import datetime

from dateutil.relativedelta import relativedelta
from django.core.validators import MinLengthValidator
from django.db import models
from faker import Faker
from faker.generator import random

from core.validators import AdultValidator


class Person(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    second_name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    age = models.IntegerField()
    phone_number = models.CharField(max_length=13)
    birthday = models.DateField(default=datetime.date.today, validators=[AdultValidator(18)])

    def __str__(self):
        return f"{self.__fullname()} {self.birthday}"

    def __fullname(self):
        return f"{self.first_name} {self.second_name}"

    def save(self, *args, **kwargs):
        if isinstance(self.birthday, str):
            self.birthday = datetime.datetime.strptime(self.birthday, "%Y-%m-%d")

        self.age = relativedelta(datetime.date.today(), self.birthday).years
        super().save(*args, **kwargs)

    @classmethod
    def _generate(cls):
        f = Faker()
        obj = cls(
            first_name=f.first_name(),
            second_name=f.last_name(),
            birthday=f.date_between(start_date="-65y", end_date="-18y"),
            phone_number=random.randint(1000000, 9999999)
        )
        obj.save()
        return obj

    @classmethod
    def generate(cls, cnt):
        from groups.models import Groups
        groups = Groups.objects.all()
        if groups:
            for _ in range(cnt):
                cls._generate()
        else:
            raise AttributeError("There are no available groups")
