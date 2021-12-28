from django.core.validators import MinLengthValidator
from django.db import models

from groups.models import Groups

from teachers.validators import phone_number_validator


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    second_name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    age = models.IntegerField()
    specialization = models.CharField(max_length=70)
    phone_number = models.CharField(
        max_length=13,
        blank=True,
        null=True,
        validators=[phone_number_validator]
    )

    group = models.ForeignKey(
        Groups,
        on_delete=models.SET_NULL,
        null=True,
        related_name='teachers'
    )

    def __str__(self):
        return f"{self.first_name} {self.second_name} {self.age} {self.specialization} {self.phone_number}"
