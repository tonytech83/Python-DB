import os
from datetime import date

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import RealEstateListing, VideoGame, BillingInfo, Invoice, Technology, Project, Programmer, Task, \
    Exercise

#
# Exam: 01. Real Estate Listing
# Test Code
#
# Create instances of RealEstateListing with locations
# RealEstateListing.objects.create(
#     property_type='House',
#     price=100000.00,
#     bedrooms=3,
#     location='Los Angeles'
# )
# RealEstateListing.objects.create(
#     property_type='Flat',
#     price=75000.00,
#     bedrooms=2,
#     location='New York City'
# )
#
# RealEstateListing.objects.create(
#     property_type='Villa',
#     price=250000.00,
#     bedrooms=4,
#     location='Los Angeles'  # Same location as the first instance
# )
#
# RealEstateListing.objects.create(
#     property_type='House',
#     price=120000.00,
#     bedrooms=3,
#     location='San Francisco'
# )

# Run the 'by_property_type' method
# house_listings = RealEstateListing.objects.by_property_type('House')
# print("House listings:")
# for listing in house_listings:
#     print(f"- {listing.property_type} in {listing.location}")
#
# # Run the 'in_price_range' method
# affordable_listings = RealEstateListing.objects.in_price_range(75000.00, 120000.00)
# print("Price in range listings:")
# for listing in affordable_listings:
#     print(f"- {listing.property_type} in {listing.location}")
#
# # Run the 'with_bedrooms' method
# two_bedroom_listings = RealEstateListing.objects.with_bedrooms(2)
# print("Two-bedroom listings:")
# for listing in two_bedroom_listings:
#     print(f"- {listing.property_type} in {listing.location}")
#
# # Run the 'popular_locations' method
# popular_locations = RealEstateListing.objects.popular_locations()
# print("Popular locations:")
# for location in popular_locations:
#     print(f"- {location['location']}")


#
# Exam: 02. Video Games Library
# Test Code
#
# # Create instances of VideoGame with real data
# game1 = VideoGame.objects.create(title="The Last of Us Part II", genre="Action", release_year=2020, rating=9.0)
#
# game2 = VideoGame.objects.create(title="Cyberpunk 2077", genre="RPG", release_year=2020, rating=7.2)
#
# game3 = VideoGame.objects.create(title="Red Dead Redemption 2", genre="Adventure", release_year=2018, rating=9.7)
#
# game4 = VideoGame.objects.create(title="FIFA 22", genre="Sports", release_year=2021, rating=8.5)
#
# game5 = VideoGame.objects.create(title="Civilization VI", genre="Strategy", release_year=2016, rating=8.8)

# # Run the custom manager methods
# action_games = VideoGame.objects.games_by_genre('Action')
# recent_games = VideoGame.objects.recently_released_games(2019)
# average_rating = VideoGame.objects.average_rating()
# highest_rated = VideoGame.objects.highest_rated_game()
# lowest_rated = VideoGame.objects.lowest_rated_game()
#
# # Print the results
# print(action_games)
# print(recent_games)
# print(average_rating)
# print(highest_rated)
# print(lowest_rated)


#
# Exam: 03. Shopaholic Haven
# Test Code
#
# # Create BillingInfo instances with real addresses
# billing_info_1 = BillingInfo.objects.create(address="456 Oak Lane, Boston, MA 02108")
#
# billing_info_2 = BillingInfo.objects.create(address="789 Maple Avenue, San Francisco, CA 94101")
#
# billing_info_3 = BillingInfo.objects.create(address="101 Pine Street, New York, NY 10001")
#
# # Create Invoice instances with related BillingInfo
# invoice_1 = Invoice.objects.create(invoice_number="INV007", billing_info=billing_info_1)
# invoice_2 = Invoice.objects.create(invoice_number="INV002", billing_info=billing_info_2)
# invoice_3 = Invoice.objects.create(invoice_number="INV004", billing_info=billing_info_3)

# # Get invoices starting with a specific prefix
# invoices_with_prefix = Invoice.get_invoices_with_prefix("INV")
# for invoice in invoices_with_prefix:
#     print(f"Invoice Number with prefix INV: {invoice.invoice_number}")

# # Get invoices sorted by invoice number
# invoices_sorted = Invoice.get_invoices_sorted_by_number()
# for invoice in invoices_sorted:
#     print(f"Invoice Number: {invoice.invoice_number}")

# # Get an invoice by a specific invoice number along with its related billing info
# invoice = Invoice.get_invoice_with_billing_info("INV002")
# print(f"Invoice Number: {invoice.invoice_number}")
# print(f"Billing Info: {invoice.billing_info.address}")


#
# Exam: 04. IT Sector
# Test Code
#
# # Create instances of Technology
# tech1 = Technology.objects.create(name="Python", description="A high-level programming language")
# tech2 = Technology.objects.create(name="JavaScript", description="A scripting language for the web")
# tech3 = Technology.objects.create(name="SQL", description="Structured Query Language")
#
# # Create instances of Project
# project1 = Project.objects.create(name="Web App Project", description="Developing a web application")
# project1.technologies_used.add(tech1, tech2)
#
# project2 = Project.objects.create(name="Database Project", description="Managing databases")
# project2.technologies_used.add(tech3)
#
# # Create instances of Programmer
# programmer1 = Programmer.objects.create(name="Alice")
# programmer2 = Programmer.objects.create(name="Bob")
#
# # Associate projects with programmers
# programmer1.projects.add(project1, project2)
# programmer2.projects.add(project1)

# # Execute the "get_programmers_with_technologies" method for a specific project
# specific_project = Project.objects.get(name="Web App Project")
# programmers_with_technologies = specific_project.get_programmers_with_technologies()
#
# # Iterate through the related programmers and technologies
# for programmer in programmers_with_technologies:
#     print(f"Programmer: {programmer.name}")
#     for technology in programmer.projects.get(name="Web App Project").technologies_used.all():
#         print(f"- Technology: {technology.name}")

# # Execute the "get_projects_with_technologies" method for a specific programmer
# specific_programmer = Programmer.objects.get(name="Alice")
# projects_with_technologies = specific_programmer.get_projects_with_technologies()
#
# # Iterate through the related projects and technologies
# for project in projects_with_technologies:
#     print(f"Project: {project.name} for {specific_programmer.name}")
#     for technology in project.technologies_used.all():
#         print(f"- Technology: {technology.name}")


#
# Exam: 05. Taskify
# Test Code
#
# # Create task instances with custom creation dates
# task1 = Task(
#     title="Task 1",
#     description="Description for Task 1",
#     priority="High",
#     creation_date=date(2023, 1, 15),
#     completion_date=date(2023, 1, 25)
# )
#
# task2 = Task(
#     title="Task 2",
#     description="Description for Task 2",
#     priority="Medium",
#     is_completed=True,
#     creation_date=date(2023, 2, 1),
#     completion_date=date(2023, 2, 10)
# )
#
# task3 = Task(
#     title="Task 3",
#     description="Description for Task 3",
#     priority="Hard",
#     is_completed=True,
#     creation_date=date(2023, 1, 15),
#     completion_date=date(2023, 1, 20)
# )
#
# # Save the tasks to the database
# task1.save()
# task2.save()
# task3.save()

# Now, you can run the defined methods

# # 1. Get overdue high-priority tasks
# overdue_high_priority = Task.overdue_high_priority_tasks()
# print("Overdue High Priority Tasks:")
# for task in overdue_high_priority:
#     print('- ' + task.title)

# # 2. Get completed medium-priority tasks
# completed_mid_priority = Task.completed_mid_priority_tasks()
# print("Completed Medium Priority Tasks:")
# for task in completed_mid_priority:
#     print('- ' + task.title)

# # 3. Search for tasks based on a query
# search_results = Task.search_tasks("Task 3")
# print("Search Results:")
# for task in search_results:
#     print('- ' + task.title)

# # 4. Get recent completed tasks
# recent_completed = task1.recent_completed_tasks(days=5)
# print("Recent Completed Tasks:")
# for task in recent_completed:
#     print('- ' + task.title)


#
# Exam: 06. Gym Session
# Test Code
#
# # Create instances of Exercise
# exercise1 = Exercise.objects.create(
#     name="Push-ups",
#     category="Strength",
#     difficulty_level=4,
#     duration_minutes=10,
#     repetitions=50,
# )
#
# exercise2 = Exercise.objects.create(
#     name="Running",
#     category="Cardio",
#     difficulty_level=7,
#     duration_minutes=20,
#     repetitions=0,
# )
#
# exercise3 = Exercise.objects.create(
#     name="Pull-ups",
#     category="Strength",
#     difficulty_level=13,
#     duration_minutes=35,
#     repetitions=20,
# )

# # Print the results
# long_and_hard_exercises = Exercise.get_long_and_hard_exercises()
# print("Long and hard exercises:")
# for exercise in long_and_hard_exercises:
#     print('- ' + exercise.name)

# short_and_easy_exercises = Exercise.get_short_and_easy_exercises()
# print("Short and easy exercises:")
# for exercise in short_and_easy_exercises:
#     print('- ' + exercise.name)

# exercises_within_duration = Exercise.get_exercises_within_duration(20, 40)
# print(f"Exercises within 20 - 40 minutes:")
# for exercise in exercises_within_duration:
#     print('- ' + exercise.name)

# exercises_with_difficulty_and_repetitions = Exercise.get_exercises_with_difficulty_and_repetitions(6, 15)
# print(f"Exercises with difficulty 6+ and repetitions 15+:")
# for exercise in exercises_with_difficulty_and_repetitions:
#     print('- ' + exercise.name)
