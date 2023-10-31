import os
import django
from datetime import datetime

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
# Create and check models
# Run and print your queries

from main_app.models import Student


# Exam: 01. Add Students
def add_students():
    students = [
        ('FC5204', 'John', 'Doe', '15/05/1995', 'john.doe@university.com'),
        ('FE0054', 'Jane', 'Smith', 'NULL', 'jane.smith@university.com'),
        ('FH2014', 'Alice', 'Johnson', '10/02/1998', 'alice.johnson@university.com'),
        ('FH2015', 'Bob', 'Wilson', '25/11/1996', 'bob.wilson@university.com')
    ]

    for student in students:
        student_id, first_name, last_name, birth_date, email = student

        if birth_date == "NULL":
            # This method first we create instance of Student model
            # at the end we should do student_to_add.save() to save the new instance into DB
            student_instance = Student(
                student_id=student_id,
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
            student_instance.save()
        else:
            # This method creates record directly into DB, without save
            Student.objects.create(
                student_id=student_id,
                first_name=first_name,
                last_name=last_name,
                birth_date=datetime.strptime(birth_date, '%d/%m/%Y').strftime('%Y-%m-%d'),
                email=email,
            )


# Test Code
# add_students()
# print(Student.objects.all())


# Exam: 02. Get Students Info
def get_students_info():
    result = []

    for student in Student.objects.all():
        result.append(
            f'Student №{student.student_id}: {student.first_name} {student.last_name}; Email: {student.email}'
        )

    return '\n'.join(result)


# Test Code
# print(get_students_info())


# Exam: 03. Update Students' Emails
def update_students_emails():
    new_domain = 'uni-students.com'

    def change_domain(email, domain):
        local_part, _ = email.split('@')
        new_email = f"{local_part}@{domain}"

        return new_email

    for student in Student.objects.all():
        student.email = change_domain(student.email, new_domain)
        student.save()

# Test Code
# update_students_emails()
# for student in Student.objects.all():
#     print(student.email)
