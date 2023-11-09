from django.core.validators import ValidationError


# Exam: 01. Customer
def validate_customer_name(value: str):
    if not all(c.isalpha() or c.isspace() for c in value):
        raise ValidationError('Name can only contain letters and spaces')

    return value


def validate_customer_age(value: int):
    if value < 18:
        raise ValidationError(message="Age must be greater than 18")

    return value


def validate_customer_phone_number(value: str):
    if not all([
        (True if value[:4] == '+359' else False),
        (True if value[5:].isdigit() else False)]
    ):
        raise ValidationError("Phone number must start with a '+359' followed by 9 digits")
