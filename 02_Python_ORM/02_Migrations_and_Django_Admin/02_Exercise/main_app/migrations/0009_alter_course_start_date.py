# Generated by Django 4.2.4 on 2023-10-30 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
    ]