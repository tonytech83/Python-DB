from django.db import models

from main_app.validators import validate_customer_name, validate_customer_age, validate_customer_phone_number


# Exam: 01. Customer
class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[validate_customer_name]
    )

    age = models.PositiveIntegerField(
        validators=[validate_customer_age]
    )

    email = models.EmailField(
        error_messages={
            'invalid': "Enter a valid email address"
        }
    )

    phone_number = models.CharField(
        max_length=13,
        validators=[validate_customer_phone_number]
    )

    website_url = models.URLField(
        error_messages={
            'invalid': "Enter a valid URL"
        }
    )
