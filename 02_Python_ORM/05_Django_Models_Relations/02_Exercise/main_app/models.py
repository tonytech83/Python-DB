from django.db import models


# Exam: 01. Library
class Author(models.Model):
    name = models.CharField(
        max_length=40,
    )


class Book(models.Model):
    title = models.CharField(
        max_length=40,
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
        related_name='books'
    )


# Exam: 02. Music App
class Song(models.Model):
    pass
