import os
from typing import List

import django
from django.db.models import Case, When, Value, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, Laptop, ChessPlayer, Meal


#
# Exam: 01. Artwork Gallery
#
def show_highest_rated_art() -> str:
    the_art = ArtworkGallery.objects.order_by('-rating', 'id').first()

    return f'{the_art.art_name} is the highest-rated art with a {the_art.rating} rating!'


def bulk_create_arts(first_art, second_art) -> None:
    ArtworkGallery.objects.bulk_create([first_art, second_art])


def delete_negative_rated_arts() -> None:
    ArtworkGallery.objects.filter(rating__lt=0).delete()


# Test Code
# artwork1 = ArtworkGallery(artist_name="Vincent van Gogh", art_name="Starry Night", rating=4, price=1200000.0)
# artwork2 = ArtworkGallery(artist_name="Leonardo da Vinci", art_name="Mona Lisa", rating=5, price=1500000.0)
#
# # Bulk saves the instances
# bulk_create_arts(artwork1, artwork2)
# print(show_highest_rated_art())
# print(ArtworkGallery.objects.all())


#
# Exam: 02. Laptop
#
def show_the_most_expensive_laptop() -> str:
    the_laptop = (Laptop.objects
                  .order_by('-price', '-id')
                  .first())

    return f'{the_laptop.brand} is the most expensive laptop available for {the_laptop.price}$!'


def bulk_create_laptops(*args: List[Laptop]) -> None:
    Laptop.objects.bulk_create(*args)


def update_to_512_GB_storage() -> None:
    (Laptop.objects
     .filter(brand__in=["Asus", "Lenovo"])
     .update(storage=512))

    # Laptop.objects.filter(Q(brand='Asus') | Q(brand='Lenovo')).update(storage=512)


def update_to_16_GB_memory() -> None:
    (Laptop.objects
     .filter(brand__in=["Apple", "Dell", "Acer"])
     .update(memory=16))


def update_operation_systems() -> None:
    Laptop.objects.update(
        operation_system=Case(
            When(brand='Asus', then=Value('Windows')),
            When(brand='Apple', then=Value('MacOS')),
            When(brand__in=['Dell', 'Acer'], then=Value('Linux')),
            When(brand='Lenovo', then=Value('Chrome OS')),
            default=F('operation_system')
        )
    )


def delete_inexpensive_laptops() -> None:
    Laptop.objects.filter(price__lt=1200).delete()


# Test Code
# # Create three instances of Laptop
# laptop1 = Laptop(
#     brand='Asus',
#     processor='Intel Core i5',
#     memory=8,
#     storage=256,
#     operation_system='Windows',
#     price=899.99
# )
#
# laptop2 = Laptop(
#     brand='Apple',
#     processor='Apple M1',
#     memory=16,
#     storage=512,
#     operation_system='MacOS',
#     price=1399.99
#
# )
#
# laptop3 = Laptop(
#     brand='Lenovo',
#     processor='AMD Ryzen 7',
#     memory=12,
#     storage=512,
#     operation_system='Linux',
#     price=999.99,
# )
#
# # Create a list of instances
# laptops_to_create = [laptop1, laptop2, laptop3]
#
# # Use bulk_create to save the instances
# bulk_create_laptops(laptops_to_create)
#
# # Execute the following functions
# update_to_512_GB_storage()
# update_operation_systems()
#
# # Retrieve 2 laptops from the database
# asus_laptop = Laptop.objects.filter(brand__exact='Asus').get()
# lenovo_laptop = Laptop.objects.filter(brand__exact='Lenovo').get()
#
# print(asus_laptop.storage)
# print(lenovo_laptop.operation_system)


#
# Exam: 03. Chess Player
#
def bulk_create_chess_players(*args: List[ChessPlayer]) -> None:
    ChessPlayer.objects.bulk_create(*args)


def delete_chess_players() -> None:
    (ChessPlayer.objects
     .filter(title='no title')
     .delete())


def change_chess_games_won() -> None:
    (ChessPlayer.objects
     .filter(title='GM')
     .update(games_won=30))


def change_chess_games_lost() -> None:
    (ChessPlayer.objects
     .filter(title='no_title')
     .update(games_lost=25))


def change_chess_games_drawn() -> None:
    ChessPlayer.objects.all().update(games_drawn=10)


def grand_chess_title_GM() -> None:
    (ChessPlayer.objects
     .filter(rating__gte=2400)
     .update(title='GM'))


def grand_chess_title_IM() -> None:
    (ChessPlayer.objects
     .filter(rating__range=(2300, 2399))
     .update(title='IM'))


def grand_chess_title_FM() -> None:
    (ChessPlayer.objects
     .filter(rating__range=(2200, 2299))
     .update(title='FM'))


def grand_chess_title_regular_player() -> None:
    (ChessPlayer.objects
     .filter(rating__range=(0, 2199))
     .update(title='regular player'))


# Test Code
# # Create two instances of ChessPlayer
# player1 = ChessPlayer(
#     username='Player1',
#     title='no title',
#     rating=2200,
#     games_played=50,
#     games_won=20,
#     games_lost=25,
#     games_drawn=5,
# )
#
# player2 = ChessPlayer(
#     username='Player2',
#     title='IM',
#     rating=2350,
#     games_played=80,
#     games_won=40,
#     games_lost=25,
#     games_drawn=15,
# )
#
# # Call the bulk_create_chess_players function
# bulk_create_chess_players([player1, player2])
#
# # Call the delete_chess_players function
# delete_chess_players()
#
# # Check that the players are deleted
# print("Number of Chess Players after deletion:", ChessPlayer.objects.count())


#
# Exam: 04. Meal
#
def set_new_chefs() -> None:
    Meal.objects.update(
        chef=Case(
            When(meal_type='Breakfast', then=Value('Gordon Ramsay')),
            When(meal_type='Lunch', then=Value('Julia Child')),
            When(meal_type='Dinner', then=Value('Jamie Oliver')),
            When(meal_type='Snack', then=Value('Thomas Keller')),
            default=F('chef')
        )
    )


def set_new_preparation_times() -> None:
    Meal.objects.update(
        preparation_time=Case(
            When(meal_type='Breakfast', then=Value('10 minutes')),
            When(meal_type='Lunch', then=Value('12 minutes')),
            When(meal_type='Dinner', then=Value('15 minutes')),
            When(meal_type='Snack', then=Value('5 minutes')),
            default=F('preparation_time')
        )
    )


def update_low_calorie_meals() -> None:
    (Meal.objects
     .filter(meal_type__in=['Breakfast', 'Dinner'])
     .update(calories=400))


def update_high_calorie_meals() -> None:
    (Meal.objects
     .filter(meal_type__in=['Lunch', 'Snack'])
     .update(calories=700))


def delete_lunch_and_snack_meals() -> None:
    (Meal.objects
     .filter(meal_type__in=['Lunch', 'Snack'])
     .delete())
