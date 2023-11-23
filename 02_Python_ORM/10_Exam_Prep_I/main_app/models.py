from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

from main_app.mixins import Person, Updated, Awarded
from main_app.managers import DirectorManager


class Director(Person):
    years_of_experience = models.SmallIntegerField(
        validators=[MinValueValidator(0)],
        default=0,
    )

    objects = DirectorManager()

    def __str__(self):
        return f'Director: {self.full_name}'


class Actor(Person, Awarded, Updated):
    def __str__(self):
        return f'Actor: {self.full_name}'


class Movie(Awarded, Updated):
    class Genre(models.TextChoices):
        ACTION = 'Action'
        COMEDY = 'Comedy'
        DRAMA = 'Drama'
        OTHER = 'Other'

    title = models.CharField(
        max_length=150,
        validators=[
            MinLengthValidator(5),
        ],
    )
    release_date = models.DateField()
    storyline = models.TextField(
        null=True,
        blank=True,
    )
    genre = models.CharField(
        max_length=6,
        choices=Genre.choices,
        default=Genre.OTHER,
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
        default=0
    )
    is_classic = models.BooleanField(default=False, )

    director = models.ForeignKey(
        to=Director,
        on_delete=models.CASCADE,
        related_name='movies'
    )
    starring_actor = models.ForeignKey(
        to=Actor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='movies'
    )
    actors = models.ManyToManyField(to=Actor, )

    def __str__(self):
        return f'Title: {self.title}'
