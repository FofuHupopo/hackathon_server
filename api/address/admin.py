from django.contrib import admin

from . import models


class AddressModelAdmin(admin.ModelAdmin):
    list_display = ("country", "city")


admin.site.register(models.AddressModel, AddressModelAdmin)
