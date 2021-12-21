from django.core.exceptions import ValidationError

import teachers.models


def phone_number_validator(phone_number):
    if teachers.models.Teacher.objects.filter(phone_number=phone_number).exists():
        raise ValidationError(f"The phone number {phone_number} is already registered")
