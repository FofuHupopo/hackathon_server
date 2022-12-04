from django.contrib import admin

from . import models


admin.site.register(models.CampEventModel)
admin.site.register(models.CampOrganizationModel)
