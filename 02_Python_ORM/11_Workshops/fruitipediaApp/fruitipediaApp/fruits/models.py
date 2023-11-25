from django.db import models
from django.core.validators import MinLengthValidator

from fruitipediaApp.fruits.validators import only_letters


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            only_letters,
        ]
    )
    Image_url = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
