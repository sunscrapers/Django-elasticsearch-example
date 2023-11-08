from django.contrib import admin

from cars.models import Car
from cars.models import Manufacturer

admin.site.register(Car)
admin.site.register(Manufacturer)
