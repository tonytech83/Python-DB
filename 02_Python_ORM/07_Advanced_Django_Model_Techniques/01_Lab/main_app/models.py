from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator, MaxLengthValidator
from django.db import models

from main_app.validators import validate_menu_categories


# Exam: 01. Restaurant
class Restaurant(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(2, message='Name must be at least 2 characters long.'),
            MaxLengthValidator(100, message='Name cannot exceed 100 characters.')
        ],
    )
    location = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(2, message='Location must be at least 2 characters long.'),
            MaxLengthValidator(200, message='Location cannot exceed 200 characters.')
        ],
    )
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[
            MinValueValidator(0, message='Rating must be at least 0.00.'),
            MaxValueValidator(5, message='Rating cannot exceed 5.00.')
        ]
    )


# Exam: 02. Menu
class Menu(models.Model):
    name = models.CharField(max_length=100, )
    description = models.TextField(
        validators=[validate_menu_categories]
    )
    restaurant = models.ForeignKey(
        to=Restaurant,
        on_delete=models.CASCADE,
    )


# Exam: 03. Restaurant Review
class RestaurantReview(models.Model):
    class Meta:
        # Made RestaurantReview model abstract based on exam 04. Restaurant Review Types
        abstract = True
        ordering = ['-rating']
        verbose_name = 'Restaurant Review'
        verbose_name_plural = 'Restaurant Reviews'
        unique_together = ['reviewer_name', 'restaurant']

    reviewer_name = models.CharField(max_length=100, )
    restaurant = models.ForeignKey(
        to=Restaurant,
        on_delete=models.CASCADE,
    )
    review_content = models.TextField()
    rating = models.PositiveIntegerField(validators=[
        MaxValueValidator(5)
    ])


# Exam: 04. Restaurant Review Types
class RegularRestaurantReview(RestaurantReview):
    pass


class FoodCriticRestaurantReview(RestaurantReview):
    class Meta(RestaurantReview.Meta):
        verbose_name = 'Food Critic Review'
        verbose_name_plural = 'Food Critic Reviews'

    food_critic_cuisine_area = models.CharField(max_length=100, )


# Exam: 05. Menu Review
class MenuReview(models.Model):
    class Meta:
        ordering = ['-rating']
        verbose_name = 'Menu Review'
        verbose_name_plural = 'Menu Reviews'
        unique_together = ['reviewer_name', 'menu']
        indexes = [models.Index(
            fields=['menu'],
            name='main_app_menu_review_menu_id'
        )]

    reviewer_name = models.CharField(max_length=100, )
    menu = models.ForeignKey(
        to=Menu,
        on_delete=models.CASCADE,
    )
    review_content = models.TextField()
    rating = models.PositiveIntegerField(validators=[
        MaxValueValidator(5)
    ])
