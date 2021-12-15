import datetime

from django.core.exceptions import ValidationError

import students.models

adult_age = 18


def adult_validation(birthday):
    age = datetime.date.today().year - birthday.year
    if age < adult_age:
        raise ValidationError("Age should be greater than 18")


def phone_number_validator(phone_number):
    if students.models.Students.objects.filter(phone_number=phone_number).exists():
        raise ValidationError(f"The phone number {phone_number} is already registeredd")
