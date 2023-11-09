from django.db import models

from main_app.validators import validate_customer_name, validate_customer_age, validate_customer_phone_number
from django.core.validators import MinLengthValidator


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


# Exam: 02. Media
class BaseMedia(models.Model):
    class Meta:
        abstract = True
        ordering = ['-created_at', 'title']

    title = models.CharField(max_length=100, )
    description = models.TextField()
    genre = models.CharField(max_length=50, )
    created_at = models.DateTimeField(auto_now=True, )


class Book(BaseMedia):
    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Book'
        verbose_name_plural = 'Models of type - Book'

    author = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(5, 'Author must be at least 5 characters long')
        ]
    )
    isbn = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(6, 'ISBN must be at least 6 characters long')
        ],
        unique=True,
    )


class Movie(BaseMedia):
    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Movie'
        verbose_name_plural = 'Models of type - Movie'

    director = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(8, 'Director must be at least 8 characters long')
        ]
    )


class Music(BaseMedia):
    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Music'
        verbose_name_plural = 'Models of type - Music'

    artist = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(9, 'Artist must be at least 9 characters long')
        ]
    )


# Exam: 03. Tax-Inclusive Pricing
class Product(models.Model):
    TAX_RATE = 0.08
    DISCOUNT_TAX_RATE = 0.05
    MULTIPLIER = 2.00
    DISCOUNT_MULTIPLIER = 1.50

    name = models.CharField(
        max_length=100,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    def calculate_tax(self):
        if self.__class__.__name__ == 'Product':
            tax_rate = Product.TAX_RATE
        else:
            tax_rate = Product.DISCOUNT_TAX_RATE

        return float(self.price) * tax_rate

    def calculate_shipping_cost(self, weight):
        if self.__class__.__name__ == 'Product':
            multiplier = Product.MULTIPLIER
        else:
            multiplier = Product.DISCOUNT_MULTIPLIER

        return float(weight) * multiplier

    def format_product_name(self) -> str:
        if self.__class__.__name__ == 'Product':
            product_type = self.__class__.__name__
        else:
            product_type = 'Discounted Product'

        return f'{product_type}: {self.name}'


class DiscountedProduct(Product):
    class Meta:
        proxy = True

    def calculate_price_without_discount(self):
        return float(self.price) * 1.20


# Exam: 04. Superhero Universe
class RechargeEnergyMixin(models.Model):
    def recharge_energy(self, amount: int):
        self.energy = min(self.energy + amount, 100)

        self.save()


class Hero(RechargeEnergyMixin, models.Model):
    name = models.CharField(max_length=100, )
    hero_title = models.CharField(max_length=100, )
    energy = models.PositiveIntegerField()


class SpiderHero(Hero):
    class Meta:
        proxy = True

    def swing_from_buildings(self) -> str:
        self.energy -= 80

        if self.energy <= 0:
            return f'{self.name} as Spider Hero is out of web shooter fluid'

        self.save()

        return f'{self.name} as Spider Hero swings from buildings using web shooters'


class FlashHero(Hero):
    class Meta:
        proxy = True

    def run_at_super_speed(self) -> str:
        self.energy -= 65

        if self.energy <= 0:
            return f'{self.name} as Flash Hero needs to recharge the speed force'

        self.save()

        return f'{self.name} as Flash Hero runs at lightning speed, saving the day'
