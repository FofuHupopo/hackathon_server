from django.contrib import admin

from . import models


admin.site.register(models.ChildModel)
admin.site.register(models.RepresentativeModel)
admin.site.register(models.PassportModel)
