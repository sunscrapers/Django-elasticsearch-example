from django.contrib import admin

from cars.models import (
    Car,
    Manufacturer,
)


admin.site.register(Car)
admin.site.register(Manufacturer)
