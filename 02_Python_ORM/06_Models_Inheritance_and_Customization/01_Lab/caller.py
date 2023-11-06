import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Animal, Mammal, Bird, Reptile, ZooKeeper, Veterinarian, ZooDisplayAnimal

#
# Exam: 01. Zoo Animals
# Test Code
# Animal.objects.create(
#     name="Nemo",
#     species="Clownfish",
#     birth_date="2019-04-10",
#     sound="Bubbles"
# )
# Mammal.objects.create(
#     name="Fluffy",
#     species="Orangutan",
#     birth_date="2018-02-10",
#     sound="Chomps",
#     fur_color="Reddish-brown"
# )
# Bird.objects.create(
#     name="Robby",
#     species="American Robin",
#     birth_date="2021-03-20",
#     sound="Chirp",
#     wing_span=28.50
# )
# Reptile.objects.create(
#     name="Python",
#     species="Ball Python",
#     birth_date="2019-07-01",
#     sound="Hiss",
#     scale_type="Smooth"
# )
#
# animals = Animal.objects.all()
# for a in animals:
#     print(f"{a.name} is {a.species}.")


#
# Exam: 02. Zoo Employees
# Test Code
#
# zookeeper = ZooKeeper.objects.create(
#     first_name="Peter",
#     last_name="Johnson",
#     phone_number="0899524265",
#     specialty="Mammals"
# )
# mammal = Mammal.objects.get(name="Fluffy")
# zookeeper.managed_animals.add(mammal)
# veterinarian = Veterinarian.objects.create(
#     first_name="Dr. Michael",
#     last_name="Smith",
#     phone_number="9876543210",
#     license_number="VET12345"
# )
#
# zookeeper_from_db = ZooKeeper.objects.first()
# print(f"{zookeeper_from_db.first_name} {zookeeper_from_db.last_name} is a ZooKeeper.")
#
# veterinarian_from_db = Veterinarian.objects.first()
# print(f"{veterinarian_from_db.first_name} {veterinarian_from_db.last_name} is a Veterinarian.")


#
# Exam: 03. Animal Display System
# Test Code
#
# is_proxy = ZooDisplayAnimal._meta.proxy
#
# if is_proxy:
#     print("ZooDisplayAnimal is a proxy model.")
# else:
#     print("ZooDisplayAnimal is not a proxy model.")

#
# Exam: 04. Zookeeper's Specialty
#
# zookeeper = ZooKeeper(
#     first_name="John",
#     last_name="Doe",
#     phone_number="0123456789",
#     specialty="Fishes"
# )
# zookeeper.full_clean()
# zookeeper.save()
