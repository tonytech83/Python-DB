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
    subjects = models.ManyToManyField(Subject)



