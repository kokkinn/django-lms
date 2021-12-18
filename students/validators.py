import datetime

from django.core.exceptions import ValidationError

import students.models


def adult_validation(birthday, age_limit=18):
    age = datetime.date.today().year - birthday.year
    if age < age_limit:
        raise ValidationError(f"Age should be greater than {age_limit}")


def phone_number_validator(phone_number):
    if students.models.Students.objects.filter(phone_number=phone_number).exists():
        raise ValidationError(f"The phone number {phone_number} is already registeredd")


class AdultValidator:
    def __init__(self, age_limit):
        self.age_limit = age_limit

    def __call__(self, *args, **kwargs):
        adult_validation(args[0], self.age_limit)