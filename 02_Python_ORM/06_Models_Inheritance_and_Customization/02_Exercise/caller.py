import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import BaseCharacter, Mage, Necromancer

#
# Exam: 01. Character Classes
# Test Code
#
# Create instances
# mage = Mage.objects.create(
#     name="Fire Mage",
#     description="A powerful mage specializing in fire magic.",
#     elemental_power="Fire",
#     spellbook_type="Ancient Grimoire"
# )
#
# necromancer = Necromancer.objects.create(
#     name="Dark Necromancer",
#     description="A mage specializing in dark necromancy.",
#     elemental_power="Darkness", spellbook_type="Necronomicon",
#     raise_dead_ability="Raise Undead Army"
# )
# print(mage.elemental_power)
# print(mage.spellbook_type)
# print(necromancer.name)
# print(necromancer.description)
# print(necromancer.raise_dead_ability)
