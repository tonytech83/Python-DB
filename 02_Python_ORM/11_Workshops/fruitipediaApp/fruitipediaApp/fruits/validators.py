from django.core.exceptions import ValidationError


def only_letters(value: str):
    if any(char.isdigit() for char in value):
        raise ValidationError('Fruit name should contain only letters!')
