from django.contrib import admin

from . import models

admin.site.site_header = "Админ-панель"


class ChildModelAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "patronymic", "birthday_date")

class BirthCertificateModelAdmin(admin.ModelAdmin):
    list_display = ("series", "number")

class ForeignPassportModelAdmin(admin.ModelAdmin):
    list_display = ("series", "number")

class RussianPassportModelAdmin(admin.ModelAdmin):
    list_display = ("series", "number")

class RepresentativeModelAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "patronymic")




admin.site.register(models.ChildModel, ChildModelAdmin)
admin.site.register(models.BirthCertificateModel, BirthCertificateModelAdmin)

admin.site.register(models.RepresentativeModel, RepresentativeModelAdmin)
admin.site.register(models.ForeignPassportModel, ForeignPassportModelAdmin)
admin.site.register(models.RussianPassportModel, RussianPassportModelAdmin)
