import datetime

from dateutil.relativedelta import relativedelta
from django.core.validators import MinLengthValidator
from django.db import models

from .validators import adult_validation
from .validators import phone_number_validator


class Students(models.Model):
    first_name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    second_name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    age = models.IntegerField()
    phone_number = models.CharField(max_length=13, validators=[phone_number_validator])
    birthday = models.DateField(default=datetime.date.today, validators=[adult_validation])

    def __str__(self):
        return f"{self.first_name} {self.second_name} {self.age}"

    def save(self, *args, **kwargs):
        self.age = relativedelta(datetime.date.today(), self.birthday).years
        super().save(*args, **kwargs)

    # @staticmethod
    # def generate_students(request):
    #     fake = Faker()
    #     countt = 10
    #
    #     if 'count' in request.GET:
    #         if request.GET['count'].isdigit():
    #             countt = int(request.GET['count'])
    #
    #     for _ in range(countt):
    #         st = Students(first_name=fake.first_name(),
    #                       second_name=fake.last_name(),
    #                       age=fake.pyint(12, 100))
    #         st.save()
    #
    #     return f'{countt} students were generatedd'
