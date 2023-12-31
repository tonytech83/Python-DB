import os
import django
from django.db.models import QuerySet, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


#
# Exam: 01. Pet
#
def create_pet(name: str, species: str):
    Pet.objects.create(
        name=name,
        species=species
    )

    return f"{name} is a very cute {species}!"


#
# Exam: 02. Artifact
#
def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )

    return f'The artifact {artifact.name} is {artifact.age} years old!'


def delete_all_artifacts():
    Artifact.objects.all().delete()


#
# Exam: 03. Location
#
def show_all_locations() -> str:
    locations = Location.objects.all().order_by('-id')

    return '\n'.join(str(l) for l in locations)


def new_capital() -> None:
    location = Location.objects.first()
    location.is_capital = True
    location.save()


def get_capitals() -> QuerySet:
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location() -> None:
    Location.objects.first().delete()


#
# Exam: 04. Car
#
def apply_discount() -> None:
    cars = Car.objects.all()

    for car in cars:
        discount = car.price * sum(int(x) for x in str(car.year)) / 100
        car.price_with_discount = car.price - discount
        car.save()


def get_recent_cars() -> QuerySet:
    return Car.objects.all().filter(year__gt=2020).values('model', 'price_with_discount')


def delete_last_car() -> None:
    Car.objects.last().delete()


#
# Exam: 05.	Task Encoder
#
def show_unfinished_tasks() -> str:
    unfinished_tasks = Task.objects.all().filter(is_finished=False)

    return '\n'.join(str(t) for t in unfinished_tasks)


def complete_odd_tasks() -> None:
    for task in Task.objects.all():
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str) -> None:
    decoded_text = ''.join(chr(ord(c) - 3) for c in text)
    Task.objects.filter(title=task_title).update(description=decoded_text)


#
# Exam: 06. Hotel Room
#
def get_deluxe_rooms() -> str:
    deluxe_rooms = HotelRoom.objects.filter(room_type="Deluxe")
    even_id_deluxe_rooms = []

    for room in deluxe_rooms:
        if room.id % 2 == 0:
            even_id_deluxe_rooms.append(str(room))

    return '\n'.join(even_id_deluxe_rooms)


def increase_room_capacity() -> None:
    rooms = HotelRoom.objects.all().order_by("id")

    previous_room_capacity = None

    for room in rooms:
        if not room.is_reserved:
            continue

        if previous_room_capacity:
            room.capacity += previous_room_capacity
        else:
            room.capacity += room.id

        previous_room_capacity = room.capacity

        room.save()


def reserve_first_room() -> None:
    first_room = HotelRoom.objects.first()
    first_room.is_reserved = True
    first_room.save()


def delete_last_room() -> None:
    last_room = HotelRoom.objects.last()

    if last_room.is_reserved:
        last_room.delete()


#
# Exam: 07. Character
#
def update_characters() -> None:
    Character.objects.filter(class_name='Mage').update(
        level=F('level') + 3,
        intelligence=F('intelligence') - 7
    )

    Character.objects.filter(class_name='Warrior').update(
        hit_points=F('hit_points') / 2,
        dexterity=F('dexterity') + 4
    )

    Character.objects.filter(class_name__in=['Assassin', 'Scout']).update(
        inventory='The inventory is empty',
    )


def fuse_characters(first_character: Character, second_character: Character) -> None:
    fusion_name = first_character.name + ' ' + second_character.name
    fusion_class_name = 'Fusion'
    fusion_level = int((first_character.level + second_character.level) // 2)
    fusion_strength = int((first_character.strength + second_character.strength) * 1.2)
    fusion_dexterity = int((first_character.dexterity + second_character.dexterity) * 1.4)
    fusion_intelligence = int((first_character.intelligence + second_character.intelligence) * 1.5)
    fusion_hit_points = first_character.hit_points + second_character.hit_points

    if first_character.class_name in ("Mage", "Scout"):
        fusion_inventory = 'Bow of the Elven Lords, Amulet of Eternal Wisdom'
    else:
        fusion_inventory = 'Dragon Scale Armor, Excalibur'

    Character.objects.create(
        name=fusion_name,
        class_name=fusion_class_name,
        level=fusion_level,
        strength=fusion_strength,
        dexterity=fusion_dexterity,
        intelligence=fusion_intelligence,
        hit_points=fusion_hit_points,
        inventory=fusion_inventory,
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity() -> None:
    Character.objects.update(
        dexterity=30,
    )


def grand_intelligence() -> None:
    Character.objects.update(
        intelligence=40,
    )


def grand_strength() -> None:
    Character.objects.update(
        strength=50,
    )


def delete_characters() -> None:
    Character.objects.filter(inventory='The inventory is empty').delete()
