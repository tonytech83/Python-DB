# Exam: 02. Menu
from django.core.exceptions import ValidationError


def validate_menu_categories(value: str):
    required_categories = ("Appetizers", "Main Course", "Desserts")
    if not all(c.lower() in value.lower() for c in required_categories):
        raise ValidationError(
            'The menu must include each of the categories "Appetizers", "Main Course", "Desserts".'
        )
