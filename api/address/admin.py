from django.contrib import admin

from . import models


admin.site.register(models.AddressModel)
admin.site.register(models.CityModel)
admin.site.register(models.RegionModel)
