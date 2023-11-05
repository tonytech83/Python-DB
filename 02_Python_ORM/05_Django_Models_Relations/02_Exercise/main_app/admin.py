from django.contrib import admin

from main_app.models import Car


#
# Exam: 06. Car Admin Setup
#
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'year', 'owner', 'car_details')

    @staticmethod
    def car_details(obj: Car) -> str:
        try:
            owner_name = obj.owner.name
        except AttributeError:
            owner_name = 'No owner'

        try:
            registration_number = obj.registration.registration_number
        except AttributeError:
            registration_number = 'No registration number'

        return f'Owner: {owner_name}, Registration: {registration_number}'

    # change the name of the column 'car_details' in admin portal to 'Car Details'.
    car_details.short_description = 'Car Details'
