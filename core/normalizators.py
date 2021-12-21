from django.core.exceptions import ValidationError


def normalize_phone(phone):
    phone = phone.strip(" ")
    for symb in phone:
        if not symb.isdigit():
            phone = phone.replace(symb, "")
    def_ph_len = 12
    if len(phone) != def_ph_len:
        raise ValidationError('Number entered incorrectly')
    return phone
#
# phonee = '913929292922'
# print(normalize_phone(phonee))