import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Restaurant, Menu
from django.core.exceptions import ValidationError

#
# Exam: 01. Restaurant
# Test Code
#
# valid_restaurant = Restaurant(
#     name="Delicious Bistro",
#     location="123 Main Street",
#     description="A cozy restaurant with a variety of dishes.",
#     rating=5.00,
# )
#
# try:
#     valid_restaurant.full_clean()
#     valid_restaurant.save()
#     print("Valid Restaurant saved successfully!")
# except ValidationError as e:
#     print(f"Validation Error: {e}")
#
# invalid_restaurant = Restaurant(
#     name="A",
#     location="A" * 201,
#     description="A restaurant with a long name and invalid rating.",
#     rating=5.01,
# )
#
# try:
#     invalid_restaurant.full_clean()
#     invalid_restaurant.save()
#     print("Invalid Restaurant saved successfully!")
# except Exception as e:
#     print(f"Validation Error: {e}")


#
# Exam: 02. Menu
# Test Code
#
# valid_menu = Menu(
#     name="Menu at The Delicious Bistro",
#     description="** Appetizers: **\nSpinach and Artichoke Dip\n** Main Course: **\nGrilled Salmon\n** Desserts: **\nChocolate Fondue",
#     restaurant=Restaurant.objects.first(),
# )
#
# try:
#     valid_menu.full_clean()
#     valid_menu.save()
#     print("Valid Menu saved successfully!")
# except ValidationError as e:
#     print(f"Validation Error: {e}")
#
# invalid_menu = Menu(
#     name="Incomplete Menu",
#     description="** Appetizers: **\nSpinach and Artichoke Dip",
#     restaurant=Restaurant.objects.first(),
# )
#
# try:
#     invalid_menu.full_clean()
#     invalid_menu.save()
#     print("Invalid Menu saved successfully!")
# except ValidationError as e:
#     print(f"Validation Error: {e}")
