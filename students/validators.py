from django.core.exceptions import ValidationError

import students


def phone_number_validator(phone_number):
    if students.models.Students.objects.filter(phone_number=phone_number).exists():
        raise ValidationError(f"The phone number {phone_number} is already registeredd")
