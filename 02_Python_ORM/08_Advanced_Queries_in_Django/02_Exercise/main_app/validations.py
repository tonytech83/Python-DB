from django.core.exceptions import ValidationError
from decimal import Decimal


# Exam: 02. Video Games Library
def validate_rating(value: Decimal) -> None:
    if value < 0 or value > 10:
        raise ValidationError('The rating must be between 0.0 and 10.0')


def validate_release_year(value: int) -> None:
    if value < 1990 or value > 2023:
        raise ValidationError('The release year must be between 1990 and 2023')
