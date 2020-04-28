from django.core.exceptions import ValidationError


def phone_number_validator(phone):
    try:
        if phone:
            min_length = 10
            max_length = 15
            phone_number_length = (str(phone))
            if phone_number_length < min_length or phone_number_length > max_length:
                raise ValidationError('Contact number length is not valid')
    except(ValueError, TypeError):
        raise ValidationError('Enter the valid phone number')
    return phone

