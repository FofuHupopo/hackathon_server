from django.contrib import admin

from . import models

admin.site.site_header = "Админ-панель"

admin.site.register(models.ChildModel)
admin.site.register(models.BirthCertificateModel)

admin.site.register(models.RepresentativeModel)
admin.site.register(models.ForeignPassportModel)
admin.site.register(models.RussianPassportModel)
