from django.db import models

from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

from main_app.mixins import Content, Published
from main_app.mamagers import AuthorManager


class Author(models.Model):
    full_name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(3),
        ]
    )
    email = models.EmailField(unique=True, )
    is_banned = models.BooleanField(default=False)
    birth_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2005),
        ]
    )
    website = models.URLField(null=True, blank=True)

    objects = AuthorManager()

    def __str__(self):
        return self.full_name


class Article(Content, Published):
    class Category(models.TextChoices):
        TECHNOLOGY = 'Technology'
        SCIENCE = 'Science'
        EDUCATION = 'Education'

    title = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(5),
        ]
    )
    category = models.CharField(
        max_length=10,
        choices=Category.choices,
        default=Category.TECHNOLOGY
    )
    authors = models.ManyToManyField(
        to=Author,
    )

    def __str__(self):
        return self.title


class Review(Content, Published):
    rating = models.FloatField(
        validators=[
            MinValueValidator(1.0),
            MaxValueValidator(5.0)
        ]
    )
    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
        related_name='author_reviews'
    )
    article = models.ForeignKey(
        to=Article,
        on_delete=models.CASCADE,
        related_name='article_reviews'
    )
