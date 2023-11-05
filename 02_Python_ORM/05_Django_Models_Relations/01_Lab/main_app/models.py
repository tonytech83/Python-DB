from datetime import date

from django.db import models


# Exam: 01. The Lecturer
class Lecturer(models.Model):
    first_name = models.CharField(
        max_length=100,
    )
    last_name = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Subject(models.Model):
    name = models.CharField(
        max_length=100,
    )
    code = models.CharField(
        max_length=10,
    )
    lecturer = models.ForeignKey(
        to=Lecturer,
        on_delete=models.SET_NULL,
        null=True,
        related_name='subjects'
    )

    def __str__(self):
        return f'{self.name}'


# Exam: 02. The Student
class Student(models.Model):
    student_id = models.CharField(
        max_length=10,
        primary_key=True,
    )
    first_name = models.CharField(
        max_length=100,
    )
    last_name = models.CharField(
        max_length=100,
    )
    birth_date = models.DateField()
    email = models.EmailField(
        unique=True
    )
    subjects = models.ManyToManyField(to=Subject, through='StudentEnrollment')


# Exam: 03. The Enrollment
class StudentEnrollment(models.Model):
    class Grade(models.TextChoices):
        A = 'A'
        B = 'B'
        C = 'C'
        D = 'D'
        F = 'F'

    student = models.ForeignKey(
        to=Student,
        on_delete=models.CASCADE,
    )
    subject = models.ForeignKey(
        to=Subject,
        on_delete=models.CASCADE,
    )
    enrollment_date = models.DateField(
        default=date.today
    )
    grade = models.CharField(
        max_length=1,
        choices=Grade.choices
    )


# Exam: 04. The Lecturer Profile
class LecturerProfile(models.Model):
    lecturer = models.OneToOneField(
        to=Lecturer,
        on_delete=models.CASCADE,
    )
    email = models.EmailField(
        unique=True
    )
    bio = models.TextField(
        null=True,
        blank=True,
    )
    office_location = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
