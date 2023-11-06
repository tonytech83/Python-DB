from datetime import date

from django.core.exceptions import ValidationError
from django.db import models


# Exam: 07. Veterinarian Availability
class BooleanChoiceField(models.BooleanField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = (
            (True, 'Available'),
            (False, 'Not Available')
        )
        kwargs['default'] = True
        super().__init__(*args, **kwargs)


# Exam: 01. Zoo Animals
class Animal(models.Model):
    name = models.CharField(
        max_length=100,
    )
    species = models.CharField(
        max_length=100,
    )
    birth_date = models.DateField()
    sound = models.CharField(
        max_length=100
    )

    # Exam: 06. Animal's Age
    @property
    def age(self):
        return (date.today() - self.birth_date).days // 365


class Mammal(Animal):
    fur_color = models.CharField(
        max_length=50,
    )


class Bird(Animal):
    wing_span = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )


class Reptile(Animal):
    scale_type = models.CharField(
        max_length=50,
    )


# Exam: 02. Zoo Employees
class Employee(models.Model):
    first_name = models.CharField(
        max_length=50,
    )
    last_name = models.CharField(
        max_length=50,
    )
    phone_number = models.CharField(
        max_length=10,
    )

    # Turns the model into an Abstract Base Class
    class Meta:
        abstract = True


class ZooKeeper(Employee):
    class Speciality(models.TextChoices):
        Mammals = 'Mammals'
        Birds = 'Birds'
        Reptiles = 'Reptiles'
        Others = 'Others'

    specialty = models.CharField(
        max_length=10,
        choices=Speciality.choices
    )
    managed_animals = models.ManyToManyField(
        to=Animal
    )

    # Exam: 04. Zookeeper's Specialty
    def clean(self):
        # check for other validations
        super().clean()

        # custom logic, clean method is before saving the data in db
        # it checks is data valid
        if self.specialty not in self.Speciality:
            raise ValidationError('Specialty must be a valid choice.')


class Veterinarian(Employee):
    license_number = models.CharField(
        max_length=10,
    )
    # Exam: 07. Veterinarian Availability
    availability = BooleanChoiceField()

    def is_available(self):
        return self.availability


# Exam: 03. Animal Display System
class ZooDisplayAnimal(Animal):
    class Meta:
        proxy = True

    # Exam: 05. Animal Display System Logic
    def __extra_info(self):
        extra_info = ''

        if hasattr(self, 'mammal'):
            extra_info = f' Its fur color is {self.mammal.fur_color}.'
        elif hasattr(self, 'bird'):
            extra_info = f' Its wingspan is {self.bird.wing_span} cm.'
        elif hasattr(self, 'reptile'):
            extra_info = f' Its scale type is {self.reptile.scale_type}.'

        return extra_info

    def display_info(self):
        return (f"Meet {self.name}! It's {self.species} and it's born {self.birth_date}."
                f" It makes a noise like '{self.sound}'!{self.__extra_info()}")

    def is_endangered(self):
        animals_at_risk = ["Cross River Gorilla", "Orangutan", "Green Turtle"]

        return True if self.species in animals_at_risk else False
