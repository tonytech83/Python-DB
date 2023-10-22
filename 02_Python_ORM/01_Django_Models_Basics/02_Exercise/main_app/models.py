from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()


class Blog(models.Model):
    post = models.TextField()
    author = models.CharField(max_length=35)


class WeatherForecast(models.Model):
    date = models.DateField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    precipitation = models.FloatField()


class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    ingredients = models.TextField()
    cook_time = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
