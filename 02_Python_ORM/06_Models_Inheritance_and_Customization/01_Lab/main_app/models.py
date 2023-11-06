from django.core.exceptions import ValidationError
from django.db import models


# 01. Zoo Animals
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

        # custom logic
        if self.specialty not in self.Speciality:
            raise ValidationError('Specialty must be a valid choice.')


class Veterinarian(Employee):
    license_number = models.CharField(
        max_length=10,
    )


# Exam: 03. Animal Display System
class ZooDisplayAnimal(Animal):
    class Meta:
        proxy = True

# Exam: 04. Zookeeper's Specialty
