# Generated by Django 4.2.4 on 2023-10-20 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='last_edited_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]